from typing import List, Optional

from fastapi import Depends

from src.models.EmployeesUserModel import EmployeeUser

from src.models.EmployeeModel import Employee

from src.repositories.EmployeeRepository import EmployeesRepo

from src.schemas.Employeeschemas import Employee

#from src.schemas.LstEmployeeschemas import lstEmps

class EmployeeService:
    employeeRepository: EmployeesRepo

    def __init__(
        self, employeeRepository: EmployeesRepo = Depends()
    ) -> None:
        self.employeeRepository = employeeRepository

    def fetch_all(self) -> List[Employee]:
        return self.employeeRepository.fetch_all()
    
    def fetch_by_name(self,employeeName) -> None:
        return self.employeeRepository.fetch_by_name(employeeName)
    
    def add_employees(self, employees: List[Employee]) -> str:
        try:
            # Convert list of employee schemas to a list of dictionaries
            employees_data = [employee.dict() for employee in employees]

            # Call your repository method passing the list of dictionaries
            result = self.employeeRepository.add_employee(employees_data)
            
            return result  # Assuming your repository method returns a message
            
        except Exception as e:
            # Log or handle the exception as needed
            print(f"This is service...Error occurred: {e}")
            raise e
    
    def add_employee_users(self, employees: List[Employee],employeeName,dateofBirth) -> str:
        try:
            # Convert list of employee schemas to a list of dictionaries
            employees_data = [employee.dict() for employee in employees]

            # Call your repository method passing the list of dictionaries
            result = self.employeeRepository.add_employee_users(employees_data,employeeName,dateofBirth)
            
            return result  # Assuming your repository method returns a message
            
        except Exception as e:
            # Log or handle the exception as needed
            print(f"This is service...Error occurred: {e}")
            raise e
    
    def add_employee_usersUDT(self, employees: List[EmployeeUser]) -> str:
        try:
            # Convert list of employee schemas to a list of dictionaries
            employees_data = [employee.dict() for employee in employees]

            # Call your repository method passing the list of dictionaries
            result = self.employeeRepository.add_employee_usersUDT(employees_data)
            
            return result  # Assuming your repository method returns a message
            
        except Exception as e:
            # Log or handle the exception as needed
            print(f"This is service...Error occurred: {e}")
            raise e