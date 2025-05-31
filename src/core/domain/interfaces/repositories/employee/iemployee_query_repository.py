from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.domain.entities.employee.employee import Employee

class IEmployeeQueryRepository(ABC):

    @abstractmethod
    async def get_all_employees(self) -> List[Employee]:
        """Fetch all employees from the database."""
        pass

    @abstractmethod
    async def get_employee_by_id(self, employeeid: int) -> Optional[Employee]:
        """Fetch a single employee by ID."""
        pass

    @abstractmethod
    async def get_employees_odata(
        self,
        top: Optional[int],
        skip: Optional[int],
        orderby: Optional[str],
        filter_: Optional[str],
        count: Optional[bool]
    ) -> List[Employee]:
        """Fetch employees using OData-style query parameters."""
        pass