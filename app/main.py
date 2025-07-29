# File: app/main.py
import os
from fastapi import FastAPI
from app.db import database, models
from app.api import auth, documents
from app.core.config import settings

# --- DEBUGGING STEP ---
# Print the database URL to the logs to verify it
print("--- Attempting to connect with DATABASE_URL: ---")
print(f"'{settings.DATABASE_URL}'")
print("-------------------------------------------------")
# ----------------------

app = FastAPI(title="NAS AI Employee Backend")

@app.on_event("startup")
async def startup_event():
    """
    On startup, create database tables.
    """
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

# Include API routers from other files
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the NAS AI Core API"}