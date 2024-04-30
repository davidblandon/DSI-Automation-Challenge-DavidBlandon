# Navegation Flows

This module contains the logic of differents flows through some applications. In this case, we have flows for three diferents programs:

1. Word
2. Chrome
3. Invoices Images

Now we will explain each flow of each program

## 1. Word

We have two simple flows:

- Open a blank word; To use it you have to run the file "new_blank_word.py" but previously you have to add the call of the function start_word() at the end of the file
- Automatic bills; It intends to simulate the creation of differents bills and saving them in a directory. Each time it creates a bill it modifies the context of "bills_template_word.txt" with
the information of the customer, this information is given in the parameters of the function as a python dict. Here is an example
```
start_bills({"David":123213, "Marie": 546456})
```
In this case we add the call of the function with a dict parameter, where the key is the name of the customer and the value is the total of the bill. 
The files will be saved in app\src\navegation_flows\word\words_generated
**NOTE: If you are having issues saving each word document, try to drag your file's browser to merge with the RPA movement to the "Save" button** 

## 2. Chrome

We find differents flows:

- Open a selected chrome page with "new_page_chrome.py" file, by simple adding the call of the function at the end of the document. Like this
```
start_chrome("www.facebook.com")
```
- Instagram commands; In the file "commands_instagram.py" you will find two functions "follow(instagram_user)" that just follows on instagram the user you enter and "capture_followers(instagram_user)"
that returns the followers of a given user. This last one uses the tesseract to extract the text in the screen
- Open a document in one drive; "open_document_onedrive.py" has the function "open(document_name:str)" where by giving the parameter of the document name you can open that document. Make sure you
write the correct name. 
- Fill a microsoft forms; the file "fill_microsoft_forms.py" containts the function "fill(form_url:str, responses:list)" where you can automatically fill the form in the given url with the respones you
entered. Make sure you enter the correct numbers of answers, otherwise will not work. Example of respones:
```
respones = ["Answer 1", "Answer 2, "etc"]
```
In this case the flow will try to answer three questions and send it

## 3. Invoices image

This applies tesseract to extract text from a given image. In this case I provided some invoices examples located in the folder's module to do the process. **This flows only will work with my invoices
images due it's selecting the text of a given (x,y) where I know it's located the information of the invoice, if you want to upload your own image and extract the text where you want, I recommend using the
api, exactly the endpoint @app.post("/extract")**

- Total of invoice; captures the total of the invoice selected, in "extract_total.py" you will see "total(file_name:str)" You have to call the function giving the name of the invoice with the termination of .png
(The image should be located in the same root that the python file)
- Date of the invoice; same logic that the previous one, "extract_date.py" with the function "date(file_name:str)"
- Customer info of invoice; same logic that the previous one, "extract_customer_info.py" with the function "info(file_name:str)"
