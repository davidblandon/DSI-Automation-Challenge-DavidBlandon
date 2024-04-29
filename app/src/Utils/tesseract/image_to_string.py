#The following code contains the logic to convert an image to a string using tesseract

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def convert(route:str):
    image = Image.open(route)
    return pytesseract.image_to_string(image)