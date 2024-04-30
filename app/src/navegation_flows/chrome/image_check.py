#The following code check if the image that pyautogui is trying to search is located on the screen
import pyautogui,sys

def check_screen(identifier:str):
    pyautogui.useImageNotFoundException()
    try:
        location = pyautogui.locateOnScreen(f"app\src\opening_programs\identifiers\{identifier}", confidence=0.5)
        print('Program found')
    except pyautogui.ImageNotFoundException:
        pyautogui.alert(f"The {identifier} image has not been found, check if the programs or the pages are loading properly\n For more information check the documentation")
        sys.exit(1)