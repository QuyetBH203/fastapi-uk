from sqlalchemy.ext.asyncio import AsyncSession


async def get_all_employees_with_filters_service(
    db: AsyncSession,
    status: str,
    location: str | None = None,
    company: str | None = None,
    department: str | None = None,
    position: str | None = None,
    page: int = 1,
    limit: int = 10,
):
    pass
