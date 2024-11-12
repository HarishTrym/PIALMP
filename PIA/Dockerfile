# Usa una imagen base que tenga Python y la última versión de Alpine o Debian
FROM python:3.9-slim

# Instala dependencias del sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expone el puerto en el que la app correrá
EXPOSE 5000

# Copia el código de la aplicación Flask al contenedor
COPY . /app

# Define el directorio de trabajo
WORKDIR /app

# Comando para ejecutar la aplicación
CMD ["python", "App.py"]