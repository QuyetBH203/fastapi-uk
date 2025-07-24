from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, composite, relationship
from core.base_model.timestamp_model import TimestampModel
from core.enum.role import Role


from core.db import Base
from core.enum.section import Question_Section


class Question(Base, TimestampModel):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    module_id: Mapped[int] = mapped_column(ForeignKey("modules.id"), nullable=False)
    module: Mapped["Module"] = relationship("Module", back_populates="questions")
    section: Mapped[Question_Section] = mapped_column(String(1), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    question_text: Mapped[str] = mapped_column(Text, nullable=False)
    marking_scheme: Mapped[str] = mapped_column(Text, nullable=False)
    answers: Mapped[list["Answer"]] = relationship("Answer", back_populates="question")
    