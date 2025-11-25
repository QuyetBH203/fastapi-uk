from app.models.employees import EmployeeStatus
from fastapi import APIRouter, Depends
from typing import Annotated
from app.service.employee_service import get_all_employees_with_filters_service
from core.enum.propagation import SortOrder
from core.db import get_db_session
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("/")
async def get_all_employees_with_filters(
    db: Annotated[AsyncSession, Depends(get_db_session)],
    status: EmployeeStatus = EmployeeStatus.ACTIVE,
    location: str | None = None,
    company: str | None = None,
    department: str | None = None,
    position: str | None = None,
    page: int = 1,
    limit: int = 10,

):
    status_str = status.value if status else None
    response = await get_all_employees_with_filters_service(db, status_str, location, company, department, position, page, limit)
    pass
