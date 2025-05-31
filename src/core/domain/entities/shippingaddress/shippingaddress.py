from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class ShippingAddress(Base):
    __tablename__ = "ShippingAddress"

    ShippingAddressId = Column(Integer, primary_key=True, index=True)
    ShippingAddress = Column(String(500), nullable=True)
    ShippingAddressSalesforceId = Column(String(18), nullable=True)
    IsDeleted = Column(Boolean, nullable=False, default=False)
    CreatedOn = Column(DateTime, nullable=False, default=datetime.utcnow)
    CreatedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    ModifiedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, default=datetime.utcnow)

    # Relationships
    creator = relationship("User", foreign_keys=[CreatedBy], backref="created_shipping_addresses")
    modifier = relationship("User", foreign_keys=[ModifiedBy], backref="modified_shipping_addresses")

    def __repr__(self):
        return f"<ShippingAddress(Id={self.ShippingAddressId}, Address='{self.ShippingAddress}')>"