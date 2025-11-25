from pydantic import BaseModel
from typing import Optional
from app.models.employees import EmployeeStatus

class EmployeeSchemaResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    department: Optional[str] = None
    location: Optional[str] = None
    company: Optional[str] = None
    position: Optional[str] = None
    status: EmployeeStatus