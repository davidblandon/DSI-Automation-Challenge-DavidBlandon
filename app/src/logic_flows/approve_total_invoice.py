#The following code checks if the invoice total is bigger than $1000 if it is the case writes an email
#Otherwise sends a prompt with approvation

from base_logic import invoice_total, invoice_info, write_email
import pyautogui

def approve(invoice_name:str, financial_email:str):
    total = invoice_total(invoice_name)
    if total >= 10000:
        bank_name,bank_account,invoice_no = invoice_info(invoice_name)
        message = f"The invoice with the following content:\n Bank Name: {bank_name}\n Bank Account: {bank_account}\n Invoice #: {invoice_no}\n Total: {total}\n Needs to be verified by you in order to be approved." 
        write_email(financial_email, f"{invoice_no} Approbation", message)
    else:
        pyautogui.alert("The invoice is now approved")

