from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.domain.entities.order.search_completed_orders.order import CompletedOrder

class IOrderQueryRepository(ABC):

    @abstractmethod
    async def search_orders(self, search_string: str, user_id: int) -> List[CompletedOrder]:
        """Fetch all order from the database."""
        pass