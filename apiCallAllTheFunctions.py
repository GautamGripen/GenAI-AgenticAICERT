#This will call any function from rest of the code files
#so simply import the function. for example the "users" functions, just write "app.api.api import <function>"

from fastapi import FastAPI, HTTPException

from starlette.responses import  Response
import uvicorn
from App.apiReadJSONFiles import read_user, read_questions     #App.api says the root folder is App and file to call functions from is "apiReadJSONFiles"

app = FastAPI()

@app.get("/")
def root():
    return {"massage": "Fast API in Python"}

@app.get("/users")        #calling the "users" function
def read_users():
    return read_user()

@app.post('/questions') #calling the "questions" function
def get_quest(que_id:int):
    return read_questions(que_id)




if __name__ == "__main__":
    uvicorn.run(app, port=5002)