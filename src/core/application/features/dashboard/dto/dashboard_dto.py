from pydantic import BaseModel, Field
from typing import Self

class DashboardDTO(BaseModel):
    dashboard_name: str = Field(..., max_length=500)

    class Config:
        from_attributes = True  # Enables ORM support (same as orm_mode = True)


class DashboardRead(DashboardDTO):
    dashboard_id: int

    class Config:
        from_attributes = True