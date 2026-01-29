@echo off
cd /d "%~dp0"
echo Starting Vocabulary Quiz Server...
echo Please wait, opening browser...
start "" "http://localhost:8000"

:: Try using 'py' launcher first (standard on Windows)
py -m http.server 8000
if %errorlevel% equ 0 goto end

:: Fallback to 'python' if 'py' fails
python -m http.server 8000

:end
pause
