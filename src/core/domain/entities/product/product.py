from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Product(Base):
    __tablename__ = "Product"

    ProductId = Column(Integer, primary_key=True, index=True)
    ProductName = Column(String(100), nullable=False)
    ProductNameSalesforceId = Column(String(18), nullable=False)
    Description = Column(String(500), nullable=True)
    PatternNo = Column(String(50), nullable=True)
    Face1 = Column(String(50), nullable=True)
    Adhesive1 = Column(String(50), nullable=True)
    Liner1 = Column(String(50), nullable=True)
    Adhesive2 = Column(String(50), nullable=True)
    Liner2 = Column(String(50), nullable=True)
    IsDeleted = Column(Boolean, nullable=False, default=False)
    CreatedOn = Column(DateTime, nullable=False, default=datetime.utcnow)
    CreatedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    ModifiedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, default=datetime.utcnow)

    # Relationships (optional)
    creator = relationship("User", foreign_keys=[CreatedBy], backref="created_products")
    modifier = relationship("User", foreign_keys=[ModifiedBy], backref="modified_products")

    def __repr__(self):
        return f"<Product(ProductId={self.ProductId}, ProductName='{self.ProductName}')>"