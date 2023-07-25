from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.data_base import get_db
from app.schemas.category_schema import Category


class CategoryRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_all(self):
        return self.db.query(Category).all()
