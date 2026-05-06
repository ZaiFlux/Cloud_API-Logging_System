from fastapi import APIRouter, HTTPException
from app.models import UserCreate, User

router = APIRouter()

# temporary database (in-memory)
users = []

# ✅ CREATE USER
@router.post("/users", response_model=User)
def create_user(user: UserCreate):
    new_user = User(
        id=len(users) + 1,
        name=user.name,
        email=user.email
    )
    users.append(new_user)
    return new_user


# ✅ GET ALL USERS
@router.get("/users")
def get_users():
    return {"users": users}


# ✅ GET USER BY ID
@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user

    raise HTTPException(status_code=404, detail="User not found")