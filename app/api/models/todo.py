from pydantic import BaseModel , Field
from typing import Optional
from datetime import datetime

class TodoBase(BaseModel):
    title: str = Field(...,min_length=3, example="My Todo Title")
    description: Optional[str] = Field(None, example="My Todo Description")
    
class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoInDB(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True