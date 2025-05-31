from typing import List
from fastapi import HTTPException

from src.core.application.features.feature.dto.feature_dto import FeatureRead
from src.core.application.features.feature.dto.feature_mappings import FeatureMappings
from src.core.domain.interfaces.repositories.feature.ifeature_query_repository import IFeatureQueryRepository
from src.config.infrastructure.exceptions.app_exception import AppException
from src.config.infrastructure.exceptions.database_exception import DatabaseException

class GetFeaturesByDashboardAndModuleQueryService:
    def __init__(self, feature_repository: IFeatureQueryRepository):
        self.feature_repository = feature_repository

    async def get_features_by_dashboard_and_module(
        self, dashboard_id: int, module_id: int, user_id: int
    ) -> List[FeatureRead]:
        try:
            features = await self.feature_repository.get_features_by_dashboard_and_module(
                dashboard_id, module_id, user_id
            )
            return FeatureMappings.model_list_to_dto_list(features)
        except Exception as e:
            print(f"❌ Error in Feature Service: {e}")
            raise e
