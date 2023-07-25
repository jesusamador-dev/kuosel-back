from fastapi import APIRouter
from app.domain.services.category_service import CategoryService
from app.schemas.category_schema import Category

router = APIRouter()

service = CategoryService()


@router.get("/categories", response_model=list[Category])
async def get_categories():
    return service.get_all()
