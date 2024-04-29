#The following code check if the date of the invoice has passed, if the case fills out a form
#Otherwise prompt it is correct

from base_logic import invoice_date, invoice_info, fill_form
from datetime import datetime
import pyautogui

def due_date(invoice_name:str, form_url:str):
    date = invoice_date(invoice_name)
    print(date)
    format = "%d %B, %Y" 
    date = datetime.strptime(date, format).date()
    actual_date = datetime.now().date()

    if date < actual_date:
        responses = list(invoice_info(invoice_name))
        fill_form(form_url, responses)
    else:
        pyautogui.alert("The invoice is on date to be payed")
    
due_date("Invoice3.png", "https://forms.office.com/r/hXc10CxTBC?origin=lprLink")