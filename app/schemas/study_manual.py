from pydantic import BaseModel, Field


class CreateStudyManualDto(BaseModel):
    content: str = Field(..., description="The content of the study manual")
    module_id: int = Field(..., description="The id of the module")
