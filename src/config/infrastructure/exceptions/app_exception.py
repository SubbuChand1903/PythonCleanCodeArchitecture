class AppException(Exception):
    def __init__(self, message="Sorry, an error occured", *args, **kwargs):
        super().__init__(message, *args, **kwargs)  
        self.message = message         
    
    def __str__(self):  
        return f"Application Error: {self.message}"

    def __repr__(self):
        return f"{self.__class__.__name__}(message='AppException Message: {self.message}')"