from fastapi import FastAPI
from routers import categories, movements

app = FastAPI()

app.include_router(categories.router)
app.include_router(movements.router)
