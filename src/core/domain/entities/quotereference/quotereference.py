from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class QuoteReference(Base):
    __tablename__ = "QuoteReference"

    QuoteReferenceId = Column(Integer, primary_key=True, index=True)
    QuoteNumber = Column(String(50), nullable=True)
    QuoteNumberSalesforceId = Column(String(18), nullable=True)
    Opportunity = Column(String(255), nullable=False)
    OpportunitySalesforceId = Column(String(18), nullable=False)
    EffectiveDate = Column(DateTime, nullable=True)
    ExpirationDate = Column(DateTime, nullable=True)
    IsDeleted = Column(Boolean, nullable=False, default=False)
    CreatedOn = Column(DateTime, nullable=False, default=datetime.utcnow)
    CreatedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    ModifiedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, default=datetime.utcnow)

    # Relationships
    creator = relationship("User", foreign_keys=[CreatedBy], backref="created_quote_references")
    modifier = relationship("User", foreign_keys=[ModifiedBy], backref="modified_quote_references")

    def __repr__(self):
        return f"<QuoteReference(Id={self.QuoteReferenceId}, QuoteNumber='{self.QuoteNumber}', Opportunity='{self.Opportunity}')>"