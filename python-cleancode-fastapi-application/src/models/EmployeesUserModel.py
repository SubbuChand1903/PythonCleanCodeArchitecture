from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime
 
from src.configs.db import Base
#from src.models.EmployeeModel import EmployeeModell
   
class EmployeeUser(Base):
    __tablename__ = "EmployeesUsers"
    __table_args__ = {"schema": "dbo"}
    
    EmployeesUsersId = Column(Integer, primary_key=True,index=True, nullable=False)
    EmployeeId = Column(Integer, ForeignKey('Employees.EmployeeId'))
    EmployeeName = Column(String(255), nullable=True)
    DateOfBirth = Column(String(255), nullable=True)

    #Employee = relationship("Employee", back_populates="Employees")