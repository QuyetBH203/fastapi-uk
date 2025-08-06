from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.service.module_service import ModuleService
from core.db.session import get_db_session
from app.repository.module_repo import ModuleRepo, ModuleRepoImpl

def get_module_repo(
    db: AsyncSession = Depends(get_db_session),
) -> ModuleRepo:
    return ModuleRepoImpl(db)

def get_module_service(
    repo: ModuleRepo = Depends(get_module_repo),
) -> ModuleService:
    return ModuleService(repo)