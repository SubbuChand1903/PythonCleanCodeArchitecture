from fastapi import APIRouter, Depends, HTTPException, Query
from dependency_injector.wiring import Provide, inject
from typing import List
from src.core.application.extensions.dependencies import Container
from src.core.application.features.module.module_query_service import GetModulesByDashboardQueryService
from src.core.application.features.module.dto.module_dto import ModuleRead

module_router = APIRouter(prefix="/rest/module", tags=["Modules"])

@module_router.get("/test")
@inject
async def test():
    print("✅ Module test route hit!")
    return {"message": "Module test route is working"}

@module_router.get("/", response_model=List[ModuleRead])
@inject
async def get_modules_by_dashboard_id(
    dashboard_id: int = Query(..., description="Dashboard ID to filter modules"),
    module_service: GetModulesByDashboardQueryService = Depends(
        Provide[Container.get_modules_by_dashboard_service]
    )
):
    try:
        return await module_service.get_modules_by_dashboard_id(dashboard_id)
    except Exception as e:
        print(f"❌ Error in controller: {e}")
        raise HTTPException(status_code=500, detail=str(e))
