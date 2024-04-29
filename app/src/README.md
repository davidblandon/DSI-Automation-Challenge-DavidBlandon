# Possible error cases, General information and architecture
## Error cases
The objective of the app is do RPA with python. The project was developed with my computer specs:
- 1920x1080 Screen.
- Windows 10 Pro.
  
Some of the common errors you may encounter could be:

- Different screen size: A different size of the screen can cause the position (x,y) of some commands be different than the original of my computer. This allows the app to click and move to positions with no correct values
- Use of another OS: Every OS has a different GUI, if you are working with other OS the app could have serious problems to reach some predetermined images it has to locate
- Different version of the programs: If you use a different version of word or chrome par example, it can have different location of the buttons the app encounters.
- Not be logged in the plataforms of use: If you are not currently logged in the platforms we required such as: outlook, onedrive or instagram the app will not work

## General information
- To execute any file in the project you must be located in the root of the project DSI-Automation-Challenge-DavidBlandon/. If you try to execute any file in other directory
there will be an error of importations. Here is an example
```
py app\src\opening_programs\open_program.py
```
- The files by themselves do not contain anything besides the functions, if you want to check and run a specified function you have to modify the file and add the execution of the function at the end.
For more information check the documentation of each module. Here is an example
```
# The following code has the implementation for opening any program
import pyautogui
import time
from program_installed import installed
from identifiers.check import check_identifier


def open_program(open_app:str):

    if open_app == "":
        open_app = pyautogui.prompt('Enter the FULL NAME of the program you want to open')
        open_app.lower().strip()
    else:
        pass

    check_identifier(open_app)

    # Open the start menu
    pyautogui.press("win")  # Press the windows key
    time.sleep(0.5)

    # Look for the program to open
    pyautogui.write(open_app)
    time.sleep(0.5)

    installed(open_app)

    pyautogui.press("enter")  # Press enter to open the program

```
If you want to run the present code you should add the following line at the end
```
open_program("")
```
- I huge recommend using Visual Studio Code to run the project. This regarding the fact we have to modify each file to run a function and also regarding we have to execute every file in the root directly.

## Architecture

The app is divided by 5 modules:

- opening_programs: This module contains the logic to open any program
- navegation_flows: Contains multiple navegation flows with programs; as write an email, fill a form. This module implements opening_programs module
- logic_flows: Contains flows that has some logic interpretation and takes decisions based on the interpretation; as chech the number of a photo and then write and email or not, based on the number extracted This module implements navegation_flows module
- fastAPI: Contains the information of the API. The API system implements a variety of the last mentioned modules
- Utils: Gives the logic of tesseract extract texts from images. It is used by multiple functions in all the project

For more information check the documentation of each module
