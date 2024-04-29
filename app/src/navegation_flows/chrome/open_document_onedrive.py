#The following code opens a file in OneDrive

from new_page_chrome import start_chrome
from image_check import check_screen
import pyautogui,time

def open(document_name:str):
    start_chrome("https://onedrive.live.com/")
    time.sleep(5)
    pyautogui.moveTo(893, 165)
    time.sleep(1)
    pyautogui.click()
    pyautogui.write(document_name)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(3)
    check_screen("file_onedrive.png")

    pos = pyautogui.locateCenterOnScreen(f"app/src/opening_programs/identifiers/file_onedrive.png", confidence=0.7)
    pyautogui.moveTo(pos)
    pyautogui.moveRel(0, 50)
    pyautogui.tripleClick()

open("Derecho")