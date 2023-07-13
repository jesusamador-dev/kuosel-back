from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schema import CategoryCreate, CategoryUpdate, Category
from ..controllers.categories import CategoriesController
from ..dependencies import get_db

router = APIRouter()

controller = CategoriesController()

@router.post("/categories", response_model=Category)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return controller.create_category(db, category)


@router.get("/categories/{category_id}", response_model=Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return controller.get_category(db, category_id)


@router.put("/categories/{category_id}", response_model=Category)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    return controller.update_category(db, category_id, category)


@router.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    controller.delete_category(db, category_id)
