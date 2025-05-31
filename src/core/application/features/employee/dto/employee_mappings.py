from typing import List
from src.core.application.features.employee.dto.employee_dto import EmployeeDTO
from src.core.domain.entities.employee.employee import Employee

class EmployeeMappings:

    @staticmethod
    def model_to_dto(employee_model: Employee) -> EmployeeDTO:
        if employee_model:
            return EmployeeDTO.model_validate(employee_model)
        return None

    @staticmethod
    def dto_to_model(employee_dto: EmployeeDTO) -> Employee:
        return Employee(**employee_dto.model_dump())

    @staticmethod
    def model_list_to_dto_list(employee_models: List[Employee]) -> List[EmployeeDTO]:
        return [EmployeeDTO.model_validate(model) for model in employee_models]

    @staticmethod
    def dto_list_to_model_list(employee_dtos: List[EmployeeDTO]) -> List[Employee]:
        return [Employee(**dto.model_dump()) for dto in employee_dtos]