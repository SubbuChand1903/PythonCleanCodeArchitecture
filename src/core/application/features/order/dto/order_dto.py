from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class OrderDTO(BaseModel):
    OrderId: str
    MOHeaderId: int
    MOId: Optional[int]
    MOSalesforceId: Optional[str]
    SOHeaderID: int
    SOId: Optional[str]
    SOSalesforceId: Optional[str]
    CustomerId: int
    SoldToId: int
    ShippingaddressId: int
    ProductId: int
    ContactId: int
    ShippingMethodId: int
    OrderTypeId: int
    GumTypeId: int
    MasterQtyDimTypesId: int
    QuoteReferenceId: int
    UMId: int
    CSRId_OrderTakenBy: int
    CSRId_CheckedBy: Optional[str]
    CSRId_RevisedBy: Optional[str]
    SetUpCharges: Optional[Decimal]
    AdhesiveChangeCharges: Optional[Decimal]
    LateOrder: Optional[bool]
    Reason: Optional[str]
    SpecialInstructions: Optional[str]
    LineNumber: str
    Notes: Optional[str]
    PrevMO: Optional[int]
    ApplicationProfileCompleted: bool
    CustomerRequestDate: Optional[datetime]
    PONumber: str
    ShipDate: Optional[datetime]
    OrderDate: Optional[datetime]
    Location: Optional[str]
    IsDeleted: bool
    CreatedOn: datetime
    CreatedBy: int
    ModifiedBy: Optional[int]
    ModifiedOn: Optional[datetime]
    OrderStatusId: int

    class Config:
        orm_mode = True

class OrderRead(OrderDTO):
    order_id: int
 
    class Config:
        from_attributes = True