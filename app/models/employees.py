from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, composite, relationship
from core.base_model.timestamp_model import TimestampModel
from core.enum.role import Role
from enum import Enum as PyEnum
from sqlalchemy import Enum
from core.db import Base


class EmployeeStatus(str, PyEnum):
    ACTIVE = "ACTIVE"
    NOT_STARTED = "NOT_STARTED"
    TERMINATED = "TERMINATED"

class Employees(Base, TimestampModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"), nullable=False)
    organization: Mapped["Organization"] = relationship("Organization", back_populates="employees")
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(255), nullable=True)
    department: Mapped[str] = mapped_column(String(255), nullable=True)
    location: Mapped[str] = mapped_column(String(255), nullable=True)
    company: Mapped[str] = mapped_column(String(255), nullable=True)
    position: Mapped[str] = mapped_column(String(255), nullable=True)
    status: Mapped[EmployeeStatus] = mapped_column(Enum(EmployeeStatus), nullable=False, default=EmployeeStatus.ACTIVE)