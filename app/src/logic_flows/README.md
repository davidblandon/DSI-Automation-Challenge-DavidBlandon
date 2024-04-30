# Logic Flows

This module contains two logic flows. Based on the extracted text, the app will take a decision and continue with other flow or just stops. Here are the explanation of each flow:

- Aprove invoice or send email: the file "approve_total_invoice.py" contains the function "approve(invoice_name:str, financial_email:str):" that searchs in the invoice entered the total
and if it's superior than 10000 will automatically send an email to the email provided. You can change the limit of 10000 for any you would like
- Check if the invoice is defeated: the file "check_due_invoice.py" contains the function "due_date(invoice_name:str, form_url:str):" which checks if the date in the invoice already passed,
if it is the case, it will send a form with the information of the invoice to the given forml url. **In this case the information that will be send are "bank_name,bank_account,invoice_no" of the selected
invoice, please make sure that your form has the correct number of questions**

**IMPORTANT: The invoices are located in app\src\navegation_flows\invoices_image. Also this two flows works only with the kind of invoice I'm handling regarding the location of the text, if you 
want to create your own logic flow, you can use the api with the endpoint @app.post("/total_check_email")**
