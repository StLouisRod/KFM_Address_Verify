from __future__ import annotations

import argparse
import re
import sys
from typing import Sequence


def extract_sheet_id(sheet_ref: str) -> str:
    match = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", sheet_ref)
    if match:
        return match.group(1)
    return sheet_ref


def load_google_sheet(
    sheet_ref: str,
    worksheet: str | None = None,
    credentials_path: str | None = None,
) -> list[list[str]]:
    try:
        import gspread
    except ImportError as exc:
        raise RuntimeError(
            "Missing dependency 'gspread'. Install dependencies with: pip install -e .[dev]"
        ) from exc

    sheet_id = extract_sheet_id(sheet_ref)
    client = gspread.service_account(filename=credentials_path)
    spreadsheet = client.open_by_key(sheet_id)
    target_worksheet = spreadsheet.worksheet(worksheet) if worksheet else spreadsheet.sheet1
    return target_worksheet.get_all_values()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Load rows from a Google Sheet")
    parser.add_argument("--sheet", help="Google Sheet URL or sheet ID")
    parser.add_argument(
        "--worksheet",
        help="Worksheet/tab name. Defaults to first worksheet.",
    )
    parser.add_argument(
        "--creds",
        help="Path to Google service-account JSON credentials file.",
    )
    parser.add_argument(
        "--preview-rows",
        type=int,
        default=5,
        help="Number of rows to print as a preview.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if not args.sheet:
        print("Hello from KirkFrancisMedia Python project!")
        print("Pass --sheet <Google Sheet URL or ID> to load sheet rows.")
        return 0

    try:
        rows = load_google_sheet(args.sheet, args.worksheet, args.creds)
    except Exception as exc:
        print(f"Failed to load Google Sheet: {exc}", file=sys.stderr)
        return 1

    print(f"Loaded {len(rows)} rows from Google Sheet.")
    for row in rows[: max(args.preview_rows, 0)]:
        print(row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

