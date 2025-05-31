from abc import ABC, abstractmethod
from typing import List
from src.core.domain.entities.employee.employee import Employee

class IEmployeeCommandRepository(ABC):
    @abstractmethod
    async def bulk_upsert(self, employees: List[Employee]) -> None:
        """Insert or update a list of employees in bulk."""
        pass

    @abstractmethod
    async def delete_by_id(self, employee_id: int) -> None:
        """Delete an employee by primary key."""
        pass