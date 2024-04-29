# The following code checks if the program is installed in the pc

import sys
import pyautogui

def installed(program):
    pyautogui.useImageNotFoundException()
    try:
        location = pyautogui.locateOnScreen(f"app/src/opening_programs/identifiers/{program}.png", confidence=0.9)
    except pyautogui.ImageNotFoundException:
        pyautogui.alert("The program was not found, please install it")
        sys.exit(1)
