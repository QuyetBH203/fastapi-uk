from core.base_model.timestamp_model import TimestampModel
from core.db import Base
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Organization(Base, TimestampModel):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    column_config: Mapped[dict] = mapped_column(JSONB, nullable=False, default={})
    employees: Mapped[list["Employees"]] = relationship("Employees", back_populates="organization")