#The following code adds the base for any flow in the project, starts the given program
#DISCLAIMER: THIS BASE IS USED TO FEED THE IMPORTED MODULES THAT ARE NOT IN THE CURRENT DIRECTORY

from path import add_path
add_path()
import open_program, tesseract.image_to_string

def start_flow(program:str):
    open_program.open_program(program)

def image_convert_str(route:str):
    return tesseract.image_to_string.convert(route)