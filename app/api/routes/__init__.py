from fastapi import APIRouter
from app.api.routes.categories import router as categories_router

router = APIRouter()

router.include_router(categories_router, tags=["categories"])
