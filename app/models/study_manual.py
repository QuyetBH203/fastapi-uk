from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, composite, relationship
from core.base_model.timestamp_model import TimestampModel
from core.enum.role import Role

from core.db import Base


class StudyManual(Base, TimestampModel):
    __tablename__ = "study_manuals"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    module_id: Mapped[int] = mapped_column(ForeignKey("modules.id"), nullable=False)
    module: Mapped["Module"] = relationship("Module", back_populates="study_manuals")