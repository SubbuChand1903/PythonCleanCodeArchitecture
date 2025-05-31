from pickle import TRUE
from typing import List, Optional
 
from pydantic import BaseModel, ConfigDict, validator
 
class EmployeeBase(BaseModel):
    EmployeeName: str
    DateOfBirth: str
    Gender: str
    CurrentAddress: str
    PermanentAddress: str
    City: str
    Nationality: str
    PINCode: str

    # @validator("EmployeeName")
    # @classmethod
    # def validate_name(cls, value):
       
    #     if len(value) < 3:
    #         raise ValueError("EmployeeName must be at least 3 characters long")
    #     return value
 
class EmployeesCreate(EmployeeBase):
    pass
 
class Employee(EmployeeBase):
 
    class Config:
        orm_mode = True
        model_config = ConfigDict(from_attributes=True)
        