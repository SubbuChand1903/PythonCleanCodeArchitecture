from fastapi import APIRouter, Depends, HTTPException, Query
from dependency_injector.wiring import Provide, inject
from typing import List

from src.core.application.extensions.dependencies import Container
from src.core.application.features.feature.feature_query_service import GetFeaturesByDashboardAndModuleQueryService
from src.core.application.features.feature.dto.feature_dto import FeatureRead

feature_router = APIRouter(prefix="/rest/feature", tags=["Features"])

@feature_router.get("/test")
@inject
async def test():
    print("✅ Feature test route hit!")
    return {"message": "Feature test route is working"}

@feature_router.get("/", response_model=List[FeatureRead])
@inject
async def get_features_by_dashboard_and_module(
    dashboard_id: int = Query(..., description="Dashboard ID to filter features"),
    module_id: int = Query(..., description="Module ID to filter features"),
    user_id: int = Query(..., description="User ID for logging/audit"),
    feature_service: GetFeaturesByDashboardAndModuleQueryService = Depends(
        Provide[Container.get_features_by_dashboard_and_module_service]
    )
):
    try:
        return await feature_service.get_features_by_dashboard_and_module(dashboard_id, module_id, user_id)
    except Exception as e:
        print(f"❌ Error in feature controller: {e}")
        raise HTTPException(status_code=500, detail=str(e))
