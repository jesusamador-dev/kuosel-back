# Utiliza una imagen oficial de Python como imagen base
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY /app /main/app

# Instalar las dependencias
RUN pip install --no-cache-dir -r /main/app/requirements.txt

# Expone el puerto en el que se ejecuta la aplicación
EXPOSE 8000

# Establece el comando de inicio para ejecutar la aplicación
CMD ["uvicorn", "main.app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]

LABEL name="kuosel-back"