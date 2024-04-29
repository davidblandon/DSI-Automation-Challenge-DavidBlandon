#The following code is the base for any flow in the project, starts the given program
#Defines the use of the Util tesseract image to string

from path import add_path
add_path()
import open_program, tesseract.image_to_string

def start_flow(program:str):
    open_program.open_program(program)

def image_convert_str(route:str):
    return tesseract.image_to_string.convert(route)