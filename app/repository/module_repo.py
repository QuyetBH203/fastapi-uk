from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.module import Module
from sqlalchemy import or_, select
from core.db import session

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
        return module
    
    async def get_module_by_id(self, module_id: int) -> Optional[Module]:
        return session.query(Module).filter(Module.id == module_id).first()
    
    async def get_all_modules(self) -> List[Module]:
        return session.query(Module).all()
    
    async def update_module(self, module_id: int, module: Module) -> Module:
        session.query(Module).filter(Module.id == module_id).update(module.model_dump())
        await session.commit()
        return module
    
    async def delete_module(self, module_id: int) -> None:
        session.query(Module).filter(Module.id == module_id).delete()
        await session.commit()