CRUD con Docker

Aplicación CRUD (Create, Read, Update, Delete) ejecutada mediante Docker y Docker Compose.

Tecnologías

- Docker

- Docker Compose

- API REST

- Base de datos SQL

Backend: Python

Base de datos: MySQL

Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Docker

- Docker Compose

Puedes comprobar la instalación con:

`docker --version`

`docker compose version`

Configuración

Crea un archivo .env en la raíz del proyecto:

`DB_HOST=db`

`DB_PORT=5432`

`DB_NAME=crud_db`

`DB_USER=admin`

`DB_PASSWORD=admin`

`PORT=3000`

Ajusta las variables de entorno de acuerdo con la tecnología y configuración de tu proyecto.

Ejecutar el proyecto

Para construir las imágenes y levantar los contenedores:

`docker compose up --build`

Para ejecutar los contenedores en segundo plano:

`docker compose up -d --build`


La API estará disponible en:

http://localhost:3000

Detener el proyecto

Para detener los contenedores:

`- docker compose down`


Para detenerlos y eliminar también los volúmenes:

`- docker compose down -v`


El comando -v elimina los datos persistidos de la base de datos.

Endpoints

Ejemplo de endpoints para el CRUD de usuarios:

Método	Endpoint	Descripción

`GET	/api/users`	Obtener todos los usuarios

`GET	/api/users/:id`	Obtener un usuario

`POST	/api/users`	Crear un usuario

`PUT	/api/users/:id`	Actualizar un usuario

`DELETE	/api/users/:id`	Eliminar un usuario

Crear usuario

`POST /api/users`

Content-Type: application/json

volumes:
  mysql_data:

Dockerfile

Ejemplo para una aplicación Node.js:

`FROM node:20-alpine`

`WORKDIR /app`

`COPY package*.json ./`

`RUN npm install`

`COPY . .`

`EXPOSE 3000`

`CMD ["npm", "start"]`

Logs

Para consultar los logs:

`docker compose logs`


Para consultar únicamente los logs de la aplicación:

`docker compose logs app`


Para seguir los logs en tiempo real:

`docker compose logs -f`

Reconstruir el proyecto

Si realizaste cambios en el Dockerfile o en las dependencias:

`docker compose down`

`docker compose up --build`

Desarrollo

Para trabajar en desarrollo, se recomienda utilizar volúmenes para que los cambios realizados en el código se reflejen dentro del contenedor sin tener que reconstruir la imagen constantemente.

Variables de entorno

Variable	Descripción	Ejemplo

`DB_HOST`	Host de la base de datos	db

`DB_PORT`	Puerto de la base de datos	5432

`DB_NAME`	Nombre de la base de datos	crud_db

`DB_USER`	Usuario de la base de datos	admin

`DB_PASSWORD`	Contraseña	admin

`PORT`	Puerto de la API	3000

Comandos útiles

# Levantar el proyecto

`docker compose up -d`

# Construir imágenes

`docker compose build`

# Ver contenedores

`docker compose ps`

# Ver logs

`docker compose logs -f`

# Entrar al contenedor de la aplicación

`docker compose exec app sh`

# Detener el proyecto

`docker compose down`

# Eliminar contenedores y volúmenes

docker compose down -v

Licencia

Este proyecto está disponible bajo la licencia <MIT / Apache 2.0 / otra>.
