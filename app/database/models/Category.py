from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255))
    description = Column('description', String(255))
    created_at = Column('created_at', DateTime, default=func.now())
    updated_at = Column('updated_at', DateTime, default=func.now(), onupdate=func.now())