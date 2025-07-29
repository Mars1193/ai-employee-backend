# File: app/core/config.py
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file at the very beginning
load_dotenv()

class Settings(BaseSettings):
    # Read the database URL and strip any leading/trailing whitespace or newlines
    DATABASE_URL: str = os.getenv("DATABASE_URL", "").strip()
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()