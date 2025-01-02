# Scientists Backend - Instrucciones de Ejecución

Este documento describe las opciones disponibles para ejecutar el backend del proyecto Scientists, ya sea utilizando Docker completo o ejecutando algunos servicios manualmente fuera de Docker. También incluye instrucciones sobre cómo inicializar el entorno de desarrollo y acceder a los endpoints disponibles mediante Swagger.

---

## Opciones de Ejecución

### Opcion 1: Docker Completo

Esta opción utiliza Docker para manejar todos los servicios, incluyendo la base de datos y el backend.

#### Variables de Entorno
- **DB_HOST**: `scientists-postgres-db`
- **DB_PORT**: `5432`

#### Pasos:
1. Crear una red Docker:
   ```bash
   docker network create scientists
   ```

2. Iniciar los servicios con Docker Compose:
   ```bash
   docker compose -f ./docker-compose.dev.yml up --build
   ```

---

### Opcion 2: Sin scientists-database-services en Docker

Esta opción permite ejecutar el backend localmente con una base de datos iniciada desde Docker.

#### Variables de Entorno
- **DB_HOST**: `localhost`
- **DB_PORT**: `5435`

#### Pasos:
1. Iniciar la base de datos (PostgreSQL) con Docker Compose:
   ```bash
   docker compose -f ./docker-compose.dev.yml up --build
   ```

2. Iniciar los servicios del backend manualmente utilizando Poetry:
   - Acceder al entorno virtual:
     ```bash
     poetry shell
     ```
   - Instalar las dependencias necesarias:
     ```bash
     poetry install
     ```
   - Ejecutar la aplicación:
     ```bash
     python3 run.py
     ```

---

## Endpoints

Una vez que el backend esté en funcionamiento, los endpoints disponibles se pueden explorar a través de Swagger. Para acceder a la documentación interactiva de los endpoints, abre la URL correspondiente en tu navegador.

![Swagger Endpoints](./app/utils/swagger.png "Swagger")

---

## Notas Adicionales
- Asegúrate de tener Docker, Docker Compose y Poetry correctamente instalados en tu sistema.
- La configuración de las variables de entorno es clave para garantizar que los servicios se comuniquen correctamente.
- Para cualquier duda o incidencia, consulta la documentación del proyecto o contacta al equipo de desarrollo.




