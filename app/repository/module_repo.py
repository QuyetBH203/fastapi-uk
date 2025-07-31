from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.module import Module
from sqlalchemy import or_, select, delete, update
from core.db import session
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page
from fastapi_pagination.default import Params


class ModuleRepo(ABC):
    @abstractmethod
    async def create_module(self, module: Module) -> Module:
        pass
    
    @abstractmethod
    async def get_module_by_id(self, module_id: int) -> Optional[Module]:
        pass

    @abstractmethod
    async def get_all_modules(self) -> List[Module]:
        pass

    @abstractmethod
    async def update_module(self, module_id: int, module: Module) -> Module:
        pass

    @abstractmethod
    async def delete_module(self, module_id: int) -> None:
        pass

class ModuleRepoImpl(ModuleRepo):
    async def create_module(self, module: Module) -> Module:
        session.add(module)
        await session.commit()
        await session.refresh(module)
        return module
    
    async def get_module_by_id(self, module_id: int) -> Optional[Module]:
        return await session.get(Module, module_id)
    
    async def get_all_modules(self, page: int, limit: int, search: str | None = None) -> Page[Module]:
        stmt = select(Module)
        if search:
            stmt = stmt.where(or_(
                Module.name.ilike(f"%{search}%"),
                Module.description.ilike(f"%{search}%"),
            ))
        params = Params(page=page, size=limit)
        return await paginate(session, stmt, params)
    
    async def update_module(self, module_id: int, module: Module) -> Module:
        
        # build update dict from module instance
        attrs = {col.name: getattr(module, col.name) for col in Module.__table__.columns if col.name != 'id'}
        stmt = update(Module).where(Module.id == module_id).values(**attrs)
        await session.execute(stmt)
        await session.commit()
       
        await session.refresh(module)
        return module
    
    async def delete_module(self, module_id: int) -> None:
        stmt = delete(Module).where(Module.id == module_id)
        await session.execute(stmt)
        await session.commit()