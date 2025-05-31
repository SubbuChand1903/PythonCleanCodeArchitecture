from fastapi import Depends
from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.persistence.context.database_context import get_db_async
from src.config.persistence.repositories.employee.employee_query_repository import EmployeeQueryRepository
from src.config.persistence.repositories.dashboard.dashboard_query_repository import DashboardQueryRepository
from src.config.persistence.repositories.module.module_query_repository import ModuleQueryRepository
from src.config.persistence.repositories.feature.feature_query_repository import FeatureQueryRepository
from src.config.persistence.repositories.employee.employee_command_repository import EmployeeCommandRepository

from src.config.persistence.repositories.order.search_completed_orders.order_query_repository import OrderQueryRepository
from src.config.persistence.repositories.order.search_open_orders.order_query_repository import OrderQueryRepository as OpenOrderQueryRepository

from src.config.persistence.repositories.dashboard.dashboard_query_repository import DashboardQueryRepository


class RepositoryContainer(containers.DeclarativeContainer):
    """Container for repository layer dependencies."""

    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.host.routers.v1.rest.employee.employee_rest_controller",
            "src.host.routers.v1.odata.employee.employee_odata_controller"
        ]
    )

    db_session: providers.Resource[AsyncSession] = providers.Resource(get_db_async)

    employee_command_repository = providers.Factory(
        EmployeeCommandRepository,
        db=db_session
    )

    employee_query_repository = providers.Factory(
        EmployeeQueryRepository,
        db=db_session
    )
    
    module_query_repository = providers.Factory(
        ModuleQueryRepository,
        db=db_session
    )

    feature_query_repository = providers.Factory(
        FeatureQueryRepository,
        db=db_session
    )

    employee_query_repository = providers.Factory(
        EmployeeQueryRepository,
        db=db_session
    )

    order_query_repository = providers.Factory(
        OrderQueryRepository,
        db=db_session
    )

    open_order_query_repository = providers.Factory(
        OpenOrderQueryRepository,
        db=db_session
    )


# Optional: direct instantiation and global wire
repository_container = RepositoryContainer()
repository_container.wire(modules=[__name__])


# Optional async getter for FastAPI Depends() if used manually
async def get_db() -> AsyncSession:
    async for db in get_db_async():
        yield db
