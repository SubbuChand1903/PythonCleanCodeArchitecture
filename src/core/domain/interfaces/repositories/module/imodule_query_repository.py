from abc import ABC, abstractmethod
from typing import List
from src.core.domain.entities.module.module import Module

class IModuleQueryRepository(ABC):

    @abstractmethod
    async def get_modules_by_dashboard_id(self, dashboard_id: int) -> List[Module]:
        """Fetch all Modules from the database"""
        pass
