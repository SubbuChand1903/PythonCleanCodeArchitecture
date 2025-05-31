from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from src.core.domain.entities.module.module import Module
from src.core.domain.interfaces.repositories.module.imodule_query_repository import IModuleQueryRepository
from src.config.infrastructure.exceptions.app_exception import AppException

class ModuleQueryRepository(IModuleQueryRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_modules_by_dashboard_id(self, dashboard_id: int) -> List[Module]:
        try:
            stmt = text("EXEC [dbo].[usp_GetModulesByDashboardId] :DashboardId")
            result = await self.db.execute(stmt, {"DashboardId": dashboard_id, "UserId": None})
            rows = result.mappings().all()
            return [Module(**row) for row in rows]
        except Exception as e:
            print(f"❌ Error in ModuleQueryRepository: {e}")
            raise AppException(f"Error fetching modules: {e}")
