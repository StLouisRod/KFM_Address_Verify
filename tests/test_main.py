from src.main import extract_sheet_id, main


def test_main_prints_message(capsys):
    exit_code = main([])
    captured = capsys.readouterr()
    assert "Hello from KirkFrancisMedia Python project!" in captured.out
    assert exit_code == 0


def test_extract_sheet_id_from_url_and_id():
    sheet_id = "1abcDEF_123-xyz"
    sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit#gid=0"

    assert extract_sheet_id(sheet_id) == sheet_id
    assert extract_sheet_id(sheet_url) == sheet_id
