@echo off

if not exist venv (
    python -m venv venv

    call venv\Scripts\activate.bat

    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    
) else (
    call venv\Scripts\activate.bat
)

python src\main.py

pause