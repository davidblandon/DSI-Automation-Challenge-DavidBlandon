#The following code writes an email in outlook

from new_page_chrome import start_chrome
from image_check import check_screen
import pyautogui,time

def write(email_dest:str, subject:str, message:str):
    start_chrome("https://outlook.live.com/mail")
    time.sleep(4)
    pyautogui.moveTo(1800, 500)
    time.sleep(0.5)
    pyautogui.scroll(500)
    time.sleep(0.5)
    pyautogui.moveTo(191, 290)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(2)

    user, domain = email_dest.split('@') 
    pyautogui.write(user)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'alt', 'q')
    time.sleep(0.5)
    pyautogui.write(domain)
    time.sleep(1)
    pyautogui.moveTo(1200, 529)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write(subject)
    time.sleep(0.5)
    pyautogui.moveRel(0, 100)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write(message)
    time.sleep(0.5)
    pyautogui.moveTo(536, 367)
    time.sleep(0.5)
    pyautogui.click()
