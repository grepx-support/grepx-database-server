@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%.."

cd /d "%SCRIPT_DIR%"

if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

echo Installing test dependencies...
pip install -r requirements.txt

echo Running tests...
pytest -v --tb=short

deactivate
