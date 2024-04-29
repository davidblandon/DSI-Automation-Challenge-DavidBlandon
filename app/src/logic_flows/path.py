#The following code adds the module 'opening_programs' and 'tesseract' to the path
#DISCLAIMER: THIS PATH IS USED TO FEED THE IMPORTED MODULES THAT ARE NOT IN THE CURRENT DIRECTORY

import sys
import os

def add_path():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'opening_programs')))
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Utils')))