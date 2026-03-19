@echo off
cd /d "%~dp0"

echo Starting Offline AI Assistant Terminal Mode...

call myenv\Scripts\activate.bat
python chat_cli.py

pause
