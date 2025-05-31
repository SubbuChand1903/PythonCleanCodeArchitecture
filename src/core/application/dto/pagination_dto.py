from typing import Optional
from pydantic import BaseModel

class PaginationDTO(BaseModel):
    page: Optional[int] = None
    page_size: Optional[int] = None