from fastapi import Depends
from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

# Query & Command Services
from src.core.application.features.employee.employee_query_service import (
    GetAllEmployeesQueryService,
    GetEmployeeByIdQueryService,
    GetAllEmployeesODataQueryService
)

from src.core.application.features.module.module_query_service import (
    GetModulesByDashboardQueryService
)

from src.core.application.features.feature.feature_query_service import (
    GetFeaturesByDashboardAndModuleQueryService
)

from src.core.application.features.employee.employee_command_service import (
    BulkUpsertEmployeesService,
    DeleteEmployeeService
)
from src.core.application.features.dashboard.dashboard_query_service import (
    GetAllDashboardsQueryService
)
from src.core.application.features.order.dto.search_completed_orders.order_query_service import (
    SearchOrdersQueryService
)

from src.core.application.features.order.dto.search_open_orders.order_query_service import (
    SearchOrdersQueryService as OpenSearchOrdersQueryService
)

# Repositories
from src.config.persistence.repositories.employee.employee_query_repository import (
    EmployeeQueryRepository
)
from src.config.persistence.repositories.employee.employee_command_repository import (
    EmployeeCommandRepository
)
from src.config.persistence.repositories.dashboard.dashboard_query_repository import (
    DashboardQueryRepository
)
from src.config.persistence.repositories.order.search_completed_orders.order_query_repository import (
    OrderQueryRepository
)
from src.config.persistence.repositories.order.search_open_orders.order_query_repository import (
    OrderQueryRepository as OpenOrderQueryRepository
)

# DB Context
from src.config.persistence.context.database_context import get_db_async
from src.config.persistence.repositories.employee.employee_query_repository import EmployeeQueryRepository
from src.config.persistence.repositories.employee.employee_command_repository import EmployeeCommandRepository

from src.config.persistence.repositories.dashboard.dashboard_query_repository import DashboardQueryRepository

from src.config.persistence.repositories.module.module_query_repository import ModuleQueryRepository

from src.config.persistence.repositories.feature.feature_query_repository import FeatureQueryRepository

from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import AsyncSession

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.main",
            "src.host.routers.v1.rest.employee.employee_rest_controller",
            "src.host.routers.v1.odata.employee.employee_odata_controller",
            "src.host.routers.v1.rest.dashboard.dashboard_rest_controller",
            "src.host.routers.v1.rest.module.module_rest_controller",
            "src.host.routers.v1.rest.feature.feature_rest_controller",
            "src.host.routers.v1.rest.dashboard.dashboard_rest_controller",
            "src.host.routers.v1.rest.completedorders.order_rest_controller",
            "src.host.routers.v1.rest.openorders.order_rest_controller"
            ]
    )

    config = providers.Configuration()

    # DB session provider
    db_session: providers.Resource[AsyncSession] = providers.Resource(get_db_async)

    employee_command_repository = providers.Factory(EmployeeCommandRepository, db=db_session)
    employee_query_repository = providers.Factory(EmployeeQueryRepository, db=db_session)

    dashboard_query_repository = providers.Factory(DashboardQueryRepository, db=db_session)
    module_query_repository = providers.Factory(ModuleQueryRepository, db=db_session)
    feature_query_repository = providers.Factory(FeatureQueryRepository, db=db_session)

    bulkupsert_employee_service = providers.Factory(BulkUpsertEmployeesService, employee_repository=employee_command_repository)
    delete_employee_service = providers.Factory(DeleteEmployeeService, employee_repository=employee_command_repository)

    get_all_employee_service = providers.Factory(GetAllEmployeesQueryService, employee_repository=employee_query_repository)
    get_employee_by_id_service = providers.Factory(GetEmployeeByIdQueryService, employee_repository=employee_query_repository)
    get_all_employee_odata_service = providers.Factory(GetAllEmployeesODataQueryService, employee_repository=employee_query_repository)

    get_all_dashboard_service = providers.Factory(GetAllDashboardsQueryService, dashboard_repository=dashboard_query_repository)
    get_modules_by_dashboard_service = providers.Factory(GetModulesByDashboardQueryService, module_repository=module_query_repository)
    get_features_by_dashboard_and_module_service = providers.Factory(GetFeaturesByDashboardAndModuleQueryService, feature_repository=feature_query_repository)

# Optional global container wiring
    # Repository Providers
    employee_command_repository = providers.Factory(
        EmployeeCommandRepository, db=db_session
    )
    employee_query_repository = providers.Factory(
        EmployeeQueryRepository, db=db_session
    )
    dashboard_query_repository = providers.Factory(
        DashboardQueryRepository, db=db_session
    )
    order_query_repository = providers.Factory(
        OrderQueryRepository, db=db_session
    )
    open_order_query_repository = providers.Factory(
        OpenOrderQueryRepository, db=db_session
    )

    # Command Services
    bulkupsert_employee_service = providers.Factory(
        BulkUpsertEmployeesService,
        employee_repository=employee_command_repository
    )
    delete_employee_service = providers.Factory(
        DeleteEmployeeService,
        employee_repository=employee_command_repository
    )

    # Query Services
    get_all_employee_service = providers.Factory(
        GetAllEmployeesQueryService,
        employee_repository=employee_query_repository
    )
    get_employee_by_id_service = providers.Factory(
        GetEmployeeByIdQueryService,
        employee_repository=employee_query_repository
    )
    get_all_employee_odata_service = providers.Factory(
        GetAllEmployeesODataQueryService,
        employee_repository=employee_query_repository
    )
    get_all_dashboard_service = providers.Factory(
        GetAllDashboardsQueryService,
        dashboard_repository=dashboard_query_repository
    )
    search_order_service = providers.Factory(
        SearchOrdersQueryService,
        order_repository=order_query_repository  # ✅ Fixed here
    )
    search_open_order_service = providers.Factory(
        OpenSearchOrdersQueryService,
        order_repository=open_order_query_repository  # ✅ Fixed here
    )

# Optional global container instance for wiring
container = Container()
container.wire(modules=[__name__])