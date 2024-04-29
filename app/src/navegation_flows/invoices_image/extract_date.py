# The following code extracts the date from an invoice IMAGE, check the documentation for more info

from base import image_convert_str
import pyautogui,time, subprocess
import os

def date(file_name:str):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))
    subprocess.Popen(['explorer', path])
    time.sleep(1)
    pyautogui.hotkey("win", "up")
    time.sleep(1)

    x,y = 1100, 384
    width, height = 140, 25

    route_image = f"app/src/navegation_flows/invoices_image/date_images/{file_name}"
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(route_image)
    string = image_convert_str(route_image)
    return string.strip()

 