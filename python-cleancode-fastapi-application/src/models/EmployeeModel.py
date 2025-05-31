from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
 
from src.configs.db import Base
   
class Employee(Base):
    __tablename__ = "Employees"
    __table_args__ = {"schema": "dbo"}
 
    EmployeeId = Column(Integer, primary_key=True,index=True, nullable=False)
    EmployeeName = Column(String(255), nullable=True)
    DateOfBirth = Column(String(255), nullable=True)
    Gender = Column(String(255), nullable=True)
    CurrentAddress = Column(String(255), nullable=True)
    PermanentAddress = Column(String(255), nullable=True)
    City = Column(String(255), nullable=True)
    Nationality = Column(String(255), nullable=True)
    PINCode = Column(String(255), nullable=True)

    EmployeeUser = relationship("EmployeeUser", back_populates="EmployeesUsers")