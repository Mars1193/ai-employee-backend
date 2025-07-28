from fastapi import FastAPI
from app.db import models
from app.db.database import engine
from app.api import auth, documents

# This line creates the FastAPI application instance
app = FastAPI(title="NAS AI Employee Backend")

@app.on_event("startup")
async def startup_event():
    """
    On startup, create database tables.
    """
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

# Include API routers from other files
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the NAS AI Core API"}