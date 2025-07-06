from pydantic import BaseModel, Field
from typing import Optional

class UserBase(BaseModel):
    username: str
    password: str
    organization_id: Optional[int] = None

class UserCreate(UserBase):
    password: str
    organization_id: Optional[int] = None

class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None

class UserOut(UserBase):
    id: int
    organization_id: Optional[int] = None

    class Config:
        from_attributes = True
        populate_by_name = True

class Token(BaseModel):
    access_token: str
    token_type: str