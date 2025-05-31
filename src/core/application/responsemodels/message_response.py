from typing import List, Optional, Union
from pydantic import BaseModel

class MessageResponse(BaseModel):
    message: str
    is_exception: bool
    error_messages: Optional[List[str]] = None  # ✅ Made optional
    is_success: bool
    id: Optional[Union[int, str]] = None        # ✅ Made optional and flexible