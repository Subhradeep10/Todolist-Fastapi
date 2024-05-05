# Setting up python environment

Run the following to create a virtual environment for the project. (Assuming you have python installed on local machine)

```bash
python -m virtualenv env

```

If you're running the deployed instance, make sure to change the database connection string in `.env` file on the backend.

### Setting up `.env` file

To setup `.env` file on the backend, change the file named `.env` in `/app`.
Add the following in the `.env` file.

```txt
JWT_SECRET_KEY=<RAMDOM_STRING>
JWT_REFRESH_SECRET_KEY=<RANDOM_SECTURE_LONG_STRING>
MONGO_CONNECTION_STRING=<MONGO_DB_CONNECTION_STRING>
# mongodb://localhost:27017/ <-- for local running instances
```

# Activating virtual environment

```bash
# Windows
env/Scripts/activate

```

# Installing dependencies

Assuming you are in the base directory.

```bash
pip install -r requirements.txt
```

# Running the backend

Assuming you are in the backend directory.

```bash
uvicorn app.app:app --reload
```

# Todo-List API

Version: 0.1.0

## Swagger Documentation

You can view the Swagger documentation for this API by clicking [here](./swagger.yaml).

To interact with the API endpoints, you can use tools like [Swagger UI](https://swagger.io/tools/swagger-ui/) or [Redoc](https://redoc.ly/).

# Users Endpoints

- **Create User**

  - **URL**: `/api/v1/users/create`
  - **Method**: `POST`
  - **Description**: Creates a new user.
  - **Request Body**: [UserAuth](#userauth)
  - **Responses**:
    - `200`: Successful Response. Returns [UserOut](#userout).
    - `422`: Validation Error. Returns [HTTPValidationError](#httpvalidationerror).

- **Get Current User Details**

  - **URL**: `/api/v1/users/me`
  - **Method**: `GET`
  - **Description**: Retrieves details of the currently logged-in user.
  - **Responses**:
    - `200`: Successful Response. Returns [UserOut](#userout).

- **Update User**

  - **URL**: `/api/v1/users/update`
  - **Method**: `POST`
  - **Description**: Updates user information.
  - **Request Body**: [UserUpdate](#userupdate)
  - **Responses**: - `200`: Successful Response. Returns [UserOut](#userout). - `422`: Validation Error. Returns [HTTPValidationError](#httpvalidationerror).

# Tasks Endpoints

- **Get All Tasks of the User**

  - **URL**: `/api/v1/tasks/`
  - **Method**: `GET`
  - **Description**: Retrieves all todos of the user.
  - **Responses**:
    - `200`: Successful Response. Returns an array of [TodoOut](#todoout).

- **Create Tasks**

  - **URL**: `/api/v1/tasks/create`
  - **Method**: `POST`
  - **Description**: Creates a new todo.
  - **Request Body**: [TodoCreate](#todocreate)
  - **Responses**:
    - `200`: Successful Response. Returns [Todo](#todo).
    - `422`: Validation Error. Returns [HTTPValidationError](#httpvalidationerror).

- **Get a Tasks by Todo ID**

  - **URL**: `/api/v1/tasks/{todo_id}`
  - **Method**: `GET`
  - **Description**: Retrieves a todo by its ID.
  - **Parameters**:
    - `todo_id` (path) - Todo ID (UUID format)
  - **Responses**:
    - `200`: Successful Response. Returns [TodoOut](#todoout).
    - `422`: Validation Error. Returns [HTTPValidationError](#httpvalidationerror).

- **Update Tasks by Todo ID**

  - **URL**: `/api/v1/tasks/{todo_id}`
  - **Method**: `PUT`
  - **Description**: Updates a todo by its ID.
  - **Parameters**:
    - `todo_id` (path) - Todo ID (UUID format)
  - **Request Body**: [TodoUpdate](#todoupdate)
  - **Responses**:
    - `200`: Successful Response. Returns [TodoOut](#todoout).
    - `422`: Validation Error. Returns [HTTPValidationError](#httpvalidationerror).

- **Delete Tasks by Todo ID**
  - **URL**: `/api/v1/tasks/{todo_id}`
  - **Method**: `DELETE`
  - **Description**: Deletes a todo by its ID.
  - **Parameters**:
    - `todo_id` (path) - Todo ID (UUID format)
  - **Responses**:
    - `200`: Successful Response.
    - `422`: Validation Error. Returns [HTTPValidationError](#httpvalidationerror).

# Authentication Endpoints

## Login

- **URL**: `/api/v1/auth/login`
- **Method**: `POST`
- **Summary**: Create access and refresh tokens for user
- **Request Body**: [Body_login_api_v1_auth_login_post](#body_login_api_v1_auth_login_post)
- **Responses**:
  - `200`: Successful Response. Returns [TokenSchema](#tokenschema).
  - `422`: Validation Error. Returns [HTTPValidationError](#httpvalidationerror).

## Test Token

- **URL**: `/api/v1/auth/test-token`
- **Method**: `POST`
- **Summary**: Test if the access token is valid
- **Responses**:
  - `200`: Successful Response. Returns [UserOut](#userout).
  - `401`: Unauthorized. Returns [HTTPUnauthorizedError](#httpunauthorizederror).

## Refresh Token

- **URL**: `/api/v1/auth/refresh`
- **Method**: `POST`
- **Summary**: Refresh token
- **Request Body**: Refresh Token (string)
- **Responses**:
  - `200`: Successful Response. Returns [TokenSchema](#tokenschema).
  - `422`: Validation Error. Returns [HTTPValidationError](#httpvalidationerror).

...

## Swagger Specification

The Swagger specification for the API endpoints is provided below:

```yaml
swagger.yaml
```
