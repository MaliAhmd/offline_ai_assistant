@echo off
cd /d "%~dp0"

echo Starting Offline AI Assistant (API Server)...

call myenv\Scripts\activate.bat
uvicorn api.main:app --host 127.0.0.1 --port 8000 --reload

pause
