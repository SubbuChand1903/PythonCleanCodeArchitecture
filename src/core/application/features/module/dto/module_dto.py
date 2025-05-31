from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ModuleDTO(BaseModel):
    ModuleName: str = Field(..., max_length=255)

    class Config:
        from_attributes = True

class ModuleRead(ModuleDTO):
    ModuleId: int
    DashboardId: Optional[int]
    DashboardName: str

    class Config:
        from_attributes = True
