@echo off

if not exist venv\windows_env (
    python -m venv venv\windows_env

    call venv\windows_env\Scripts\activate.bat

    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    
) else (
    call venv\windows_env\Scripts\activate.bat
)

python src\main.py

pause