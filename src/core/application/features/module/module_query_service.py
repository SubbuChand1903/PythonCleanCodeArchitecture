from typing import List, Optional

from fastapi import HTTPException
from src.core.application.features.module.dto.module_dto import ModuleRead
from src.core.application.features.module.dto.module_mappings import ModuleMappings
from src.core.domain.entities.module.module import Module
from src.core.domain.interfaces.repositories.module.imodule_query_repository import IModuleQueryRepository
from src.config.infrastructure.exceptions.app_exception import AppException
from src.config.infrastructure.exceptions.database_exception import DatabaseException   

class GetModulesByDashboardQueryService:
    def __init__(self, module_repository: IModuleQueryRepository):
        self.module_repository = module_repository

    async def get_modules_by_dashboard_id(self, dashboard_id: int) -> List[ModuleRead]:
        try:
            modules = await self.module_repository.get_modules_by_dashboard_id(dashboard_id)
            return ModuleMappings.model_list_to_dto_list(modules)
        except Exception as e:
            print(f"❌ Error in service: {e}")
            raise e