from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class OrderStatus(Base):
    __tablename__ = "OrderStatus"

    OrderStatusId = Column(Integer, primary_key=True, index=True)
    OrderStatus = Column(String(255), nullable=False)
    IsDeleted = Column(Boolean, nullable=False, default=False)
    CreatedOn = Column(DateTime, nullable=False, default=datetime.utcnow)
    CreatedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    ModifiedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, default=datetime.utcnow)

    # Relationships
    creator = relationship("User", foreign_keys=[CreatedBy], backref="created_order_statuses")
    modifier = relationship("User", foreign_keys=[ModifiedBy], backref="modified_order_statuses")

    def __repr__(self):
        return f"<OrderStatus(OrderStatusId={self.OrderStatusId}, Status='{self.OrderStatus}')>"
