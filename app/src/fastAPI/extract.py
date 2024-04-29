#The following code contains the logic to extract text from a section in an uploaded image

import requests, os, time, subprocess, pyautogui
from base_api import image_convert_str

def save_image(image_url,name):

    image_file = f"app/src/fastAPI/downloaded_photos/{name}.png"
    response = requests.get(image_url)

    # Guarda la imagen en un archivo
    with open(image_file, "wb") as f:
        f.write(response.content)

    print("Imagen descargada con éxito:", image_file)

def to_text(name:str, initial_position:list, lenght:list):

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "downloaded_photos", name + ".png"))
    subprocess.Popen(['explorer', path])
    time.sleep(1)
    pyautogui.hotkey("win", "up")
    time.sleep(1)


    route_image = f"app/src/fastAPI/downloaded_photos/{name}_text.png"
    screenshot = pyautogui.screenshot(region=(initial_position[0], initial_position[1], lenght[0], lenght[1]))
    screenshot.save(route_image)
    string = image_convert_str(route_image)
    return string.strip()

