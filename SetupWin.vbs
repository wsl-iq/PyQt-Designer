Set shell = CreateObject("WScript.Shell")

' Title
WScript.Echo "Installing Python libraries..."

' Python pip install commands
shell.Run "cmd /c pip install platform winshell pywin32 prettytable keyboard", 1, True

WScript.Echo "Installation complete!"
