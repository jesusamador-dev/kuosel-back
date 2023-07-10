# Utiliza una imagen oficial de Python como imagen base
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

# Establece el directorio de trabajo en el contenedor como /app
WORKDIR /app

# Copia el contenido del directorio kuosel-back en la máquina local al directorio /app en el contenedor
COPY /app /app

# Instala las dependencias necesarias
#RUN pip install --no-cache-dir -r /app/requirements.txt

# Expone el puerto en el que se ejecuta la aplicación
EXPOSE 8000

# Establece el comando de inicio para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]