from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class MasterQtyDimTypes(Base):
    __tablename__ = "MasterQtyDimTypes"

    MasterQtyDimTypesId = Column(Integer, primary_key=True, index=True)
    MasterQtyDimTypes = Column(String(500), nullable=False)
    IsDeleted = Column(Boolean, nullable=False, default=False)
    CreatedOn = Column(DateTime, nullable=False, default=datetime.utcnow)
    CreatedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    ModifiedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, default=datetime.utcnow)

    # Relationships
    creator = relationship("User", foreign_keys=[CreatedBy], backref="created_qty_dim_types")
    modifier = relationship("User", foreign_keys=[ModifiedBy], backref="modified_qty_dim_types")

    def __repr__(self):
        return f"<MasterQtyDimTypes(Id={self.MasterQtyDimTypesId}, Name='{self.MasterQtyDimTypes}')>"