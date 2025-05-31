from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from datetime import date
from typing import Self, List
 
class EmployeeDTO(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    email: EmailStr
    department: str
    salary: float
    hire_date: date

    class Config:
        from_attributes = True  # Enables ORM support (formerly orm_mode=True)
 
class EmployeeCreateUpdate(EmployeeDTO):
    @field_validator('salary')
    @classmethod
    def validate_salary(cls, v: float) -> float:
        if v < 0:
            raise ValueError("Salary must be non-negative")
        return v
 
    @field_validator('department')
    @classmethod
    def validate_department(cls, v: str) -> str:
        allowed_departments = {'HR', 'Engineering', 'Sales', 'Marketing'}
        if v not in allowed_departments:
            raise ValueError(f"Department must be one of: {allowed_departments}")
        return v
 
    @model_validator(mode="after")
    def validate_hire_date(self) -> Self:
        if self.hire_date > date.today():
            raise ValueError("Hire date cannot be in the future")
        return self
 
class EmployeeRead(EmployeeDTO):
    employee_id: int
 
    class Config:
        from_attributes = True
 
class EmployeesBulkCreateUpdate(BaseModel):
    employees: List[EmployeeCreateUpdate]
 
class EmployeeDeleteRequest(BaseModel):
    employee_id: int