@echo off
title Telegram Video Downloader Runner
color 0A

echo ===========================================
echo    Telegram Video Downloader Runner
echo ===========================================

:: Activate virtual environment
call venv\Scripts\activate

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
