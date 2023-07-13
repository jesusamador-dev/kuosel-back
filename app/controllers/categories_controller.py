from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud, deps

class CategoriesController:
    def __init__(self, db: Session = Depends(deps.get_db)):
        self.db = db

    def create_category(self, category: schemas.CategoryCreate) -> schemas.Category:
        return crud.create_category(db=self.db, category=category)

    def get_category(self, category_id: int) -> schemas.Category:
        category = crud.get_category(db=self.db, category_id=category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

    def update_category(
        self, category_id: int, category: schemas.CategoryUpdate
    ) -> schemas.Category:
        updated_category = crud.update_category(
            db=self.db, category_id=category_id, category=category
        )
        if not updated_category:
            raise HTTPException(status_code=404, detail="Category not found")
        return updated_category

    def delete_category(self, category_id: int) -> None:
        success = crud.delete_category(db=self.db, category_id=category_id)
        if not success:
            raise HTTPException(status_code=404, detail="Category not found")