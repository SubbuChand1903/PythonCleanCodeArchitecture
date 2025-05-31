from src.config.infrastructure.exceptions.app_exception import AppException

class SecurityException(AppException):
    def __init__(self, message="Invalid data", *args, **kwargs):
        super().__init__(message, *args, **kwargs)      
        
        self.error_code = kwargs.get("error_code")
        self.details = kwargs.get("details")

    def __str__(self):  
        return f"Security Error: {self.message}"