# Utiliza una imagen oficial de Python como imagen base
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

# Establece el directorio de trabajo en el contenedor como /app
WORKDIR /app

# Copia el contenido del directorio kuosel-back en la máquina local al directorio /app en el contenedor
COPY ./kuosel-back /app
