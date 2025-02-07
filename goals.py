# goals.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Goal(BaseModel):
    id: int
    description: str
    target_amount: float
    amount_saved: float = 0

# In-memory storage for demonstration purposes
goals: List[Goal] = []

@router.get("/", response_model=List[Goal])
def get_goals():
    return goals

@router.post("/", response_model=Goal)
def create_goal(goal: Goal):
    if any(g.id == goal.id for g in goals):
        raise HTTPException(status_code=400, detail="Goal with that id already exists.")
    goals.append(goal)
    return goal

@router.put("/{goal_id}", response_model=Goal)
def update_goal(goal_id: int, amount: float):
    for g in goals:
        if g.id == goal_id:
            g.amount_saved += amount
            return g
    raise HTTPException(status_code=404, detail="Goal not found.")

@router.delete("/{goal_id}", response_model=dict)
def delete_goal(goal_id: int):
    global goals
    new_goals = [g for g in goals if g.id != goal_id]
    if len(new_goals) == len(goals):
        raise HTTPException(status_code=404, detail="Goal not found.")
    goals = new_goals
    return {"message": "Goal deleted"}
