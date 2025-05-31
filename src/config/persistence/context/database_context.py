from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from urllib.parse import quote_plus

import os

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT", "1433")
database = os.getenv("DB_NAME")

# ✅ Build ODBC string and URL encode
odbc_str = (
    f"DRIVER=ODBC Driver 18 for SQL Server;"
    f"SERVER={host},{port};"
    f"DATABASE={database};"
    f"UID={user};"
    f"PWD={password};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
    f"Connection Timeout=30;"
)
encoded_odbc = quote_plus(odbc_str)

# ✅ SQLAlchemy async database URL
DATABASE_URL = f"mssql+aioodbc:///?odbc_connect={encoded_odbc}"

# ✅ Create async engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# ✅ Create session factory
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# ✅ Declarative base for models
Base = declarative_base()

# ✅ Async DB dependency for FastAPI / DI container
async def get_db_async() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
