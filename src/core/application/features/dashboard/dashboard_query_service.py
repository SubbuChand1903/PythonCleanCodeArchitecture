from typing import List, Optional

from fastapi import HTTPException
from src.core.application.features.dashboard.dto.dashboard_dto import DashboardRead
from src.core.application.features.dashboard.dto.dashboard_mappings import DashboardMappings
from src.core.domain.entities.dashboard.dashboard import Dashboard
from src.core.domain.interfaces.repositories.dashboard.idashboard_query_repository import IDashboardQueryRepository
from src.config.infrastructure.exceptions.app_exception import AppException
from src.config.infrastructure.exceptions.database_exception import DatabaseException   

class GetAllDashboardsQueryService:
    def __init__(self, dashboard_repository: IDashboardQueryRepository):
        self.dashboard_repository = dashboard_repository

    async def get_all_dashboards(self) -> List[DashboardRead]:
        try:
            dashboards : List[Dashboard] = await self.dashboard_repository.get_all_dashboards()      
            result: List[DashboardRead] = DashboardMappings.model_list_to_dto_list(dashboards)  
            return result
        except Exception as e:                
                print(f"In Dashboard Service - Exception Occured: {e}")  # Log the error
                raise  e # Re-raise the exception (or handle as needed)