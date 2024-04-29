#The following code adds the base for getting any existent flow

from path_logic import add_path
add_path()
from invoices_image.extract_total import total
from invoices_image.extract_customer_info import info
from invoices_image.extract_date import date
from chrome.write_email_outlook import write
from chrome.fill_microsoft_forms import fill

def invoice_total(file_name:str):
    return total(file_name)

def invoice_info(file_name:str):
    return info(file_name)

def invoice_date(file_name:str):
    return date(file_name)

def write_email(email_dest:str, subject:str, message:str):
    return write(email_dest, subject, message)

def fill_form(form_url:str, responses:list):
    return fill(form_url, responses)