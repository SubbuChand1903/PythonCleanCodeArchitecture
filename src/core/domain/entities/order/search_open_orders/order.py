from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class OpenOrder:
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
