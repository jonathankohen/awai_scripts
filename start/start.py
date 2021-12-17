"""Initializes necessary applications for daily work."""


import os, sys
import webbrowser
import pyautogui
import time


CURRENT = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(CURRENT)
sys.path.append(PARENT)

from theme import Colors, logo


def main():
    comm_apps()
    coding_apps()

    time.sleep(22)
    os.system("clear")
    print(f"{Colors.OKBLUE}{logo}{Colors.ENDC}")
    print(f"{Colors.WARNING}Welcome, Jon!{Colors.ENDC}\n")
    os.system("open /Applications/iTerm.app")
    pyautogui.keyDown("command")
    pyautogui.keyDown("option")
    pyautogui.press("h")
    os.system("open /Applications/Microsoft\ Teams.app")


def comm_apps():
    os.system("open -g /Applications/Microsoft\ Outlook.app")
    os.system("open -g /Applications/Microsoft\ Teams.app")
    os.system("open -g /Applications/zoom.us.app")
    os.system("open -g /Applications/Trello.app")


def coding_apps():
    webbrowser.open("https://www.awai.com/edit/", new=2)
    os.system("open -g /Applications/Visual\ Studio\ Code.app")
    os.system("open -g /Applications/Adobe\ Dreamweaver\ 2021/Adobe\ Dreamweaver\ 2021.app")


if __name__ == "__main__":
    main()
