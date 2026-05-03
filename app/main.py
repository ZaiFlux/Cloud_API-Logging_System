from fastapi import FastAPI

app = FastAPI()

users = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/users")
def get_users():
    return {"users": users}

@app.post("/users")
def create_user(user: dict):
    users.append(user)
    return {"message": "user created", "user": user}