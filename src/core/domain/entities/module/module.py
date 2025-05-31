from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func
from src.core.domain.entities.dashboard.dashboard import Dashboard
from sqlalchemy.orm import declarative_base, relationship
 
Base = declarative_base()
 
class Module(Base):
    __tablename__ = "Module"
 
    DashboardId = Column(Integer, ForeignKey("Dashboard.DashboardId"))
    DashboardName = Column(String(255), nullable=False)
    ModuleId = Column(Integer, primary_key=True)
    ModuleName = Column(String(255), nullable=False)
    