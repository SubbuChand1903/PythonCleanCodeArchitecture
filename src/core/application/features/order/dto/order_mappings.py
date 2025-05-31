from typing import List
from src.core.application.features.order.dto.order_dto import OrderDTO
from src.core.domain.entities.order.order import Order

class OrderMappings:

    @staticmethod
    def model_to_dto(order_model: Order) -> OrderDTO:
        if order_model:
            return OrderDTO.model_validate(order_model)
        return None

    @staticmethod
    def dto_to_model(order_dto: OrderDTO) -> Order:
        return Order(**order_dto.model_dump())

    @staticmethod
    def model_list_to_dto_list(order_models: List[Order]) -> List[OrderDTO]:
        return [OrderDTO.model_validate(model) for model in order_models]

    @staticmethod
    def dto_list_to_model_list(order_dtos: List[OrderDTO]) -> List[Order]:
        return [Order(**dto.model_dump()) for dto in order_dtos]