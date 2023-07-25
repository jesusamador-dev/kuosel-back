from fastapi import APIRouter
from fastapi import Depends
from app.domain.services.category_service import CategoryService
from app.schemas.category_schema import Category

router = APIRouter()


@router.get("/categories")
def get_categories(service: CategoryService = Depends()) -> list[Category]:
    return service.get_all()
