from pydantic import BaseModel, EmailStr
from typing import Optional
from app.db.models.user_role import UserRole

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.GERERAL

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    is_active: Optional[str] = None
    role: Optional[str] = None

class UserInDB(UserBase):
    id: int
    is_active: bool
    role: UserRole

    class Config:
        from_attributes = True

class UserWithToken(UserInDB):
    access_token: str
    token_type: str