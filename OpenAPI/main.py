from fastapi import FastAPI
from fastapi.params import Query

app = FastAPI()

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    {"id": 4, "name": "Diana", "email": "diana@example.com"},
    {"id": 5, "name": "Eve", "email": "eve@example.com"},
]
@app.get("/ping")
def ping():
    return "pong"

@app.get("/users")
def get_users(
        page: int = Query(1, description="Numéro de la page", ge=1),
        size: int = Query(20, description="Nombre d'utilisateurs par page", ge=1)
):
    try:
        start = (page - 1) * size
        end = start + size
        return users[start:end]
    except Exception:
        return {"error": "Bad types for provided query parameters"}