from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OpenOrderDTO(BaseModel):
    OrderId: str
    MOId: int
    SOId: str
    CustomerName: str
    ProductName: str
    ShipDate: datetime
    OrderStatus: str
    CreatedBy: int
    CreatedOn: datetime
    UpdatedBy: Optional[int]
    UpdatedOn: Optional[datetime]

    class Config:
        from_attributes = True