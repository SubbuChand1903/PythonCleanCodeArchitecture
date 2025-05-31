from typing import List, Optional
from src.core.application.features.module.dto.module_dto import ModuleRead
from src.core.domain.entities.module.module import Module

class ModuleMappings:

    @staticmethod
    def model_to_dto(module_model: Optional[Module]) -> Optional[ModuleRead]:
        if module_model:
            return ModuleRead.model_validate(module_model)
        return None

    @staticmethod
    def dto_to_model(module_dto: ModuleRead) -> Module:
        return Module(**module_dto.model_dump())

    @staticmethod
    def model_list_to_dto_list(module_models: List[Module]) -> List[ModuleRead]:
        return [ModuleRead.model_validate(model) for model in module_models]

    @staticmethod
    def dto_list_to_model_list(module_dtos: List[ModuleRead]) -> List[Module]:
        return [Module(**dto.model_dump()) for dto in module_dtos]