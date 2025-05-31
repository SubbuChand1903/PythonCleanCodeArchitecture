from pickle import TRUE
from typing import List, Optional
 
from pydantic import BaseModel, ConfigDict, validator
 
class EmployeeUsersBase(BaseModel):
    EmployeeId : int
    EmployeeName: str
    DateOfBirth: str

    # @validator("EmployeeName")
    # @classmethod
    # def validate_name(cls, value):
       
    #     if len(value) < 3:
    #         raise ValueError("EmployeeName must be at least 3 characters long")
    #     return value
 
class EmployeeUsersCreate(EmployeeUsersBase):
    pass
 
class EmployeeUser(EmployeeUsersBase):
 
    class Config:
        orm_mode = True
        model_config = ConfigDict(from_attributes=True)
        