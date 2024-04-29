# The following code opens a blank word to be modified

from base import start_flow

import pyautogui,time

def start_word():
    start_flow("word")
    time.sleep(2)
    pyautogui.hotkey('win', 'up')
    time.sleep(0.5)
    pyautogui.moveTo(393, 300, duration=0.5)  # Mover con duración de 1 segundo
    pyautogui.click() 
