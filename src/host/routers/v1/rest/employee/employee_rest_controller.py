from fastapi import APIRouter, Depends, HTTPException, status, Query
from dependency_injector.wiring import Provide, inject
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.application.extensions.dependencies import Container
from src.core.application.features.employee.employee_command_service import (
    BulkUpsertEmployeesService,
    DeleteEmployeeService
)
from src.core.application.features.employee.employee_query_service import (
    GetAllEmployeesQueryService,
    GetEmployeeByIdQueryService
)
from src.core.application.features.employee.dto.employee_dto import EmployeeDTO, EmployeesBulkCreateUpdate
from src.core.application.responsemodels.message_response import MessageResponse

employee_router = APIRouter(prefix="/rest/employees", tags=["Employees"])


@employee_router.get("/test")
@inject
async def test():
    print("Test route hit!")
    return {"message": "Test route is working"}


@employee_router.get("/{employee_id}", response_model=Optional[EmployeeDTO])
@inject
async def get_employee_by_id(
    employee_id: int,
    employee_service: GetEmployeeByIdQueryService = Depends(
        Provide[Container.get_employee_by_id_service]
    )
):
    try:
        response = await employee_service.get_employee_by_id(employee_id)
        return response
    except Exception as e:
        print(f"Error during employee_service.get_employee_by_id: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@employee_router.get("/", response_model=Optional[List[EmployeeDTO]])
@inject
async def get_all_employees(
    employee_service: GetAllEmployeesQueryService = Depends(
        Provide[Container.get_all_employee_service]
    )
):
    print("🔍 employee_service:", type(employee_service))  # <-- ADD THIS LINE
    try:
        response = await employee_service.get_all_employees()
        return response
    except Exception as e:
        print(f"Error during get_all_employees: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@employee_router.post("/bulkupsert", response_model=MessageResponse, status_code=status.HTTP_200_OK)
@inject
async def bulk_update_employees(
    payload: EmployeesBulkCreateUpdate,
    employee_service: BulkUpsertEmployeesService = Depends(
        Provide[Container.bulkupsert_employee_service]
    )
):
    try:
        response = await employee_service.bulk_upsert_employees(payload.employees)
        print("Bulk upsert successful")
        return response
    except Exception as e:
        print(f"Error during bulk upsert: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@employee_router.delete("/", response_model=MessageResponse, status_code=status.HTTP_200_OK)
@inject
async def delete_employee_by_id(
    employee_id: int,
    employee_service: DeleteEmployeeService = Depends(
        Provide[Container.delete_employee_service]
    )
):
    try:
        response = await employee_service.delete_employee_by_id(employee_id)
        print(f"Deleted employee with ID {employee_id}")
        return response
    except Exception as e:
        print(f"Error during delete by ID: {e}")
        raise HTTPException(status_code=500, detail=str(e))