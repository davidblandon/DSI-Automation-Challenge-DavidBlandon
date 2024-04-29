#The following code fills out a form in microsoft forms

from new_page_chrome import start_chrome
import pyautogui,time

def fill(form_url:str, responses:list):
    start_chrome(form_url)
    time.sleep(5)
    for response in responses:
        pyautogui.write(response)
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
    pyautogui.press("enter")
