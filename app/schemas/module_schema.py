from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class CreateModuleDto(BaseModel):
    name: str = Field(..., description="The name of the module")
    description: str = Field(..., description="The description of the module")


class ModuleResponse(BaseModel):
    id: int = Field(..., description="The id of the module")
    name: str = Field(..., description="The name of the module")
    description: str = Field(..., description="The description of the module")
    created_at: datetime = Field(..., description="The date and time the module was created")
    updated_at: datetime = Field(..., description="The date and time the module was updated")
    
    class Config:
        from_attributes = True
 

class UpdateModuleDto(BaseModel):
    name: Optional[str] = Field(None, description="The name of the module (optional)")
    description: Optional[str] = Field(None, description="The description of the module (optional)")