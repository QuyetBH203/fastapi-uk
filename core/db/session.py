from contextlib import asynccontextmanager
from contextvars import ContextVar, Token
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from core.config import config  

#
session_context: ContextVar[str] = ContextVar("session_context")

def get_session_context() -> str:
    return session_context.get()

def set_session_context(session_id: str) -> Token:
    return session_context.set(session_id)

def reset_session_context(context: Token) -> None:
    session_context.reset(context)

# Tạo engine async duy nhất
engine = create_async_engine(config.DB_URL, pool_recycle=3600)

# Tạo session factory
_async_session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Tạo async scoped session để tự gắn session theo context (ví dụ mỗi request)
session = async_scoped_session(
    session_factory=_async_session_factory,
    scopefunc=get_session_context,
)

# Base class cho ORM
class Base(DeclarativeBase):
    ...

# Tạo context manager để dùng trong async with
@asynccontextmanager
async def session_factory() -> AsyncGenerator[AsyncSession, None]:
    async with _async_session_factory() as _session:
        yield _session
