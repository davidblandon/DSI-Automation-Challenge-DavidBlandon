#The following code contains all the information of the FastAPI, including the api and the endpoints configuration

from fastapi import FastAPI,Depends, Request, HTTPException
from pydantic import BaseModel
from jose import jwt
from datetime import datetime,timedelta
import time
import pyautogui
from base_api import start_flow, automatic_bills, write_email, fill_form, get_followers
from extract import to_text, save_image
import uvicorn

# ----- Classes that works as templates of the information the endpoint should receive -----

class User(BaseModel):
    name:str

class PyAutoGuiCommand(BaseModel):
    action: str
    args: list

class ImageInfo(BaseModel):
    name: str
    url: str
    initial_pos: list
    length: list

class WordInfo(BaseModel):
    users_total: dict

class EmailInfo(BaseModel):
    dest: str
    subject:str
    message:str

class FormInfo(BaseModel):
    url: str
    responses: list

class InstagramFollowers(BaseModel):
    user:str


# ----- API CONFIGURATION -----

app = FastAPI()
secret = "key"

# Endpoint to get a Token, the user should enter "admin_dsi"
@app.post("/token")
def fn(user:User):
    if user.name == "admin_dsi":
        token = jwt.encode({"id":user.name, "exp":datetime.now().utcnow()+timedelta(minutes=15)}, secret)
        return token
    return "Invalid name"

# Function to check if the given token is correct
def check(req:Request):
    try:
        token = req.headers["Authorization"].split(" ")[1]
        jwt.decode(token, secret, algorithms=["HS256"])
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail="An unexpected error occurred: chech the token"
        )
    return True

# Endpoint base that returns ok if the token is correct
@app.get("/")
def fn2(verify:bool=Depends(check)):
    return "OK"


# ----- Endpoints of the project -----

# Endpoint to execute a pyautogui command
@app.post("/execute_command")
async def execute_command(command: PyAutoGuiCommand, verify: bool = Depends(check)):
    try:
        if command.action == "click":
            pyautogui.click(*command.args)
        elif command.action == "press":
            pyautogui.press(command.args[0])
        elif command.action == "position":
            pos = pyautogui.position()
            return pos
        elif command.action == "size":
            size = pyautogui.size()
            return size
        elif command.action == "hotkey":
            pyautogui.hotkey(*command.args)
        elif command.action == "write":
            time.sleep(3)
            pyautogui.write(command.args[0])
        elif command.action == "move":
            pyautogui.moveTo(*command.args)
        elif command.action == "scroll":
            pyautogui.scroll(command.args[0])
        else:
            raise HTTPException(status_code=400, detail="Unsupported command")

        return {"status": "Command executed"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Endpoint to open any program
@app.post("/open/{program}")
async def open(program: str, verify: bool = Depends(check)):
    try:
        print(program)
        start_flow(str(program))
    except Exception:
        raise HTTPException(status_code=400, detail="The program could not be opened")
    return {"status": f"{program} opened"}


# Endpoint to extract text from an image given the section to extract
@app.post("/extract")
async def extract_text(image_info: ImageInfo, verify: bool = Depends(check)):
    try:
        save_image(image_info.url, image_info.name)
        text = to_text(image_info.name, image_info.initial_pos, image_info.length)
    except Exception:
        raise HTTPException(status_code=400, detail="The proccess could not be done")
    return {"The extracted text is: " + text}

# Endpoint to write multiple words with the template and the given users information
@app.post("/write_invoices_word")
async def write_invoices(word_info: WordInfo, verify: bool = Depends(check)):
    try:
        automatic_bills(word_info.users_total)
    except Exception:
        raise HTTPException(status_code=400, detail="The proccess could not be done")
    return {"The words have been created in the local pc"}

# Endpoint to write an email in outlook given the information
@app.post("/write_email_outlook")
async def write_email_outlook(email_info: EmailInfo, verify: bool = Depends(check)):
    try:
        write_email(email_info.dest, email_info.subject, email_info.message)
    except Exception:
        raise HTTPException(status_code=400, detail="The proccess could not be done")
    return {"The email has been sent"}

# Endpoint to fill a microsoft forms given the information
@app.post("/fill_microsoft_form")
async def fill_form_microsoft(form_info: FormInfo, verify: bool = Depends(check)):
    try:
        fill_form(form_info.url, form_info.responses)
    except Exception:
        raise HTTPException(status_code=400, detail="The proccess could not be done")
    return {"The form has been sent"}

# Endpoint to get the instagram followers of an user
@app.post("/instagram_followers/{user}")
async def fill_form_microsoft(user: str, verify: bool = Depends(check)):
    try:
        followers = get_followers(user)
    except Exception:
        raise HTTPException(status_code=400, detail="The proccess could not be done")
    return {f"The user {user} has: {followers} followers" }

# Endpoint to extract a number of an image and if it is superior than the limit, send and email
@app.post("/total_check_email")
async def check_total_email(image_info: ImageInfo, email_info: EmailInfo, limit:int, verify: bool = Depends(check)):
    try:
        save_image(image_info.url, image_info.name)
        text = to_text(image_info.name, image_info.initial_pos, image_info.length)
        if int(text) >= limit:
            write_email(email_info.dest, email_info.subject, email_info.message)
        else:
            pyautogui.alert("The limit has not been reached")
    except Exception:
        raise HTTPException(status_code=400, detail="The proccess could not be done")
    
if(__name__=="__main__"):
    uvicorn.run("main:app")
