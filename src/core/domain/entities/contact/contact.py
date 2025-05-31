from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Contact(Base):
    __tablename__ = "Contact"

    ContactId = Column(Integer, primary_key=True, index=True)
    CustomerId = Column(Integer, ForeignKey("Customer.CustomerId"), nullable=False)
    ContactName = Column(String(255), nullable=False)
    ContactNamesalesforceId = Column(String(18), nullable=False)
    PhoneNumber = Column(String(14), nullable=False)
    Fax = Column(String(14), nullable=True)
    IsDeleted = Column(Boolean, nullable=False, default=False)
    CreatedOn = Column(DateTime, nullable=False, default=datetime.utcnow)
    CreatedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    ModifiedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, default=datetime.utcnow)

    # Relationships
    customer = relationship("Customer", backref="contacts")
    creator = relationship("User", foreign_keys=[CreatedBy], backref="created_contacts")
    modifier = relationship("User", foreign_keys=[ModifiedBy], backref="modified_contacts")

    def __repr__(self):
        return f"<Contact(ContactId={self.ContactId}, ContactName='{self.ContactName}')>"