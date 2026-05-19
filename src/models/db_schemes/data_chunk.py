from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from bson import ObjectId

class DataChunk(BaseModel):
    id: Optional[ObjectId] = Field(default=None, alias="_id")
    chunk_text: str
    chunk_metadata: dict = {}
    chunk_order: int
    chunk_project_id: ObjectId

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True
    )