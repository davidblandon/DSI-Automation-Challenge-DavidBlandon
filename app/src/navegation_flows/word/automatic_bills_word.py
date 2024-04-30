# The following code contains a code to save multiple words given a dict with users and total of the invoice

from new_blank_word import start_word
import pyautogui,time, os

def start_bills(users_total:dict):
    start_word()
    file_path = "app/src/navegation_flows/word/bills_template_word.txt" 
    with open(file_path, "r") as file:
        text_content = file.read()
    for user,total in users_total.items():
        text_content_modified = text_content.replace('[user]', str(user))
        text_content_modified = text_content_modified.replace('[total]', str(total))
        pyautogui.write(text_content_modified)
        time.sleep(1)
        pyautogui.press('f12')
        time.sleep(1)
        pyautogui.write("Invoice user " + str(user))
        time.sleep(1)
        save_path = os.path.join(os.path.dirname(__file__), 'words_generated')
        res = pyautogui.locateOnScreen(f"app/src/opening_programs/identifiers/windows_explorer.png", confidence=0.5)
        pyautogui.moveTo(res)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.write(save_path)
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.moveRel(100, 650)
        time.sleep(1)
        pyautogui.click()
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.hotkey("ctrl", "e")
        pyautogui.press("backspace")
        pyautogui.press("backspace")
        pyautogui.press("backspace")
        time.sleep(1)


        