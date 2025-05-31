from typing import List, Optional

from fastapi import HTTPException
from src.core.application.features.order.dto.search_completed_orders.order_dto import CompletedOrderDTO
from src.core.application.features.order.dto.search_completed_orders.order_mappings import OrderMappings
from src.core.domain.entities.order.search_completed_orders.order import CompletedOrder
from src.core.domain.interfaces.repositories.order.search_completed_orders.iorder_query_repository import IOrderQueryRepository
from src.config.infrastructure.exceptions.app_exception import AppException
from src.config.infrastructure.exceptions.database_exception import DatabaseException   

class SearchOrdersQueryService:
    def __init__(self, order_repository: IOrderQueryRepository):
        self.order_repository = order_repository

    async def search_orders(self, search_string: str, user_id: int) -> List[CompletedOrderDTO]:
        try:
            orders: List[CompletedOrder] = await self.order_repository.search_orders(search_string, user_id)
            result: List[CompletedOrderDTO] = OrderMappings.model_list_to_dto_list(orders)
            return result
        except Exception as e:
            print(f"In Order Service - Exception occurred during search_orders: {e}")
            raise e

