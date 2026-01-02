from passwordManager import PassWordManager
from typing import Optional
from fastapi import FastAPI, Request, Query

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates("templates")


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)

def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "FastAPI"}
    )

@app.get("/check/{password}")
async def check(password : str):
    return {password : PassWordManager().check_strength(password=password)}


@app.get("/create/")
async def create(request: Request,
                 length: Optional[int] = None,
                 upper: Optional[bool] = Query(None),
                 digits: Optional[bool] = Query(None),
                 special: Optional[bool] = Query(None)):
    number_of_types = 1
    length = length if length is not None else 12
    if length < 2:
        return {"messsage" : "Length too short"} 
    #Upper 
    upper = upper if upper is not None else False
    #Digits
    digits = digits if digits is not None else False
    #Special
    special = special if special is not None else False
    print(upper, digits, special)
    number_of_types = sum([1, upper, digits, special])
    password = PassWordManager().create(length, number_of_types, upper, digits, special )
    return {"password" : password }