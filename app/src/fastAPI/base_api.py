#The following code adds the functions of other modules that are required for the API

from path_api import add_path
add_path()
import open_program, tesseract.image_to_string, automatic_bills_word, write_email_outlook, fill_microsoft_forms, commands_instagram

def start_flow(program:str):
    open_program.open_program(program)

def image_convert_str(route:str):
    return tesseract.image_to_string.convert(route)

def automatic_bills(users_total:dict):
    automatic_bills_word.start_bills(users_total)

def write_email(email_dest:str, subject:str, message:str):
    write_email_outlook.write(email_dest, subject, message)

def fill_form(url:str, responses:list):
    fill_microsoft_forms.fill(url, responses)

def get_followers(user:str):
    return commands_instagram.capture_followers(user)