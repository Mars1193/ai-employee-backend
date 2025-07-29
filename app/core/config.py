# File: app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Pydantic-settings will automatically look for these variables
    # in the system environment or a .env file.
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # This tells pydantic-settings to look for a .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

settings = Settings()

# --- DEBUGGING STEP ---
# We will print the final URL that the application is using.
print("--- Settings loaded. Final DATABASE_URL being used: ---")
print(f"'{settings.DATABASE_URL}'")
print("-------------------------------------------------")
# ----------------------