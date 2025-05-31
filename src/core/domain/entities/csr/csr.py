from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class CSR(Base):
    __tablename__ = "CSR"

    CSRId = Column(Integer, primary_key=True, index=True)
    CSR = Column(String(10), nullable=False)
    IsDeleted = Column(Boolean, nullable=False, default=False)
    CreatedOn = Column(DateTime, nullable=False, default=datetime.utcnow)
    CreatedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    ModifiedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, default=datetime.utcnow)

    # Relationships
    creator = relationship("User", foreign_keys=[CreatedBy], backref="created_csrs")
    modifier = relationship("User", foreign_keys=[ModifiedBy], backref="modified_csrs")

    def __repr__(self):
        return f"<CSR(CSRId={self.CSRId}, CSR='{self.CSR}')>"