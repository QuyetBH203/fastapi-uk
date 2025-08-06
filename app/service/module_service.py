from fastapi import HTTPException
from app.repository.module_repo import ModuleRepo
from app.models.module import Module
from app.schemas.module_schema import CreateModuleDto
from typing import Optional, List
from app.schemas.module_schema import ModuleResponse
from fastapi_pagination import Page
from app.schemas.module_schema import UpdateModuleDto

class ModuleService:
    
    def __init__(self, module_repo: ModuleRepo):
        self.module_repo = module_repo

    async def create_module(self, module_dto: CreateModuleDto) -> ModuleResponse:
        module = Module(
            name=module_dto.name,
            description=module_dto.description
        )
        created_module = await self.module_repo.create_module(module)
        return ModuleResponse.model_validate(created_module)
    

    async def get_module_by_id(self, module_id: int) -> Optional[ModuleResponse]:
        module = await self.module_repo.get_module_by_id(module_id)
        if module is None:
            raise HTTPException(status_code=404, detail="Module not found")
        return ModuleResponse.model_validate(module)
    
    async def get_all_modules(self, page: int, limit: int, search: str | None = None) -> Page[ModuleResponse]:
      
        module_page = await self.module_repo.get_all_modules(page, limit, search)
        
        items = [ModuleResponse.model_validate(m) for m in module_page.items]
     
        return Page[ModuleResponse](
            items=items,
            total=module_page.total,
            page=module_page.page,
            size=module_page.size,
        )
    
    async def update_module(self, module_id: int, module_dto: UpdateModuleDto) -> ModuleResponse:
       
        existing = await self.module_repo.get_module_by_id(module_id)
        if existing is None:
            raise HTTPException(status_code=404, detail="Module not found")
        
        updates = module_dto.model_dump(exclude_unset=True)
        for attr, value in updates.items():
            setattr(existing, attr, value)
        updated = await self.module_repo.update_module(module_id, existing)
        return ModuleResponse.model_validate(updated)

    async def delete_module(self, module_id: int) -> None:
        
        existing = await self.module_repo.get_module_by_id(module_id)
        if existing is None:
            raise HTTPException(status_code=404, detail="Module not found")
        await self.module_repo.delete_module(module_id)