from pydantic import BaseModel
from typing import List

class PoloBase(BaseModel):
    name: str
    city: str
    state: str


class PoloCreate(PoloBase):
    pass

class PoloUpdate(PoloBase):
    pass

class PoloOut(PoloBase):
    id: int

    class Config:
        from_attributes = True

class PaginatedPoloOut(BaseModel):
    data: List[PoloOut]
    page: int
    page_size: int
    total_pages: int
    total_items: int