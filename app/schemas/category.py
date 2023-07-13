from pydantic import BaseModel
from datetime import datetime


class CategoryBase(BaseModel):
    name: str
    description: str


class CategoryCreate(CategoryBase):
    created_at: datetime


class CategoryUpdate(CategoryBase):
    updated_at: datetime


class Category(CategoryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
