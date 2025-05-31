from fastapi import APIRouter, Depends, HTTPException, Query
from dependency_injector.wiring import inject, Provide
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.persistence.context.database_context import get_db_async
from src.core.application.extensions.dependencies import Container
from src.core.application.features.employee.employee_query_service import GetAllEmployeesODataQueryService
from src.core.application.features.employee.dto.employee_dto import EmployeeDTO

employee_router = APIRouter(prefix="/odata/employees", tags=["Employees"])

@employee_router.get("/health")
async def test():
    return {"message": "OData test route is working!"}


@employee_router.get("/", response_model=List[EmployeeDTO])
@inject
async def get_all_employees_odata(
    top: Optional[int] = Query(None, alias="$top"),
    skip: Optional[int] = Query(None, alias="$skip"),
    orderby: Optional[str] = Query(None, alias="$orderby"),
    filter_: Optional[str] = Query(None, alias="$filter"),
    count: Optional[bool] = Query(False, alias="$count"),
    db: AsyncSession = Depends(get_db_async),
    employee_service: GetAllEmployeesODataQueryService = Depends(
        Provide[Container.get_all_employee_odata_service]
    )
):
    try:
        result = await employee_service.get_all_employees_odata(
            top=top,
            skip=skip,
            orderby=orderby,
            filter_=filter_,
            count=count
        )
        return result
    except Exception as e:
        print(f"Error in get_all_employees_odata: {e}")
        raise HTTPException(status_code=500, detail=str(e))