from fastapi import APIRouter

from src.host.routers.v1.odata.employee import employee_odata_controller as v1_employee_odata_router
from src.host.routers.v1.rest.employee import employee_rest_controller as v1_employee_rest_router
from src.host.routers.v1.rest.dashboard import dashboard_rest_controller as v1_dashboard_rest_controller
from src.host.routers.v1.rest.module import module_rest_controller as v1_module_rest_controller
from src.host.routers.v1.rest.feature import feature_rest_controller as v1_feature_rest_controller
from src.host.routers.v1.rest.completedorders import order_rest_controller as v1_order_rest_controller
from src.host.routers.v1.rest.openorders import order_rest_controller as v1_open_order_rest_controller
#from src.host.routers.v2 import user_router as v2_user_router

v1_router = APIRouter(prefix="/api/v1")

# Employee
v1_router.include_router(v1_employee_odata_router.employee_router) 
v1_router.include_router(v1_employee_rest_router.employee_router)

# Dashboard
v1_router.include_router(v1_dashboard_rest_controller.dashboard_router)

# Module
v1_router.include_router(v1_module_rest_controller.module_router)

# Feature
v1_router.include_router(v1_feature_rest_controller.feature_router)

#completedorder
v1_router.include_router(v1_order_rest_controller.completed_order_router)

#openorder
v1_router.include_router(v1_open_order_rest_controller.open_order_router)

def create_app_routers():        
        return v1_router#, v2_router  # Return both routers