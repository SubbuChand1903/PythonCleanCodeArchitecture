from fastapi import APIRouter, Depends, HTTPException, status, Query
from dependency_injector.wiring import Provide, inject
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.application.extensions.dependencies import Container

from src.core.application.features.order.dto.search_open_orders.order_query_service import (
    SearchOrdersQueryService
)
from src.core.application.features.order.dto.search_open_orders.order_dto import OpenOrderDTO
from src.core.application.responsemodels.message_response import MessageResponse

open_order_router = APIRouter(prefix="/rest/open", tags=["open Orders"])

@open_order_router.get("/test")
@inject
async def test():
    print("Test route hit!")
    return {"message": "Test route is working"}


@open_order_router.get("/search", response_model=Optional[List[OpenOrderDTO]])
@inject
async def search_orders(
    search_string: str = Query(..., description="Search term for orders"),
    user_id: int = Query(..., description="User ID for access control"),
    order_service: SearchOrdersQueryService = Depends(
        Provide[Container.search_open_order_service]
    )
):
    try:
        response = await order_service.search_orders(search_string, user_id)
        return response
    except Exception as e:
        print(f"❌ Error during search_orders: {e}")
        raise HTTPException(status_code=500, detail=str(e))