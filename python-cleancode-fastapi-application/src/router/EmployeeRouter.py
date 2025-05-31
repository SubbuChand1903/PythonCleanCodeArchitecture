from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status

import src.schemas.Employeeschemas as Employeeschemas

import src.schemas.EmployeesUserModelschemas as EmployeesUserschemas

from src.services.EmployeeService import EmployeeService

EmployeeRouter = APIRouter(
    prefix="/Employees", tags=["Employees"]
)

@EmployeeRouter.get("/GetAllEmployees", response_model=list[Employeeschemas.Employee])
def get_all_employees(employeeService: EmployeeService = Depends()):
    try:
        employees = []
        db_employee = employeeService.fetch_all()

        if db_employee:
            return db_employee
        else:
            return employees
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@EmployeeRouter.get("/GetSimilarEmployees")
def get_similar_employees(employeeName,employeeService: EmployeeService = Depends()):
    try:
        employees =[]
        db_employee = employeeService.fetch_by_name(employeeName)
        employees.append(db_employee)
        return employees
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@EmployeeRouter.post("/SubmitEmployees",status_code=status.HTTP_201_CREATED)
def add_employees(lst_employee_schemas: list[Employeeschemas.Employee],employeeService: EmployeeService = Depends()):
    try:
        result  = employeeService.add_employees(lst_employee_schemas)
        return result 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@EmployeeRouter.post("/SubmitEmployeeUsers",status_code=status.HTTP_201_CREATED)
def add_employees(lst_employee_schemas: list[Employeeschemas.Employee],emp_name,dob,employeeService: EmployeeService = Depends()):
    try:
        result  = employeeService.add_employee_users(lst_employee_schemas,emp_name,dob)
        return result 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@EmployeeRouter.post("/SubmitEmployeeUsersUDT",status_code=status.HTTP_201_CREATED)
def add_employees(lst_employee_schemas: list[EmployeesUserschemas.EmployeeUser],employeeService: EmployeeService = Depends()):
    try:
        result  = employeeService.add_employee_usersUDT(lst_employee_schemas)
        return result 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))