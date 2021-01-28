from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/db", StaticFiles(directory="db"), name="db")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/three_js/", response_class=HTMLResponse)
async def three_js(request: Request):
    path = "./db/01_01.bvh"
    return templates.TemplateResponse(
        "index.html", {"request": request,
                        "bvh_motion_path": path}
    )