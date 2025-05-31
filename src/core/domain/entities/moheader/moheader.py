from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class MoHeader(Base):
    __tablename__ = "MoHeader"

    MOHeaderId = Column(Integer, primary_key=True, index=True)
    MOId = Column(Integer, nullable=True)
    MOSalesforceId = Column(String(18), nullable=True)
    OrderId = Column(String(30), ForeignKey("Orders.OrderId"), nullable=False)
    CustomerId = Column(Integer, ForeignKey("Customer.CustomerId"), nullable=False)
    ShippingaddressId = Column(Integer, ForeignKey("ShippingAddress.ShippingAddressId"), nullable=False)
    ProductId = Column(Integer, ForeignKey("Product.ProductId"), nullable=False)
    ContactId = Column(Integer, ForeignKey("Contact.ContactId"), nullable=False)
    ShippingMethodId = Column(Integer, ForeignKey("ShippingMethod.ShippingMethodId"), nullable=False)
    QuoteReferenceId = Column(Integer, ForeignKey("QuoteReference.QuoteReferenceId"), nullable=False)
    CSRId_OrderTakenBy = Column(Integer, ForeignKey("CSR.CSRId"), nullable=False)
    SpecialInstructions = Column(String(8000), nullable=True)
    PONumber = Column(String(15), nullable=False)
    ShipDate = Column(DateTime, nullable=True)
    OrderDate = Column(DateTime, nullable=True)
    Status = Column(Integer, nullable=True, default=4)
    IsMigrated = Column(Boolean, default=False)
    IsTransfer = Column(Boolean, default=False)
    PromotionCode = Column(String(15), nullable=True)
    FOBPoint = Column(String(30), nullable=True)
    IsDeleted = Column(Boolean, nullable=False, default=False)
    CreatedOn = Column(DateTime, nullable=False, default=datetime.utcnow)
    CreatedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    ModifiedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, default=datetime.utcnow)

    # Relationships
    contact = relationship("Contact", backref="mo_headers")
    customer = relationship("Customer", backref="mo_headers")
    creator = relationship("User", foreign_keys=[CreatedBy], backref="created_mo_headers")
    modifier = relationship("User", foreign_keys=[ModifiedBy], backref="modified_mo_headers")
    order = relationship("Order", backref="mo_header_ref")
    product = relationship("Product", backref="mo_headers")
    quote_reference = relationship("QuoteReference", backref="mo_headers")
    shipping_address = relationship("ShippingAddress", backref="mo_headers")
    shipping_method = relationship("ShippingMethod", backref="mo_headers")
    csr = relationship("CSR", backref="mo_headers")

    def __repr__(self):
        return f"<MoHeader(MOHeaderId={self.MOHeaderId}, MOId={self.MOId}, PONumber='{self.PONumber}')>"