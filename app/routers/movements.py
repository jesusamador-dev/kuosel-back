from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


# Definición del modelo de movimiento
class Movement(BaseModel):
    id: int
    name: str
    amount: float
    category_id: int


# Base de datos simulada para almacenar los datos
db = {}


# Ruta para obtener todos los movimientos
@router.get("/movements")
def get_movements():
    return db.values()


# Ruta para obtener un movimiento por ID
@router.get("/movements/{movement_id}")
def get_movement(movement_id: int):
    movement = db.get(movement_id)
    if not movement:
        raise HTTPException(status_code=404, detail="Movement not found")
    return movement


# Ruta para crear un movimiento
@router.post("/movements")
def create_movement(movement: Movement):
    db[movement.id] = movement
    return movement


# Ruta para actualizar un movimiento por ID
@router.put("/movements/{movement_id}")
def update_movement(movement_id: int, movement: Movement):
    if movement_id not in db:
        raise HTTPException(status_code=404, detail="Movement not found")
    db[movement_id] = movement
    return movement


# Ruta para eliminar un movimiento por ID
@router.delete("/movements/{movement_id}")
def delete_movement(movement_id: int):
    if movement_id not in db:
        raise HTTPException(status_code=404, detail="Movement not found")
    del db[movement_id]
    return {"message": "Movement deleted"}
