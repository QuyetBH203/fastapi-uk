from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, composite, relationship
from core.base_model.timestamp_model import TimestampModel
from core.enum.role import Role

from core.db import Base

class Answer(Base, TimestampModel):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    answer_text: Mapped[str] = mapped_column(Text, nullable=False)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id"), nullable=False)
    question: Mapped["Question"] = relationship("Question", back_populates="answers")
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    student: Mapped["User"] = relationship("User", back_populates="answers")
    marks: Mapped[list["Mark"]] = relationship("Mark", back_populates="answer")