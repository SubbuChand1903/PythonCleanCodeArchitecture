from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.domain.entities.dashboard.dashboard import Dashboard

class IDashboardQueryRepository(ABC):

    @abstractmethod
    async def get_all_dashboards(self) -> List[Dashboard]:
        """Fetch all dashboards from the database."""
        pass