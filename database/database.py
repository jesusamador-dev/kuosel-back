import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

db_host = os.environ.get('HOST')
db_port = 3306
db_user = os.environ.get('DATABASE_USER')
db_password = os.environ.get('DATABASE_PASSWORD')
db_name = os.environ.get('DATABASE_NAME')

# Configura la URL de conexión a la base de datos
db_url = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Crea el motor de SQLAlchemy con el pool de conexiones
engine = create_engine(db_url, poolclass=QueuePool, pool_size=10, max_overflow=20)

# Crea una fábrica de sesiones
Session = sessionmaker(bind=engine)