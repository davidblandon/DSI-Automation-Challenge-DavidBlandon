# The following code has the implementation for opening any program
import pyautogui
import time
from program_installed import installed
from identifiers.check import check_identifier


def open_program(open_app:str):

    if open_app == "":
        open_app = pyautogui.prompt('Enter the FULL NAME of the program you want to open')
        open_app.lower().strip()
    else:
        pass

    check_identifier(open_app)

    # Open the start menu
    pyautogui.press("win")  # Press the windows key
    time.sleep(0.5)

    # Look for the program to open
    pyautogui.write(open_app)
    time.sleep(0.5)

    installed(open_app)

    pyautogui.press("enter")  # Press enter to open the program


