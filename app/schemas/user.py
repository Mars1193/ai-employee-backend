from pydantic import BaseModel, EmailStr
from typing import List

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    documents: List['Document'] = []

    class Config:
        from_attributes = True

# Forward reference for Document
from app.schemas.document import Document
User.update_forward_refs()
