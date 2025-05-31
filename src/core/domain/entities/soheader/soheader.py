from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class SoHeader(Base):
    __tablename__ = "SoHeader"

    SOHeaderID = Column(Integer, primary_key=True, index=True)
    OrderId = Column(String(30), ForeignKey("Orders.OrderId"), nullable=True)
    SOId = Column(String(20), nullable=True)
    SOSalesforceId = Column(String(18), nullable=True)
    DateTimeOrdered = Column(DateTime, nullable=True, default=datetime.utcnow)
    CSRId_OrderTakenBy = Column(Integer, ForeignKey("CSR.CSRId"), nullable=True)
    PONumber = Column(String(15), nullable=False)
    SoldToId = Column(Integer, ForeignKey("SoldTo.SoldToId"), nullable=False)
    ShippingaddressId = Column(Integer, ForeignKey("ShippingAddress.ShippingAddressId"), nullable=False)
    ShipDate = Column(DateTime, nullable=True)
    CustomerRequestDate = Column(DateTime, nullable=True)
    Company = Column(String(30), nullable=False)
    ProductId = Column(Integer, ForeignKey("Product.ProductId"), nullable=False)
    ContactId = Column(Integer, ForeignKey("Contact.ContactId"), nullable=False)
    CutDetailsID = Column(Integer, ForeignKey("CutDetails.CutDetailsID"), nullable=True)
    SpecialInstructions = Column(String(8000), nullable=True)
    CreatedOn = Column(DateTime, nullable=False, default=datetime.utcnow)
    CreatedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    ModifiedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, default=datetime.utcnow)
    IsDeleted = Column(Boolean, nullable=False, default=False)

    # Relationships
    order = relationship("Order", backref="so_header_ref", foreign_keys=[OrderId])
    csr = relationship("CSR", backref="so_headers", foreign_keys=[CSRId_OrderTakenBy])
    contact = relationship("Contact", backref="so_headers", foreign_keys=[ContactId])
    creator = relationship("User", foreign_keys=[CreatedBy], backref="created_so_headers")
    modifier = relationship("User", foreign_keys=[ModifiedBy], backref="modified_so_headers")
    product = relationship("Product", backref="so_headers")
    sold_to = relationship("SoldTo", backref="so_headers")
    shipping_address = relationship("ShippingAddress", backref="so_headers")
    cut_details = relationship("CutDetails", backref="so_headers")

    def __repr__(self):
        return f"<SoHeader(SOHeaderID={self.SOHeaderID}, SOId='{self.SOId}', PONumber='{self.PONumber}')>"