import os
import sys
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from a2wsgi import ASGIMiddleware

from src.core.application.extensions.dependencies import Container
from src.host.routers.app_router import create_app_routers

# Application Metadata
APP_TITLE = "3 Sigma Order Entry Automation API"
APP_DESCRIPTION = "3 Sigma Order Entry Automation API automates order creation and updation"
APP_VERSION = "1.0.0"
DEFAULT_PORT = 8000

# Create FastAPI instance
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

# Middleware Configuration
def configure_middlewares(application: FastAPI):
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Router Configuration
def configure_routers(application: FastAPI):
    v1_router = create_app_routers()
    application.include_router(v1_router)

# Dependency Injector Container Setup
def configure_containers(application: FastAPI):
    container = Container()
    container.init_resources()
    container.wire(
        modules=[
            sys.modules[__name__],
            "src.host.routers.v1.odata.employee.employee_odata_controller",
            "src.host.routers.v1.rest.employee.employee_rest_controller"
        ],
        packages=["src.host.routers.v1"]
    )
    application.container = container

# Root Endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to 3 Sigma Order Entry Automation API!"}

# Main Application Configuration
def create_application() -> FastAPI:
    configure_middlewares(app)
    configure_routers(app)
    configure_containers(app)
    return app

# Create app on startup
app = create_application()

# Entry point
if __name__ == "__main__":
    port = int(os.environ.get("PORT", DEFAULT_PORT))
    uvicorn.run("src.main:app", host="127.0.0.1", port=port, reload=True)

# Optional: for WSGI/ASGI server compatibility
wsgi_app = ASGIMiddleware(app)