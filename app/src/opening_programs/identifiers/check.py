# The following code checks if the identifier of the program exists
import sys, pyautogui, os

def check(program):
    image_path = f"app/src/opening_programs/identifiers/{program}.png"
    if os.path.exists(image_path):
        return image_path
    else:
        print(image_path)
        pyautogui.alert("The identifier was not found, please create one\n Check the documentation of identifiers for more information")
        raise Exception("The identifier was not found, please create one\n Check the documentation of identifiers for more information")
    
def check_identifier(program):
    try:
        # Comprobar el identificador
        check(program)
    except Exception as e:
        # Imprimir el mensaje de error y salir del script
        print(f"Error: {e}")
        sys.exit(1)  # Salir con código de error