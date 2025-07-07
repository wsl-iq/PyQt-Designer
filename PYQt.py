#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2025 
# Developer : Mohammed Al-Baqer

__Developer__ = "Mohammed Al-Baqer"
__Copyright__ = "Copyright (c) 2025"
__version__ = "1.0.0"
__Instagram__ = "@wsl.iq"

import os
import sys
import time
import keyboard
import subprocess
import platform
import winshell
import webbrowser
from win32com.client import Dispatch
from datetime import datetime
from prettytable import PrettyTable

S = "\033[0m"        # Reset
R = "\033[91;1m"     # Red
G = "\033[92;1m"     # Green
B = "\033[94;1m"     # Blue
Y = "\033[93;1m"     # Yellow
C = "\033[96;1m"     # Cyan
M = "\033[95;1m"     # Magenta
W = "\033[97;1m"     # White
D = "\033[90;1m"     # Grey
P = "\033[38;5;198m" # Pink
O = "\033[38;5;202m" # Orange

Press = "\033[91;1m" + "[" + "\033[93;1m" + "Ctrl" + "\033[97;1m" + " + " + "\033[93;1m" + "C" + "\033[91;1m" + "]" + "\033[97;1m"
Confirm = "\033[97;1m" + "Do you want to Remove Administrator from disk (D)" + "\033[92;1m" + " continue" + "\033[97;1m" + " or" + "\033[91;1m" + " exit" + "\033[93;1m" + " ? " + "\033[97;1m" + "(" + "\033[94;1m" + "c " + "\033[97;1m" + ";" + "\033[91;1m" + " e" + "\033[97;1m" + ")"
Okay = "\033[92;1m" + "[" + "\033[94;1m" + "Okay" + "\033[92;1m" + "]" + "\033[94;1m"
Enter = "\033[94;1m" + "[" + "\033[92;1m" + "+" + "\033[94;1m" + "]" + "\033[92;1m"
sign = "\033[92;1m" + "[" + "\033[94;1m" + "*" + "\033[92;1m" + "]" + "\033[94;1m"

def ASCLLART(prompt: str) -> str:
    return input(f"\033[91;1m┌─[\033[95;1mMohammed Al-Baqer\033[93;1m@\033[94;1mWSL.IQ\033[91;1m]─[\033[92;1m{prompt}\033[91;1m]\n└──╼\033[91;1m>\033[93;1m>\033[92;1m>\033[97;1m ")

def DateTime():
    try:
        times = datetime.now()
        formatted_time = times.strftime("%I:%M:%S %p")
        formatted_day = times.strftime("%A")
        date_day = (
            "\033[94;1m" + "[" + "\033[92;1m" + "Today" + "\033[94;1m" + "]" +
            "\033[97;1m" + "(" + "\033[93;1m" + formatted_day +
            "\033[95;1m" + f" {times:%B %d %Y}" +
            "\033[97;1m" + ") " + "\033[94;1m" + "[" +
            "\033[92;1m" + "Time" + "\033[94;1m" + "]" +
            "\033[93;1m" + "[" + "\033[91;1m" + formatted_time +
            "\033[93;1m" + "]" + "\033[97;1m"
        )
        return date_day
    except Exception as e:
        return str(e)

DateTimming = DateTime()
table = PrettyTable()

class Main:
    def __init__(self):
        self.start_time = time.time()
        self.log_file = "log.txt"
        with open(self.log_file, "a", encoding="utf-8") as log:
            log.write(f"[START] {time.ctime()}\n")

    def main(self):
        try:
            while True:
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
                sys.path.append(os.path.dirname(os.path.abspath(__file__)))

                if keyboard.is_pressed('q') or keyboard.is_pressed('Q'):
                    print(W + '\nQuit')
                    break

                elif keyboard.is_pressed('Ctrl') and keyboard.is_pressed('C'):
                    break

                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'''                           
 {G}_____     _____ _      {B}____          _         {W}
{G}|  _  |_ _|     | |_   {B}|    \ ___ ___|_|___ ___ {W}
{G}|   __| | |  |  |  _|  {B}|  |  | -_|_ -| | . |   |{W}
{G}|__|  |_  |__  _|_|    {B}|____/|___|___|_|_  |_|_|{W}
   {G}   |___|  |__|         {B}             |___|    {W}
            {B}Developer {W}: {G}{__Developer__}
            {Y}Copyright {W}: {G}{__Copyright__}
            {G}Version   {W}: {G}{__version__}
            {O}Instagram {W}: {B}{__Instagram__}
            {B}Date Time {W}: {G}{DateTimming}
''')
                system = platform.system()
                if system == 'Windows':
                    os.system(r'Windows\python setup.py')
                    running = ASCLLART('Do you run app? (y/n)')
                    if running == 'y':
                        desktop = winshell.desktop()
                        path = os.path.join(desktop, "PyQt6 Designer.lnk")
                        shortcut = Dispatch('WScript.Shell').CreateShortCut(path)
                        shortcut.TargetPath = "cmd.exe"
                        shortcut.Arguments = '/k pyqt6-tools designer'
                        shortcut.WorkingDirectory = os.getcwd()
                        shortcut.IconLocation = "cmd.exe"
                        shortcut.save()
                        break
                    elif running == 'n':
                        sys.exit(1)

                elif system == 'Linux':
                    os.system('chmod +x *')
                    os.system(r'Linux\bash setup.sh')
                    run = ASCLLART('Do you run app? (y/n)')
                    if run == 'y' or run == 'Y':
                        os.system(r'Linux\run.sh')
                        break
                    elif run == 'n' or run == 'N':
                        sys.exit(1)
                    
                    break

                elif system == 'Darwin' or system == 'macOS':
                    webbrowser.open_new('https://www.qt.io/quality-assurance/download')
                    break

                else:
                    continue

        except KeyboardInterrupt:
            print(W + '\nExiting...')
            time.sleep(1)
        finally:
            duration = time.time() - self.start_time
            with open(self.log_file, "a", encoding="utf-8") as log:
                log.write(f"[END] {time.ctime()} - Duration: {duration:.2f} seconds\n\n")
            print(f"Session lasted: {duration:.2f} seconds.")
            sys.exit()

if __name__ == "__main__":
    Main().main()
