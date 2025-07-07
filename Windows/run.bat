@echo off
echo Trying to launch Qt Designer from pyqt6-tools...

:: Try to run designer via pyqt6-tools
pyqt6-tools designer

:: Check if the command failed
if errorlevel 1 (
    echo Failed to launch Qt Designer!
    echo Make sure pyqt6-tools is installed and the Scripts folder is in your PATH.
) else (
    echo Qt Designer should be running now...
)

pause
