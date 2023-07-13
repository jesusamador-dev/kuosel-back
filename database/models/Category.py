from sqlalchemy import Table, Column, Integer, String, DateTime, func

# Define la tabla existente
categories_table = Table(
    'categories',
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('description', String(255)),
    Column('created_at', DateTime, default=func.now()),
    Column('updated_at', DateTime, default=func.now(), onupdate=func.now())
)

# Define la clase de modelo
class Category:
    def __init__(self, id, name, description, created_at, updated_at):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at