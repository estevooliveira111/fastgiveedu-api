from pydantic import BaseModel

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