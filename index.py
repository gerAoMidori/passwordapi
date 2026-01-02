from passwordManager import PassWordManager
from typing import Optional
from fastapi import FastAPI, Request, Query

from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates("templates")

@app.get("/")
def home():
    return "Welcome"