# DSI-Automation-Challenge by David Blandon

This github project contains the solution of the challenge provided by DSI, here are the instructions to run the project.

## Prerequisites

Before installing this project, make sure you have the following:

- **Python**: This project requires Python. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/). We recommend installing version 3.x.
- **pip**: `pip` is the package manager for Python. If you installed Python from python.org, `pip` should be included. You can check if it's installed by running the following command:
  ```bash
  pip --version
- **tesseract**: This project requires tesseract to extract text from images. you can download the installer for windows directly here
[github.com/UB-Mannheim/tesseract/wiki](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe). NOTE: Install the program in the predetermined location to avoid any errors.

## Instalation

Note: Execute all the following commands in a terminal 

1. Clone the github project (This will copy all the files in a new directory where you are located right now)
```
git clone https://github.com/davidblandon/DSI-Automation-Challenge-DavidBlandon.git
```
2. Go to the root of the project
```
 cd DSI-Automation-Challenge-DavidBlandon/
```
3. Create a virtual enviroment
```
 py -m venv venv
```
4. Activate the virtual enviroment. (First for bash or linux. Second for windows)
```bash or linux
source venv/Scripts/activate
```
```windows
venv/Scripts/activate
```
5. Install the requirements
```
pip install -r requirements.txt
```

Now that we have installed the project and its requirements you can check the general information [here](app/src/README.md)

## License

This project is licensed under terms that allow free use for evaluation purposes by DSI (Design Systems Inno). You are permitted to use, copy, and distribute the content in this repository for evaluation and educational purposes.

For additional permissions or to use the content in other ways, please contact the project maintainers

**Important**: This license does not grant permission for commercial use or redistribution for profit. Please refer to the LICENSE file for more details on the terms and conditions.
