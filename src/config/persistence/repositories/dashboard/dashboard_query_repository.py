from typing import List, Optional
from sqlalchemy import asc, desc, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.infrastructure.exceptions.app_exception import AppException
from src.core.domain.entities.dashboard.dashboard import Dashboard
from src.core.domain.interfaces.repositories.dashboard.idashboard_query_repository import IDashboardQueryRepository


class DashboardQueryRepository(IDashboardQueryRepository):

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_dashboards(self) -> List[Dashboard]:
        try:
            stmt = text("EXEC [dbo].[usp_GetAllDashboards] :UserId")
            result = await self.db.execute(stmt, {"UserId": None})
            rows = result.mappings().all()
            print(rows)
            dashboards = [Dashboard(**row) for row in rows]
            return dashboards

        except Exception as e:
            print(f"In Dashboard Repository - Exception during get_all_dashboards: {e}")
            raise AppException(f"Error fetching dashboards: {str(e)}")
