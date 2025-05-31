from typing import List
from src.core.application.features.order.dto.search_open_orders.order_dto import OpenOrderDTO
from src.core.domain.entities.order.search_open_orders.order import OpenOrder

class OrderMappings:

    @staticmethod
    def model_to_dto(order_model: OpenOrder) -> OpenOrderDTO:
        if order_model:
            return OpenOrderDTO.model_validate(order_model)
        return None

    @staticmethod
    def dto_to_model(order_dto: OpenOrderDTO) -> OpenOrder:
        return OpenOrder(**order_dto.model_dump())

    @staticmethod
    def model_list_to_dto_list(order_models: List[OpenOrder]) -> List[OpenOrderDTO]:
        return [OpenOrderDTO.model_validate(model) for model in order_models]

    @staticmethod
    def dto_list_to_model_list(order_dtos: List[OpenOrderDTO]) -> List[OpenOrder]:
        return [OpenOrder(**dto.model_dump()) for dto in order_dtos]