# main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="root")

@app.get("/", response_class=HTMLResponse)
async def reed_root(request: Request):
    return templates.TemplateResponse(
        "main_page.html", 
        {"request": request}
        ) # {"message": "Hello World! My first fastApi code!"}

@app.get("/first_main_page")
async def first_page():
    return {"message": "first"}

@app.get("/second_main_page")
async def second_page():
    return {"message": "second"}