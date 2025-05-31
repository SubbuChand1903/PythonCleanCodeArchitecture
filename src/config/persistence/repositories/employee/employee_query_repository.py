from typing import List, Optional
from sqlalchemy import asc, desc, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.infrastructure.exceptions.app_exception import AppException
from src.core.domain.entities.employee.employee import Employee
from src.core.domain.interfaces.repositories.employee.iemployee_query_repository import IEmployeeQueryRepository


class EmployeeQueryRepository(IEmployeeQueryRepository):

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_employees(self) -> List[Employee]:
        try:
            stmt = select(Employee)
            result = await self.db.execute(stmt)
            employees = result.scalars().all()
            return employees
        except Exception as e:
            print(f"In Employee Repository - Exception during get_all_employees: {e}")
            raise AppException(f"Error fetching all employees: {str(e)}")

    async def get_employee_by_id(self, employeeid: int) -> Optional[Employee]:
        try:
            query = text("EXEC [dbo].[usp_GetEmployeeById] :employeeid")
            params = {"employeeid": employeeid}

            result = await self.db.execute(query, params)
            row = result.mappings().first()

            if row:
                mapped_row = {
                    "employee_id": row["EmployeeId"],
                    "first_name": row["FirstName"],
                    "last_name": row["LastName"],
                    "email": row["Email"],
                    "department": row["Department"],
                    "salary": row["Salary"],
                    "hire_date": row["HireDate"]
                }
                employee = Employee(**mapped_row)
                print("Employee:", employee)
                return employee
            else:
                print(f"No employee found for ID: {employeeid}")
                return None

        except Exception as e:
            print(f"In Employee Repository - Exception during stored procedure execution: {e}")
            raise AppException(f"Error executing stored procedure: {str(e)}")

    async def get_employees_odata(
        self,
        top: Optional[int],
        skip: Optional[int],
        orderby: Optional[str],
        filter_: Optional[str],
        count: Optional[bool]
    ) -> List[Employee]:
        try:
            stmt = select(Employee)

            # Apply $filter
            if filter_:
                try:
                    for condition in filter_.split(" and "):
                        field, op, value = condition.strip().split(" ", 2)
                        value = value.strip("'\"")
                        column = getattr(Employee, field, None)
                        if column is not None:
                            if op == "eq":
                                stmt = stmt.where(column == value)
                            elif op == "gt":
                                stmt = stmt.where(column > float(value))
                            elif op == "lt":
                                stmt = stmt.where(column < float(value))
                except Exception as e:
                    raise AppException(f"Invalid filter format: {filter_}. Error: {e}")

            # Apply $orderby
            if orderby:
                try:
                    parts = orderby.split()
                    field = parts[0]
                    direction = parts[1].lower() if len(parts) > 1 else "asc"
                    column = getattr(Employee, field, None)
                    if column is not None:
                        stmt = stmt.order_by(desc(column) if direction == "desc" else asc(column))
                except Exception as e:
                    raise AppException(f"Invalid orderby format: {orderby}. Error: {e}")

            # Apply skip/top
            if skip:
                stmt = stmt.offset(skip)
            if top:
                stmt = stmt.limit(top)

            result = await self.db.execute(stmt)
            employees = result.scalars().all()

            print("OData Employees:", employees)
            return employees

        except Exception as e:
            print(f"In Employee Repository - Exception in get_employees_odata: {e}")
            raise AppException(f"Error fetching employees using OData: {str(e)}")