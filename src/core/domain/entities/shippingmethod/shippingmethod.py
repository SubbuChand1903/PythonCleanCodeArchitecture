from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class ShippingMethod(Base):
    __tablename__ = "ShippingMethod"

    ShippingMethodId = Column(Integer, primary_key=True, index=True)
    ShippingMethod = Column(String(500), nullable=False)
    IsDeleted = Column(Boolean, nullable=False, default=False)
    CreatedOn = Column(DateTime, nullable=False, default=datetime.utcnow)
    CreatedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    ModifiedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, default=datetime.utcnow)

    # Relationships
    creator = relationship("User", foreign_keys=[CreatedBy], backref="created_shipping_methods")
    modifier = relationship("User", foreign_keys=[ModifiedBy], backref="modified_shipping_methods")

    def __repr__(self):
        return f"<ShippingMethod(Id={self.ShippingMethodId}, Method='{self.ShippingMethod}')>"