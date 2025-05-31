from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from src.core.domain.entities.feature.feature import Feature
from src.core.domain.interfaces.repositories.feature.ifeature_query_repository import IFeatureQueryRepository
from src.config.infrastructure.exceptions.app_exception import AppException

class FeatureQueryRepository(IFeatureQueryRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_features_by_dashboard_and_module(self, dashboard_id: int, module_id: int, user_id: int) -> List[Feature]:
        try:
            stmt = text("EXEC [dbo].[usp_GetFeaturesByDashboardAndModule] :DashboardId, :ModuleId")
            result = await self.db.execute(stmt, {
                "DashboardId": dashboard_id,
                "ModuleId": module_id,
                "UserId": None
            })
            rows = result.mappings().all()
            return [Feature(**row) for row in rows]
        except Exception as e:
            print(f"❌ Error in FeatureQueryRepository: {e}")
            raise AppException(f"Error fetching features: {e}")
