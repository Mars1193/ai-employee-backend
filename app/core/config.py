# File: app/core/config.py
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    # This is the most important line.
    # The password has been correctly URL-encoded (@ becomes %40).
    DATABASE_URL: str = "postgresql+asyncpg://postgres.venbkhnqghutyhizhdtn:Mabdallah1%401@aws-0-eu-north-1.pooler.supabase.com:6543/postgres"
    
    SECRET_KEY: str = "your_super_secret_key_for_now"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        # This tells Pydantic to look for an .env file if it exists
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
