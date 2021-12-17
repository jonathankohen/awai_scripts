"""Closes necessary applications for daily routine"""

import os
import subprocess


def main():
    comm_apps()
    coding_apps()
    misc_apps()
    os.system("sudo shutdown -h now")


def comm_apps():
    subprocess.call(["osascript", "-e", 'tell application "Zoom.us" to quit'])
    subprocess.call(["osascript", "-e", 'tell application "Trello" to quit'])
    subprocess.call(["osascript", "-e", 'tell application "Microsoft Outlook" to quit'])
    subprocess.call(["osascript", "-e", 'tell application "Microsoft Teams" to quit'])


def coding_apps():
    subprocess.call(["osascript", "-e", 'tell application "Google Chrome" to quit'])
    subprocess.call(["osascript", "-e", 'tell application "Visual Studio Code" to quit'])
    subprocess.call(["osascript", "-e", 'tell application "Adobe Dreamweaver 2021" to quit'])


def misc_apps():
    subprocess.call(["osascript", "-e", 'tell application "Notes" to quit'])
    subprocess.call(["osascript", "-e", 'tell application "Spotify" to quit'])


if __name__ == "__main__":
    main()
