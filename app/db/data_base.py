import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import QueuePool

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,  # use QueuePool, which is a good choice for multi-threaded applications
    pool_size=10,  # this is the number of connections to keep open
    max_overflow=20,  # this is how many additional connections to open when all others are in use
    pool_recycle=3600,  # number of seconds to wait before a connection is automatically recycled
)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
