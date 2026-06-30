from collections.abc import AsyncGeneration
import uuid

from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship

DATABASE_UIL = "sqlite+aiosqLite:///./test.db"

class Post(DeclarativeBase):
    __tablename__ = "posts"

    id = Column(UUID(as_uuide = True), primary_type= True, default = uuid.uuid4)
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    created_at = Column(DateTime, default = datetime.utcnow)
