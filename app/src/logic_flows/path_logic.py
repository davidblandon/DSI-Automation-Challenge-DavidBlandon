#The following code adds the module 'opening_programs' and 'tesseract' to the path

import sys
import os

def add_path():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'navegation_flows')))
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'opening_programs')))
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'navegation_flows', 'chrome')))
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Utils')))