from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RegisterRequest(BaseModel):
    username: str
    password: str
    email: str | None = None

users = []

@app.get("/")
def read_root():
    return{"Hello": "World"}

@app.get("/users")
def get_users():
    return{"users": users}

@app.post("/register")
def register(register_request: RegisterRequest):
    new_user = {
        "username": register_request.username,
        "password": register_request.password,
        "email": register_request.email
    }
    users.append(new_user)
    print(f"User {new_user} registered.")
    return {"success": True}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return{"item_id": item_id, "q": q}
