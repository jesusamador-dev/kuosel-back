from sqlalchemy.orm import Session
from sqlalchemy import exc
from app.schemas import CategoryCreate, CategoryUpdate
from app.database.models import Category


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_category(self, category: CategoryCreate) -> Category:
        db_category = Category(name=category.name, description=category.description)
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def get_category(self, category_id: int) -> Category:
        return self.db.query(Category).filter(Category.id == category_id).first()

    def update_category(self, category_id: int, category: CategoryUpdate) -> Category:
        db_category = self.db.query(Category).filter(Category.id == category_id).first()
        db_category.name = category.name
        db_category.description = category.description
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def delete_category(self, category_id: int) -> bool:
        try:
            category = self.db.query(Category).filter(Category.id == category_id).delete()
            self.db.commit()
            return category > 0
        except exc.SQLAlchemyError:
            self.db.rollback()
            return False
