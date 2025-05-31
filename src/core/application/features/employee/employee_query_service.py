from typing import List, Optional

from fastapi import HTTPException
from src.core.application.features.employee.dto.employee_dto import EmployeeDTO
from src.core.application.features.employee.dto.employee_mappings import EmployeeMappings
from src.core.domain.entities.employee.employee import Employee
from src.core.domain.interfaces.repositories.employee.iemployee_query_repository import IEmployeeQueryRepository
from src.config.infrastructure.exceptions.app_exception import AppException
from src.config.infrastructure.exceptions.database_exception import DatabaseException   

class GetAllEmployeesQueryService:
    def __init__(self, employee_repository: IEmployeeQueryRepository):
        self.employee_repository = employee_repository

    async def get_all_employees(self) -> List[EmployeeDTO]:
        try:
            employees : List[Employee] = await self.employee_repository.get_all_employees()      
            result: List[EmployeeDTO] = EmployeeMappings.model_list_to_dto_list(employees)  
            return result
        except Exception as e:                
                print(f"In Employee Service - Exception Occured: {e}")  # Log the error
                raise  e # Re-raise the exception (or handle as needed)   
        
class GetEmployeeByIdQueryService:
    def __init__(self, employee_repository: IEmployeeQueryRepository):
        self.employee_repository = employee_repository

    async def get_employee_by_id(self, employeeid : int) -> EmployeeDTO:
        try:
            employee : Employee = await self.employee_repository.get_employee_by_id(employeeid)
            if not employee:  
                raise AppException(f"Employee with id number {employeeid} is not found")
            return EmployeeMappings.model_to_dto(employee)  
       
        except Exception as e:                
                print(f"In Employee Service - Exception Occured: {e}")  # Log the error
                raise  e # Re-raise the exception (or handle as needed)

class GetAllEmployeesODataQueryService:
    def __init__(self, employee_repository: IEmployeeQueryRepository):
        self.employee_repository = employee_repository

    async def get_all_employees_odata(
        self,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        orderby: Optional[str] = None,
        filter_: Optional[str] = None,
        count: Optional[bool] = False
    ) -> List[EmployeeDTO]:
        try:
            employees: List[Employee] = await self.employee_repository.get_employees_odata(
                top=top,
                skip=skip,
                orderby=orderby,
                filter_=filter_,
                count=count
            )
            result: List[EmployeeDTO] = EmployeeMappings.model_list_to_dto_list(employees)
            return result
        except Exception as e:
            print(f"In Employee OData Service - Exception occurred: {e}")
            raise e

