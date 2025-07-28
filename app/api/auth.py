# File: app/api/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import database
from app.schemas.user import User, UserCreate # <-- Import corrected
from app.core import security
from app.crud import user as user_crud

router = APIRouter()

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: UserCreate, db: AsyncSession = Depends(database.get_db)):
    # Check if user already exists
    db_user = await user_crud.get_user_by_email(db, email=user_in.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
        
    # Create new user
    new_user = await user_crud.create_user(db=db, user=user_in)
    return new_user

# You can add login endpoint here later