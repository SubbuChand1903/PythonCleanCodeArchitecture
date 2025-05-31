from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from src.core.domain.entities.employee.employee import Employee
from src.core.domain.interfaces.repositories.employee.iemployee_command_repository import IEmployeeCommandRepository
from src.config.infrastructure.exceptions.app_exception import AppException
import pandas as pd

class EmployeeCommandRepository(IEmployeeCommandRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def bulk_upsert(self, employees: List[Employee]) -> None:
        try:
            # Convert domain models to dicts (ensure Employee uses pydantic or has a dict method)
            df = pd.DataFrame(
                [e.__dict__ for e in employees],
                columns=["first_name", "last_name", "email", "department", "salary", "hire_date"]
            )

            # Create parameter list
            udt_employee_list = df.to_records(index=False).tolist()

            sql = text("""
                EXEC [dbo].[InsertorUpdateEmployees]
                @Employees = :udt_employees
            """)

            await self.db.execute(sql, {"udt_employees": udt_employee_list})
            await self.db.commit()

        except Exception as e:
            print(f"[EmployeeCommandRepository] bulk_upsert error: {e}")
            raise AppException(f"Failed to bulk upsert employees: {str(e)}")

    async def delete_by_id(self, employee_id: int) -> None:
        try:
            sql = text("""
                EXEC dbo.DeleteEmployeeById @EmployeeId = :employee_id
            """)
            await self.db.execute(sql, {"employee_id": employee_id})
            await self.db.commit()
        except Exception as e:
            print(f"[EmployeeCommandRepository] delete_by_id error: {e}")
            raise AppException(f"Failed to delete employee: {str(e)}")
