# schemas.py
from pydantic import BaseModel
from typing import Optional

class GoalBase(BaseModel):
    description: str
    target_amount: float
    amount_saved: float = 0

class GoalCreate(GoalBase):
    pass  # Used for creating new goals

class GoalResponse(GoalBase):
    id: int  # Include the ID in responses

    class Config:
        orm_mode = True  # This tells Pydantic to convert SQLAlchemy models into dicts
