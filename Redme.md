# FastAPI Example

Este es un ejemplo de una aplicación web simple utilizando FastAPI, un marco web moderno para Python. La aplicación incluye controladores, servicios y un modelo para administrar autores.

## Controladores

### `create_author_route`

Este controlador permite crear un nuevo autor con campos específicos. Para acceder a este endpoint, se requiere autenticación básica. Los usuarios válidos y sus contraseñas deberán ser definidos en el archivo .env en la raíz del proyecto para ser implementados en el diccionario `valid_users` en el archivo de controladores.

- Método HTTP: `POST`
- Ruta: `/input/authors/{my_target_field}`
- Parámetros de entrada:
  - `author`: Un objeto `Author` que representa al autor a crear.
  - `my_target_field`: Una cadena que indica el campo específico que se utilizará para convertir a mayúscula.
- Autenticación: Basic Auth
- Respuesta exitosa:
  - Código de estado: `200 OK`
  - Respuesta JSON con el ID del autor creado.

### `get_author_id_route`

Este controlador permite obtener la información de un autor por su ID.

- Método HTTP: `GET`
- Ruta: `/authors/{id}`
- Parámetros de entrada:
  - `id`: El ID del autor que se desea recuperar.
- Respuesta exitosa:
  - Código de estado: `200 OK`
  - Respuesta JSON con la información del autor.

## Servicios

### `create_author`

Este servicio se encarga de crear un nuevo autor en la base de datos. También convierte un campo específico en mayúscula antes de almacenarlo en la base de datos.

- Parámetros de entrada:
  - `new_author`: Un objeto `Author` que representa al autor a crear.
  - `my_target_field`: Una cadena que indica el campo específico que se utilizará para convertir a mayúscula.
- Retorna el autor creado.

### `get_author_id`

Este servicio se utiliza para obtener la información de un autor por su ID desde la base de datos.

- Parámetros de entrada:
  - `id`: El ID del autor que se desea recuperar.
- Retorna la información del autor.

## Modelo

### `Author`

Este modelo define la estructura de un autor con los siguientes campos:

- `field_1`: Una cadena.
- `author`: Una cadena.
- `description`: Una cadena.
- `my_numeric_field`: Un entero.

Este modelo también incluye un método `save` para guardar un autor en la base de datos.

## Base de datos

La aplicación utiliza una base de datos SQLite para almacenar la información de los autores. La función `create_tables` en el archivo de base de datos se encarga de crear la tabla necesaria si no existe.

## Ejecución

Para ejecutar esta aplicación, asegúrate de tener FastAPI y Uvicorn instalados. Luego, puedes ejecutar el servidor utilizando el siguiente comando:

```bash
uvicorn main:app --reload


