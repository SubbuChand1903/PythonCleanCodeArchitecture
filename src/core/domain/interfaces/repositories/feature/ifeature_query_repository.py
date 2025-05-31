from abc import ABC, abstractmethod
from typing import List
from src.core.domain.entities.feature.feature import Feature

class IFeatureQueryRepository(ABC):

    @abstractmethod
    async def get_features_by_dashboard_and_module(
        self, dashboard_id: int, module_id: int, user_id: int
    ) -> List[Feature]:
        """Fetch all Features for the given dashboard and module from the database"""
        pass
