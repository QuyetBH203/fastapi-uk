from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination.default import Params
from app.models.employees import Employees
from sqlalchemy import select


class CrudEmployee:
    def __init__(self):
        pass

    async def get_all_employees_with_filters(
        self,
        db: AsyncSession,
        status: str,
        location: str | None = None,
        company: str | None = None,
        department: str | None = None,
        position: str | None = None,
        page: int = 1,
        limit: int = 10,
    ):
        select_fields = [
            Employees.id,
            Employees.first_name,
            Employees.last_name,
            Employees.status
        ]
