
from distutils import debug
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from src.router.EmployeeRouter import EmployeeRouter
from src.models import EmployeeModel
from src.configs.db import get_db, engine
from sqlalchemy.orm import Session
import uvicorn
from typing import List,Optional
from fastapi.encoders import jsonable_encoder


app = FastAPI(title="Sample FastAPI Application",
    description="Sample FastAPI Application with Swagger and Sqlalchemy",
    version="1.0.0",)

EmployeeModel.Base.metadata.create_all(bind=engine)

#Add Routers
app.include_router(EmployeeRouter)

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)