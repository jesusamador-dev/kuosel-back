from fastapi import APIRouter
from app.domain.services.category_service import CategoryService

router = APIRouter()


@router.get("/categories")
async def get_categories(service: CategoryService):
    return await service.get_all()
