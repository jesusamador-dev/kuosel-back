from fastapi import Depends
from app.infra.repositories.category_repository import CategoryRepository


class CategoryService:
    def __init__(self, category_repo: CategoryRepository = Depends(CategoryRepository)):
        self.category_repo = category_repo

    def get_all(self):
        return self.category_repo.get_all()

