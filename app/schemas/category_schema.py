from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    type: str
    icon: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True
