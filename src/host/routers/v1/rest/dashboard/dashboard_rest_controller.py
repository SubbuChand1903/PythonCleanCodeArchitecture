from fastapi import APIRouter, Depends, HTTPException, status, Query
from dependency_injector.wiring import Provide, inject
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.application.extensions.dependencies import Container

from src.core.application.features.dashboard.dashboard_query_service import (
    GetAllDashboardsQueryService
)
from src.core.application.features.dashboard.dto.dashboard_dto import DashboardRead
from src.core.application.responsemodels.message_response import MessageResponse

dashboard_router = APIRouter(prefix="/rest/dashboard", tags=["Dashboards"])


@dashboard_router.get("/test")
@inject
async def test():
    print("Test route hit!")
    return {"message": "Test route is working"}


@dashboard_router.get("/", response_model=Optional[List[DashboardRead]])
@inject
async def get_all_dashboards(
    dashboard_service: GetAllDashboardsQueryService = Depends(
        Provide[Container.get_all_dashboard_service]
    )
):
    print("🔍 dashboard:", type(dashboard_service))  # <-- ADD THIS LINE
    try:
        response = await dashboard_service.get_all_dashboards()
        return response
    except Exception as e:
        print(f"Error during get_all_dashboards: {e}")
        raise HTTPException(status_code=500, detail=str(e))