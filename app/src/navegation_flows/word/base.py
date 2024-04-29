#The following code is the base for any flow in the project, starts the given program

from path import add_path
add_path()
import open_program

def start_flow(program:str):
    open_program.open_program(program)