
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Hello from Lumalor backend"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/view", response_class=HTMLResponse)
def render_view(request: Request):
    # Simple Jinja example to render a template
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello from Jinja"})
