#!/bin/bash
# the file Requires sudo privileges to run
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root or use sudo."
    exit 1
fi

echo "Installing dependencies for Linux..."
sudo apt-get update
clear
echo "PyQt Designer Tools"
sudo apt-get install qttools5-dev-tools
# OR
sudo pip install PyQt5 --break-system-packages

exit_code=$?
if [ $exit_code -ne 0 ]; then
    echo "Failed to install qttools5-dev-tools. Please check your package manager."
    exit $exit_code
fi