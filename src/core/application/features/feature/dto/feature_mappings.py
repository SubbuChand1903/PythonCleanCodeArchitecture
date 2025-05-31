from typing import List, Optional
from src.core.application.features.feature.dto.feature_dto import FeatureRead
from src.core.domain.entities.feature.feature import Feature

class FeatureMappings:

    @staticmethod
    def model_to_dto(feature_model: Optional[Feature]) -> Optional[FeatureRead]:
        if feature_model:
            return FeatureRead.model_validate(feature_model)
        return None

    @staticmethod
    def dto_to_model(feature_dto: FeatureRead) -> Feature:
        return Feature(**feature_dto.model_dump())

    @staticmethod
    def model_list_to_dto_list(feature_models: List[Feature]) -> List[FeatureRead]:
        return [FeatureRead.model_validate(model) for model in feature_models]

    @staticmethod
    def dto_list_to_model_list(feature_dtos: List[FeatureRead]) -> List[Feature]:
        return [Feature(**dto.model_dump()) for dto in feature_dtos]
