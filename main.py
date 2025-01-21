from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Get the base directory of your application
BASE_DIR = Path(__file__).resolve().parent

# Initialize templates with absolute path
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
