from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Dashboard(Base):
    __tablename__ = "Dashboard"

    dashboard_id = Column(Integer, primary_key=True, index=True)
    dashboard_name = Column(String(500), nullable=False)