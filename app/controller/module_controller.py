from fastapi import APIRouter
from typing import List
from app.schemas.module_schema import CreateModuleDto, ModuleResponse
from app.schemas.module_schema import UpdateModuleDto
from fastapi_pagination import Page
from app.models.module import Module
from app.service.module_service import ModuleService

module_router = APIRouter(prefix="/module", tags=["module"])


@module_router.post("/", response_model=ModuleResponse, status_code=201, summary="Create a new module")
async def create_module(module: CreateModuleDto):
    module_service = ModuleService()
    created = await module_service.create_module(module)
    return created


@module_router.get("/{module_id}", response_model=ModuleResponse, status_code=200)
async def get_module_by_id(module_id: int):
    module_service = ModuleService()
    module = await module_service.get_module_by_id(module_id)
    return module


@module_router.get("/", response_model=Page[ModuleResponse], status_code=200)
async def get_all_modules(page: int = 1, limit: int = 10, search: str | None = None):
    module_service = ModuleService()
    modules = await module_service.get_all_modules(page, limit, search)
    return modules


@module_router.patch("/{module_id}", response_model=ModuleResponse, status_code=200, summary="Update a module")
async def update_module(module_id: int, module: UpdateModuleDto):
    module_service = ModuleService()
    return await module_service.update_module(module_id, module)


@module_router.delete("/{module_id}", status_code=200, summary="Delete a module")
async def delete_module(module_id: int):
    module_service = ModuleService()
    await module_service.delete_module(module_id)
    return {"message": "Module deleted successfully"}
