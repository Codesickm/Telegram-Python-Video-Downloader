@echo off
title Telegram Video Downloader Setup
color 0A

echo ===========================================
echo    Telegram Video Downloader Installer
echo ===========================================

:: Check for Python
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed. Please install Python 3.x and re-run this script.
    pause
    exit /b
)

:: Create virtual environment (optional but clean)
echo.
echo [1/4] Creating virtual environment...
python -m venv venv

:: Activate virtual environment
call venv\Scripts\activate

:: Install required packages
echo.
echo [2/4] Installing Python requirements...
pip install --upgrade pip
pip install flask flask-cors telethon nest_asyncio

:: Optional: Install requirements from requirements.txt if you have one
:: pip install -r requirements.txt

:: Run the Flask app
echo.
echo [3/4] Starting Python server...
start cmd /k "python app.py"

:: Open the frontend HTML in default browser
echo.
echo [4/4] Opening website...
start "" index.html

echo.
echo Setup complete!
pause
