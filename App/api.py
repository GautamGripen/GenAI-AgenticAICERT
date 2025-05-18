from fastapi import FastAPI, HTTPException   ##Importing FastAPI
from starlette.responses import Response
import uvicorn
app = FastAPI()     ##to utilise FastAPI
@app.get("/root")     ##@app.get is used to convert the function as an API. We can use Http methods like Get, POST, etc..
def root():                                ## root is like a home page
    return {"message": "Fast API in python"}

@app.post("/add") ## converting function add into API, we can give any name
def add(a, b):           ## Defining the function
    a = float(a)
    b = float(b)
    c = a + b
    return c

@app.post("/sub")
def sub(a,b):
    c = a-b
    return c


if __name__ == "__main__":           ##Everything should be included within "__main__" for the interpreter to understand
    # print(add(2,4.3))
    # print(sub(b=6, a=7))
    #
    # print("This is the initialization of my AI Journey")

    uvicorn.run(app,port=5001)     ##Using the Fast API

