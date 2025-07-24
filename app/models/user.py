from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, composite, relationship
from core.base_model.timestamp_model import TimestampModel
from core.enum.role import Role

from core.db import Base


class User(Base, TimestampModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[Role] = mapped_column(String(255), nullable=False)
    answers: Mapped[list["Answer"]] = relationship("Answer", back_populates="student")
    marks: Mapped[list["Mark"]] = relationship("Mark", back_populates="tutor")