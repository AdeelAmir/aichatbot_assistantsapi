from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:12345678@localhost:5432/airag-chatbot-db")

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session local factory
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Base class for models
Base = declarative_base()

# Dependency to use in routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session