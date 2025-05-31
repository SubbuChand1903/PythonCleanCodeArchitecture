from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from src.core.domain.entities.dashboard.dashboard import Dashboard
from src.core.domain.entities.module.module import Module
from src.core.domain.entities.user.user import User 

Base = declarative_base()

class Feature(Base):
    __tablename__ = "Feature"

    FeatureId = Column(Integer, primary_key=True)
    DashboardId = Column(Integer, ForeignKey("Dashboard.DashboardId"), nullable=False)
    DashboardName = Column(Integer, ForeignKey("Dashboard.DashboardName"), nullable=False)
    ModuleId = Column(Integer, ForeignKey("Module.ModuleId"), nullable=False)
    ModuleName = Column(Integer, ForeignKey("Module.ModuleName"), nullable=False)
    FeatureName = Column(String(500), nullable=False, unique=True)
