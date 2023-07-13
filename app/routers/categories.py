from fastapi import APIRouter
from app.schemas import CategoryCreate, CategoryUpdate, Category
from app.controllers.categories_controller import CategoriesController

router = APIRouter()

controller = CategoriesController()


@router.get("/categories", response_model=list[Category])
def get_categories_all():
    return controller.get_categories_all()


@router.post("/categories", response_model=Category)
def create_category(category: CategoryCreate):
    return controller.create_category(category)


@router.get("/categories/{category_id}", response_model=Category)
def get_category(category_id: int):
    return controller.get_category(category_id)


@router.put("/categories/{category_id}", response_model=Category)
def update_category(category_id: int, category: CategoryUpdate):
    return controller.update_category(category_id, category)


@router.delete("/categories/{category_id}")
def delete_category(category_id: int):
    controller.delete_category(category_id)
