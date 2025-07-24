from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, composite, relationship
from core.base_model.timestamp_model import TimestampModel
from core.enum.role import Role

from core.db import Base


class Mark(Base, TimestampModel):
    __tablename__ = "marks"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    answer_id: Mapped[int] = mapped_column(ForeignKey("answers.id"), nullable=False)
    answer: Mapped["Answer"] = relationship("Answer", back_populates="marks")
    score: Mapped[int] = mapped_column(Integer, nullable=False)
    feedback: Mapped[str] = mapped_column(Text, nullable=False)
    tutor_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    tutor: Mapped["User"] = relationship("User", back_populates="marks")