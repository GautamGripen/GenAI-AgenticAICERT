import numbers

from fastapi import FastAPI, HTTPException

from starlette.responses import Response

import uvicorn

from App.apiReadF1JSONFiles import read_drivers1, read_drivers2, read_drivers3, read_teams1, read_teams2, read_teams3, read_teams4, read_teams5

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Fast API in Python, Welcome To The Home Page"}

@app.get("/drivers1")
def read_driver1():
    return read_drivers1(55)


@app.get("/drivers2")
def read_driver2(number:int):
    return read_drivers2(number)

@app.get("/drivers3")
def read_driver3(number:int):
    return read_drivers3(number)


@app.get("/teams1")
def read_team1(world_championships:int):
    return read_teams3(world_championships)


# taking input from the user
if __name__ == '__main__':
    uvicorn.run(app, port=5001)

