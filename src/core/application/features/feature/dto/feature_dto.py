from pydantic import BaseModel, Field
from typing import Optional

class FeatureDTO(BaseModel):
    FeatureName: str = Field(..., max_length=500)

    class Config:
        from_attributes = True

class FeatureRead(FeatureDTO):
    FeatureId: int
    DashboardId: int
    DashboardName: str
    ModuleId: int
    ModuleName: str

    class Config:
        from_attributes = True
