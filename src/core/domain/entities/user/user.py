from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
Base = declarative_base()
class User(Base):
    __tablename__ = "Users"

    UserId = Column(Integer, primary_key=True, index=True)
    EmailAddress = Column(String(500), unique=True, nullable=False)
    FirstName = Column(String(500), nullable=False)
    LastName = Column(String(500), nullable=False)
    IsValid = Column(Boolean, nullable=False, default=False)
    AliasName = Column(String(50), nullable=False)
    IsDeleted = Column(Boolean, nullable=False, default=False)
    CreatedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=False)
    CreatedOn = Column(DateTime, nullable=False, default=datetime.utcnow)
    ModifiedBy = Column(Integer, ForeignKey("Users.UserId"), nullable=True)
    ModifiedOn = Column(DateTime, nullable=True, default=datetime.utcnow)

    # Self-referencing relationships (optional)
    creator = relationship("User", remote_side=[UserId], foreign_keys=[CreatedBy], backref="created_users")
    modifier = relationship("User", remote_side=[UserId], foreign_keys=[ModifiedBy], backref="modified_users")

    def __repr__(self):
        return f"<User(UserId={self.UserId}, Email='{self.EmailAddress}')>"