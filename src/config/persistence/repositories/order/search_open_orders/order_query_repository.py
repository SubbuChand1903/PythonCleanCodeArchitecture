from typing import List, Optional
from sqlalchemy import asc, desc, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.infrastructure.exceptions.app_exception import AppException
from src.core.domain.entities.order.search_open_orders.order import OpenOrder
from src.core.domain.interfaces.repositories.order.search_open_orders.iorder_query_repository import IOrderQueryRepository

class OrderQueryRepository(IOrderQueryRepository):

    def __init__(self, db: AsyncSession):
        self.db = db

    async def search_orders(self, search_string: str, user_id: int) -> List[OpenOrder]:
        try:
            query = text("""
                EXEC dbo.usp_SearchOpenOrders
                    @SearchString = :search_string,
                    @UserId = :user_id
            """)

            result = await self.db.execute(query, {
                "search_string": search_string,
                "user_id": user_id
            })

            rows = result.fetchall()
            orders = [OpenOrder(**dict(row._mapping)) for row in rows]
            return orders

        except Exception as e:
            print(f"In Order Repository - Exception during search_orders: {e}")
            raise AppException(f"Error searching orders: {str(e)}")