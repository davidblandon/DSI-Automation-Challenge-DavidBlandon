#The following code adds the module 'opening_programs' and 'Utils' to the path

import sys
import os

def add_path():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'opening_programs')))
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Utils')))