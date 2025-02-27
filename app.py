from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates") 
# Home route
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})
# Set up template rendering
templates = Jinja2Templates(directory="templates")

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")



# Sign-in route
@app.get("/signin")
async def signin(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})

# Home route (another instance for when clicking "Go to Home")
@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Dashboard route
@app.get("/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# Projects route
@app.get("/projects")
async def projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

# Payments route
@app.get("/payments")
async def payments(request: Request):
    return templates.TemplateResponse("payments.html", {"request": request})

# Analytics route
@app.get("/analytics")
async def analytics(request: Request):
    return templates.TemplateResponse("analytics.html", {"request": request})

# Settings route
@app.get("/settings")
async def settings(request: Request):
    return templates.TemplateResponse("settings.html", {"request": request})

# About route
@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# Contact route
@app.get("/contact")
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

# Logout route
@app.get("/logout")
async def logout():
    # Add your logout logic here, e.g., clear the session, etc.
    # For now, we will simply redirect to the signin page.
    return RedirectResponse(url="/signin")

# Goal Models
class GoalCreate(BaseModel):
    name: str
    amount: float

class GoalResponse(BaseModel):
    id: int
    name: str
    amount: float

# In-memory storage for goals
goals_db = []

# Goals API
@app.get("/goals", response_model=List[GoalResponse])
async def get_goals():
    return goals_db

@app.post("/goals", response_model=GoalResponse)
async def create_goal(goal: GoalCreate):
    goal_id = len(goals_db) + 1
    new_goal = {"id": goal_id, "name": goal.name, "amount": goal.amount}
    goals_db.append(new_goal)
    return new_goal

@app.get("/goals/{goal_id}", response_model=GoalResponse)
async def get_goal(goal_id: int):
    for goal in goals_db:
        if goal["id"] == goal_id:
            return goal
    raise HTTPException(status_code=404, detail="Goal not found")

@app.put("/goals/{goal_id}", response_model=GoalResponse)
async def update_goal(goal_id: int, goal: GoalCreate):
    for g in goals_db:
        if g["id"] == goal_id:
            g["name"] = goal.name
            g["amount"] = goal.amount
            return g
    raise HTTPException(status_code=404, detail="Goal not found")

@app.delete("/goals/{goal_id}")
async def delete_goal(goal_id: int):
    global goals_db
    goals_db = [g for g in goals_db if g["id"] != goal_id]
    return {"message": "Goal deleted successfully"}

# Read the custom 404 HTML file
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)