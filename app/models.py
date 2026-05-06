from pydantic import BaseModel, EmailStr

# input model (no ID from user)
class UserCreate(BaseModel):
    name: str
    email: EmailStr

# output model (with ID)
class User(BaseModel):
    id: int
    name: str
    email: EmailStr