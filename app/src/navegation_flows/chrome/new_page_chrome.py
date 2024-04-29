#The following code opens a new page in chrome

from base import start_flow

import pyautogui,time

def start_chrome(url:str):
    start_flow("google chrome")
    time.sleep(2)
    pyautogui.hotkey('win', 'up')
    time.sleep(0.5)
    pyautogui.write(url)
    time.sleep(2)
    pyautogui.press("enter")
