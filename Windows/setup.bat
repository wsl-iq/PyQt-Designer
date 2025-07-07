@echo off
:: Check for admin privileges
:: If not running as admin, relaunch with admin rights
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~f0' -Verb runAs"
    exit /b
)

:: At this point, we are running as Administrator

:: Check if PyQt6 is installed
echo Checking if PyQt6 is installed...
python -m pip show PyQt6 >nul 2>&1
if errorlevel 1 (
    echo Installing PyQt6...
    pip install pyqt6
) else (
    echo PyQt6 is already installed.
)

:: Install pyqt6-tools (includes tools like pyuic6)
echo Installing pyqt6-tools...
pip install pyqt6-tools

:: Check and display the version of pyuic6
echo Checking pyuic6 version...
pyuic6 -V

:: Keep the window open
pause
