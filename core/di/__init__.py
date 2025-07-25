from pythondi import Provider, configure
from app.repository.module_repo import ModuleRepo, ModuleRepoImpl

def init_di():
    provider = Provider()
    provider.bind(ModuleRepo, ModuleRepoImpl)
    configure(provider=provider)