from pydantic import BaseModel
from datetime import datetime


class MovementBase(BaseModel):
    name: str
    amount: float
    category_id: int


class MovementCreate(MovementBase):
    created_at: datetime


class MovementUpdate(MovementBase):
    updated_at: datetime


class Movement(MovementBase):
    id: int
    user_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
