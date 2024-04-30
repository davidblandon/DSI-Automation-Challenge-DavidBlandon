# API Documentation

This module contains all the information of the api. It is located in "main.py"

## Configuration

These are the following steps to start using the api, the example is being runned on localhost:

1. Run the file "main.py", remember to be located in the root DSI-Automation-Challenge-DavidBlandon/
2. Send a post request to http://localhost:8000/token with this body
```
{
  "name": "admin_dsi"
}
```
Enter the exact same body in raw format, JSON and you will get an answer like this one:
```
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImFkbWluX2RzaSIsImV4cCI6MTcxNDQ5NzQ2N30.9Du_M-2ZGi5_UqLEVwckjav4HkprdfmaqrpkxwZs36Q"

```
3. Now everytime you send a request to the api you must add a header called "Authorization" with the content "Bearer {your_token}" without the brackets. Like this:
![image](https://github.com/davidblandon/DSI-Automation-Challenge-DavidBlandon/assets/103081222/76a47e5b-9ac6-4207-908b-b992ecaad585)

## Use of API endpoints

Now we will explain each endpoint

- @app.post("/execute_command"): Endpoint to send pyautogui commands and execute it in the pc locally. You must enter the following body:
```
{
  "action": "string",
  "args": [
    "string"
  ]
}
```
Where you must replace the string of action for the action would like to do and args with a list of the arguments you want to pass. Example:
```
{
  "action": "press",
  "args": [
    "win"
  ]
}
```
The last example press the boton win in the computer

- @app.post("/open/{program}"): Opens the given program, example:
```
http://127.0.0.1:8000/open/word
```
Opens a word program

- @app.post("/extract"): Extract the text in a given image in a given position:
```
{
  "name": "string",
  "url": "string",
  "initial_pos": [
    "string"
  ],
  "length": [
    "string"
  ]
}
```
Where "name" is the name of the image, could be any. "url" is the url where the image is located. "initial_pos" is a list where the first value is the x coordinate and the second value is
is the y coordinate where your text section begins. and "length" where the first value is the length in x and the second value is is the length in y coordinate that your text section has. 
This two lists creates a kind of "box" that will contain your text.
```
{
  "name": "my_image",
  "url": "chrome/my_image.png",
  "initial_pos": [142, 354],
  "length": [75,35]
}
```

- @app.post("/write_invoices_word"): Creates multiples word with the "bill_word_template.txt" with the information provided and saves them in a local folder. Check the documentation of this flow for more information
```
{
  "users_total": {}
}
```
Example:
```
{
  "users_total": {"David":123, "Juan":489}
}
```

- @app.post("/write_email_outlook"): Writes an email in outlook with the info provided:
```
{
  "dest": "string",
  "subject": "string",
  "message": "string"
}
```
Example:
```
{
  "dest": "dablandonr@eafit.edu.co",
  "subject": "Proof",
  "message": "Hello, this is a proof"
}
```

- @app.post("/fill_microsoft_form"): Fills a microsoft forms with the info provided:
```
{
  "url": "string",
  "responses": [
    "string"
  ]
}
```
Example:
```
{
  "url": "my_form_url.com",
  "responses": ["Answer 1", "Answer 2", "etc"]
}
```

- @app.post("/instagram_followers/{user}"): Returns the followers of the instagram user provided. Example:
```
http://127.0.0.1:8000/instagram_users/monlaferte
```

- @app.post("/total_check_email"): Implements a logic to check if in a provided image, the text in a section provided is superior than a limit established, if it is the case send an email.
  **It is important to send the limit as a parameter, Example of it**
```
http://127.0.0.1:8000/total_check_image?limit=9000
```
Body template:
```
{
  "image_info": {
    "name": "string",
    "url": "string",
    "initial_pos": [
      "string"
    ],
    "length": [
      "string"
    ]
  },
  "email_info": {
    "dest": "string",
    "subject": "string",
    "message": "string"
  }
}
```
Example:
```
{
  "image_info": {
    "name": "my_image",
    "url": "chrome/my_image.png",
    "initial_pos": [456, 784],
    "length": [75, 35]
  },
  "email_info": {
    "dest": "dablandonr@eafit.edu.co",
    "subject": "Limit reached",
    "message": "The limit has been reached in the image selected"
  }
}
```

You can check the full documentation in [http://localhost:8000/docs](http://localhost:8000/docs) or in [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)
