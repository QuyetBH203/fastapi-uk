from typing import List, Generic, TypeVar
from pydantic import BaseModel, ConfigDict



T = TypeVar('T')

class MetaSchema(BaseModel):
    items_per_page: int
    total_items: int
    current_page: int
    total_pages: int
    current_items: int = 0

    model_config = ConfigDict(from_attributes=True)
    

class PaginatedResponse(BaseModel, Generic[T]):
    data: List[T]
    meta: MetaSchema
    model_config = ConfigDict(from_attributes=True)