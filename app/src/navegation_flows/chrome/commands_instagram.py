#The following code provides two commands in instagram web, follow an account and extract the followers of an account

from new_page_chrome import start_chrome
from image_check import check_screen
from base import image_convert_str
import pyautogui,time

def follow(instagram_user):
    if instagram_user == "":
        instagram_user = pyautogui.prompt('Enter the user name of the account you want to follow')
    start_chrome("https://www.instagram.com/" + instagram_user + "/")
    time.sleep(4)

    check_screen("instagram_follow.png")
    pos = pyautogui.locateCenterOnScreen(f"app/src/opening_programs/identifiers/instagram_follow.png", confidence=0.7)
    pyautogui.moveTo(pos)
    pyautogui.click()

def capture_followers(instagram_user):
    if instagram_user == "":
        instagram_user = pyautogui.prompt('Enter the user name of the account you want to capture the followers')
    start_chrome("https://www.instagram.com/" + instagram_user + "/")
    time.sleep(4)

    x,y = 1067, 281
    width, height = 75, 35

    route_image = f"app/src/navegation_flows/chrome/instagram_followrs_screenshots/{instagram_user}" + ".png"
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(route_image)
    time.sleep(2)
    followers_string =  image_convert_str(route_image).strip()
    return followers_string

print(capture_followers(""))

