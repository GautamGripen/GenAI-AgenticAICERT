#This will call any function from rest of the code files
#so simply import the function. for example the "users" functions, just write "app.api.api import <function>"

from fastapi import FastAPI, HTTPException

from starlette.responses import  Response      #In Starlette, starlette.responses provides a set of classes for returning different types of HTTP responses. These classes handle the formatting and structure of the response, making it easier to send data back to the client.
import uvicorn
from App.apiReadJSONFiles import read_user, read_questions     #App.api says the root folder is App and file to call functions from is "apiReadJSONFiles"

app = FastAPI()  # app is just a variable

@app.get("/")   # This will be the Home Page
def root():
    return {"message": "Fast API in Python, Welcome To The Home Page"}

@app.get("/users")        #calling the "users" function. we are using "/" to add it as part of web URL. Like any other website
def read_users():
    return read_user()

@app.post('/questions') #calling the "questions" function. POST because we are taking an input
def get_question(que_id:int):
    return read_questions(que_id)




if __name__ == "__main__":
    uvicorn.run(app, port=5002)