# File: app/db/database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# This is the critical fix:
# We add connect_args to disable prepared statements, which is required
# for Supabase's PgBouncer connection pooler.
connect_args = {"server_settings": {"jit": "off", "statement_cache_size": "0"}}

engine = create_async_engine(
    settings.DATABASE_URL,
    connect_args=connect_args
)

AsyncSessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine, 
    class_=AsyncSession
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
