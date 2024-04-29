# The following code extracts the customer info from an invoice IMAGE, check the documentation for more info


from base import image_convert_str
import pyautogui,time, subprocess
import os

def info(file_name:str):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))
    subprocess.Popen(['explorer', path])
    time.sleep(1)
    pyautogui.hotkey("win", "up")
    time.sleep(1)
    x,y = 725, 812
    width, height = 225, 45

    route_image = f"app/src/navegation_flows/invoices_image/customer_info_images/{file_name}_customer_info.png"
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(route_image)
    string = image_convert_str(route_image).strip()
    lineas = string.split('\n')
    bank_name = lineas[0].split(':')[1].strip()
    bank_account = lineas[1].split(':')[1].strip()

    x,y = 723, 389
    width, height = 200, 25

    route_image = f"app/src/navegation_flows/invoices_image/customer_info_images/{file_name}_invoice_no.png"
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(route_image)
    string = image_convert_str(route_image)
    invoice_no = string.strip().split(" ")
    invoice_no = invoice_no[3]
    
    return bank_name,bank_account,invoice_no
    
