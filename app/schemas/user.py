from optparse import Option
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    full_name: Optional[str] = None
    username: Optional[str]= None
    role: Optional[str] = None

class UserCreate(UserBase):
    email: Optional[str] = None
    username: str
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None
    username: Optional[str] = None
    push_notification: Optional[bool] = None

class UserInDBBase(UserBase):
    id: Optional[int] = None
    push_notification: Optional[bool] = None

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    hashed_password: str