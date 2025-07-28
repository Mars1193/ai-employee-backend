# File: app/api/documents.py
import shutil
from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db import database, models
from app.core.security import get_current_user
from app.schemas.document import Document

router = APIRouter()

@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_document(file: UploadFile = File(...), db: AsyncSession = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    
    db_document = models.Document(filename=file.filename, owner_id=current_user.id)
    db.add(db_document)
    await db.commit()
    await db.refresh(db_document)
    return {"filename": file.filename, "message": "File uploaded successfully"}

@router.get("/", response_model=List[Document])
async def get_documents(db: AsyncSession = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    result = await db.execute(select(models.Document).filter(models.Document.owner_id == current_user.id))
    return result.scalars().all()