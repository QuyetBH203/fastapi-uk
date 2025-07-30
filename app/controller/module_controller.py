from fastapi import APIRouter
from app.schemas.module_schema import CreateModuleDto, ModuleResponse
from app.models.module import Module
from app.service.module_service import ModuleService


module_router = APIRouter(prefix="/module", tags=["module"])


@module_router.post("/", status_code = 201)
async def create_module(module: CreateModuleDto):
    service = ModuleService()
    return await service.create_module(module)

