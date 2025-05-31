from typing import List, Optional
from src.core.application.features.dashboard.dto.dashboard_dto import DashboardRead
from src.core.domain.entities.dashboard.dashboard import Dashboard

class DashboardMappings:

    @staticmethod
    def model_to_dto(dashboard_model: Optional[Dashboard]) -> Optional[DashboardRead]:
        if dashboard_model:
            return DashboardRead.model_validate(dashboard_model)
        return None

    @staticmethod
    def dto_to_model(dashboard_dto: DashboardRead) -> Dashboard:
        return Dashboard(**dashboard_dto.model_dump())

    @staticmethod
    def model_list_to_dto_list(dashboard_models: List[Dashboard]) -> List[DashboardRead]:
        return [DashboardRead.model_validate(model) for model in dashboard_models]

    @staticmethod
    def dto_list_to_model_list(dashboard_dtos: List[DashboardRead]) -> List[Dashboard]:
        return [Dashboard(**dto.model_dump()) for dto in dashboard_dtos]