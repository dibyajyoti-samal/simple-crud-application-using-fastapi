# FastAPI CRUD API

A simple REST API built with **FastAPI** and **MongoDB**.

## Features

- Create a user
- Get all users
- Get a user by name
- Update a user
- Delete a user
- Interactive API documentation
- MongoDB integration

---

## Requirements

- Python 3.10+
- MongoDB
- pip

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd project-name
```

### 2. Create a virtual environment

Linux/Mac

```bash
python3 -m venv venv
```

Windows

```cmd
python -m venv venv
```

### 3. Activate the virtual environment

Linux/Mac

```bash
source venv/bin/activate
```

Windows

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Start MongoDB

Make sure MongoDB is running.

Default connection string:

```text
mongodb://localhost:27017
```

---

## Run the FastAPI Server

```bash
uvicorn main:app --reload
```

Server will start at

```
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# Testing the API

## Using Swagger UI

1. Open

```
http://127.0.0.1:8000/docs
```

2. Select an endpoint.

3. Click **Try it out**.

4. Enter the request body (if required).

5. Click **Execute**.

---

## Using cURL

### Create User

```bash
curl -X POST "http://127.0.0.1:8000/users" \
-H "Content-Type: application/json" \
-d '{
    "name":"John",
    "age":25,
    "city":"New York"
}'
```

### Get All Users

```bash
curl http://127.0.0.1:8000/users
```

### Get User by Name

```bash
curl http://127.0.0.1:8000/users/John
```

### Update User

```bash
curl -X PUT "http://127.0.0.1:8000/users/John" \
-H "Content-Type: application/json" \
-d '{
    "name":"John",
    "age":26,
    "city":"Boston"
}'
```

### Delete User

```bash
curl -X DELETE http://127.0.0.1:8000/users/John
```

---

## Example Request Body

```json
{
    "name": "John",
    "age": 25,
    "city": "New York"
}
```

---

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## Install Dependencies

If `requirements.txt` is not available:

```bash
pip install fastapi uvicorn pymongo pydantic
```

Generate `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## Stop the Server

Press

```text
CTRL + C
```

---

## Author

Dibyajyoti samal
