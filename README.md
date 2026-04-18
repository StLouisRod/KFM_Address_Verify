# KirkFrancisMedia Python Project

A simple Python starter project with a `src` layout and basic tests.

## Quick start

1. Create and activate a virtual environment:
   - Windows (PowerShell):
     - `py -m venv .venv`
     - `.\.venv\Scripts\Activate.ps1`
2. Install dependencies:
   - `pip install -e .[dev]`
3. Run the app:
   - `python -m src.main`
   - or `kfm`
4. Run tests:
   - `pytest`

## Project metadata

Build and tool configuration lives in `pyproject.toml`.

TO RUN:
python -m src.main --sheet 'https://docs.google.com/spreadsheets/d/1AHR7X0Lz3Hs9u43PDH__i4MtDX2SUKd80fHLoX-v4Yc/edit?gid=1424304541#gid=1424304541' --creds 'secrets\service_account.json'
