from pydantic import BaseModel, Field

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None

class UserOut(UserBase):
    userId: int = Field(..., alias="id")

    class Config:
        from_attributes = True
        populate_by_name = True