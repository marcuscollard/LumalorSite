from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


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
