from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class OrderType(Base):
    __tablename__ = "OrderType"

    OrderTypeId = Column(Integer, primary_key=True, index=True)
    OrderType = Column(String(500), nullable=False)
    IsDeleted = Column(Boolean, nullable=False, default=False)
    CreatedOn = Column(DateTime, nullable=False, default=datetime.utcnow)
    CreatedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    ModifiedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, default=datetime.utcnow)

    # Relationships
    creator = relationship("User", foreign_keys=[CreatedBy], backref="created_ordertypes")
    modifier = relationship("User", foreign_keys=[ModifiedBy], backref="modified_ordertypes")

    def __repr__(self):
        return f"<OrderType(OrderTypeId={self.OrderTypeId}, OrderType='{self.OrderType}')>"