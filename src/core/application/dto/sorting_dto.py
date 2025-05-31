from typing import Optional,List
from pydantic import BaseModel

class SortingDTO(BaseModel):
   sort_by: Optional[List[str]] = None  
   # Example: ["name", "-price"] (- for descending)
