from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Set up template rendering
templates = Jinja2Templates(directory="templates")

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("/home.html", {"request": request})

@app.get("/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/projects")
async def projects(request: Request):
    return templates.TemplateResponse("/projects.html", {"request": request})

@app.get("/payments")
async def payments(request: Request):
    return templates.TemplateResponse("/payments.html", {"request": request})

@app.get("/analytics")
async def analytics(request: Request):
    return templates.TemplateResponse("/analytics.html", {"request": request})

@app.get("/settings")
async def settings(request: Request):
    return templates.TemplateResponse("/settings.html", {"request": request})

@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse("/about.html", {"request": request})

@app.get("/contact")
async def contact(request: Request):
    return templates.TemplateResponse("/contact.html", {"request": request})
