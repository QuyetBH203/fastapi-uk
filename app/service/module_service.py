from pythondi import inject
from app.repository.module_repo import ModuleRepo
from app.models.module import Module
from app.schemas.module_schema import CreateModuleDto

class ModuleService:
    @inject()
    def __init__(self, module_repo: ModuleRepo):
        self.module_repo = module_repo

    async def create_module(self, module_dto: CreateModuleDto) -> Module:
        module = Module(
            name=module_dto.name,
            description=module_dto.description
        )
        return await self.module_repo.create_module(module)
    