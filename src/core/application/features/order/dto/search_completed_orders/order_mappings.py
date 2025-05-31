from typing import List
from src.core.application.features.order.dto.search_completed_orders.order_dto import CompletedOrderDTO
from src.core.domain.entities.order.search_completed_orders.order import CompletedOrder

class OrderMappings:

    @staticmethod
    def model_to_dto(order_model: CompletedOrder) -> CompletedOrderDTO:
        if order_model:
            return CompletedOrderDTO.model_validate(order_model)
        return None

    @staticmethod
    def dto_to_model(order_dto: CompletedOrderDTO) -> CompletedOrder:
        return CompletedOrder(**order_dto.model_dump())

    @staticmethod
    def model_list_to_dto_list(order_models: List[CompletedOrder]) -> List[CompletedOrderDTO]:
        return [CompletedOrderDTO.model_validate(model) for model in order_models]

    @staticmethod
    def dto_list_to_model_list(order_dtos: List[CompletedOrderDTO]) -> List[CompletedOrder]:
        return [CompletedOrder(**dto.model_dump()) for dto in order_dtos]