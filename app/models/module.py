from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, composite, relationship
from core.base_model.timestamp_model import TimestampModel
from core.enum.role import Role

from core.db import Base


class Module(Base, TimestampModel):
    __tablename__ = "modules"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    study_manuals: Mapped[list["StudyManual"]] = relationship("StudyManual", back_populates="module")
    questions: Mapped[list["Question"]] = relationship("Question", back_populates="module")