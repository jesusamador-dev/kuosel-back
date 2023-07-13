from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas import Category, CategoryUpdate, CategoryCreate
from app.database.repositories import CategoryRepository
from app.dependencies import container


class CategoriesController:
    def __init__(self, db: Session = container.session.provided):
        self.db = db
        self.repository = CategoryRepository(self.db)

    def get_categories_all(self) -> List[Category]:
        return self.repository.get_categories_all()

    def create_category(self, category: CategoryCreate) -> Category:
        return self.repository.create_category(category=category)

    def get_category(self, category_id: int) -> Category:
        category = self.repository.get_category(category_id=category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

    def update_category(
        self, category_id: int, category: CategoryUpdate
    ) -> Category:
        updated_category = self.repository.update_category(
            category_id=category_id, category=category
        )
        if not updated_category:
            raise HTTPException(status_code=404, detail="Category not found")
        return updated_category

    def delete_category(self, category_id: int) -> None:
        success = self.repository.delete_category(category_id=category_id)
        if not success:
            raise HTTPException(status_code=404, detail="Category not found")