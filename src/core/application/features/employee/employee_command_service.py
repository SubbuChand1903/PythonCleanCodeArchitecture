from typing import List
from src.core.application.features.employee.dto.employee_dto import EmployeeDTO
from src.core.application.features.employee.dto.employee_mappings import EmployeeMappings
from src.core.application.responsemodels.message_response import MessageResponse
from src.core.domain.entities.employee.employee import Employee
from src.core.domain.interfaces.repositories.employee.iemployee_command_repository import IEmployeeCommandRepository

class BulkUpsertEmployeesService:
    def __init__(self, employee_repository: IEmployeeCommandRepository):
        self.employee_repository = employee_repository

    async def bulk_upsert_employees(self, employee_data_list: List[EmployeeDTO]) -> MessageResponse:
        try:
            employee_models: List[Employee] = [
                EmployeeMappings.dto_to_model(dto) for dto in employee_data_list
            ]

            await self.employee_repository.bulk_upsert(employee_models)

            return MessageResponse(
                message="Employees inserted/updated successfully.",
                is_exception=False,
                error_messages=None,
                is_success=True,
                id=None
            )

        except Exception as e:
            print(f"[BulkUpsertEmployeesService] Exception occurred: {e}")
            return MessageResponse(
                message="Bulk upsert failed.",
                is_exception=True,
                error_messages=[{"error": str(e)}],
                is_success=False,
                id=-100
            )


class DeleteEmployeeService:
    def __init__(self, employee_repository: IEmployeeCommandRepository):
        self.employee_repository = employee_repository

    async def delete_employee_by_id(self, employee_id: int) -> MessageResponse:
        try:
            await self.employee_repository.delete_by_id(employee_id)

            return MessageResponse(
                message="Employee deleted successfully.",
                is_exception=False,
                error_messages=None,
                is_success=True,
                id=employee_id
            )

        except Exception as e:
            print(f"[DeleteEmployeeService] Exception occurred: {e}")
            return MessageResponse(
                message="Failed to delete employee.",
                is_exception=True,
                error_messages=[{"error": str(e)}],
                is_success=False,
                id=-100
            )