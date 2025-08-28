from pydantic import BaseModel, Field


class CreateQuestionDto(BaseModel):
   module_id: int = Field(..., description="The id of the module")
   section: str = Field(..., description="The section of the question")
   title: str = Field(..., description="The type of the question")
   question_text: str = Field(..., description="The text of the question")
   marking_scheme: str = Field(..., description="The marking scheme of the question")