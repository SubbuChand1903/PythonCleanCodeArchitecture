from distutils import debug
from typing import List, Optional, Tuple
from sqlalchemy import text

from fastapi import Depends
import sqlalchemy
from sqlalchemy.orm import Session, lazyload

from src.configs.db import (
    get_db,
)

from src.models import EmployeeModel

class EmployeesRepo:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db)
    ) -> None:
        self.db = db
 
    def fetch_all(self) -> list[EmployeeModel.Employee]:
     return  self.db.query(EmployeeModel.Employee).all()
 
    def fetch_by_name(self,employeeName):
     return  self.db.query(EmployeeModel.Employee).filter(EmployeeModel.Employee.EmployeeName.like(f'%{employeeName}%')).all()
    
    def add_employee(self, employees: List[dict]) -> str:
     outParam = ""

     try:
            print(employees)
        # Convert list of dictionaries to a list of sequences
            employees_data = [(employee['EmployeeName'], employee['DateOfBirth'], employee['Gender'], employee['CurrentAddress'], employee['PermanentAddress'], employee['City'], employee['Nationality'], employee['PINCode']) for employee in employees]
            
            # Execute the stored procedure with the list of sequences
            self.db.execute('EXEC [dbo].[Usp_insert_CreateEmployee] @UDT_Create_Employee=:employees, @outputresponse=:outputresponse OUTPUT', {'employees': employees_data, 'outputresponse': None})
            self.db.commit()

     except Exception as e:
        print(f"This is add_employee repo...Error occurred: {e}")

     return outParam
    

    def add_employee_usersUDT(self, employeeusers: List[Tuple[int, str, str]]) -> str:
     outParam = ""

     try:
            print(employeeusers)
        # Convert list of dictionaries to a list of sequences
            employees_data = [(employeeuser['EmployeeId'],employeeuser['EmployeeName'], employeeuser['DateOfBirth']) for employeeuser in employeeusers]

            # Execute the stored procedure with the list of sequences
            self.db.execute('EXEC [dbo].[Usp_insert_CreateEmployeeUsersUDT] @UDT_Create_EmployeeUsers=:employees, @outputresponse=:outputresponse OUTPUT', {'employees': employees_data,'outputresponse': None})
            self.db.commit()

     except Exception as e:
        print(f"This is add_employee_users repo...Error occurred: {e}")

     return outParam
    
    def add_employee_users(self, employeeusers: List[Tuple[int, str, str]],employeeName,dateofBirth) -> str:
     outParam = ""

     try:
            print(employeeusers)
        # Convert list of dictionaries to a list of sequences
            employees_data = [(employeeuser['EmployeeName'], employeeuser['DateOfBirth'], employeeuser['Gender'], employeeuser['CurrentAddress'], employeeuser['PermanentAddress'], employeeuser['City'], employeeuser['Nationality'], employeeuser['PINCode']) for employeeuser in employeeusers]

            # Execute the stored procedure with the list of sequences
            self.db.execute('EXEC [dbo].[Usp_insert_CreateEmployeeUsers] @UDT_Create_Employee=:employees, @EmployeeName=:employeeName, @DateOfBirth=:dateofBirth ,@outputresponse=:outputresponse OUTPUT', {'employees': employees_data,'employeeName':employeeName,'dateofBirth':dateofBirth,'outputresponse': None})
            self.db.commit()

     except Exception as e:
        print(f"This is add_employee_users repo...Error occurred: {e}")

     return outParam