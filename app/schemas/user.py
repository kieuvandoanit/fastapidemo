from optparse import Option
from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    firstName: Optional[str] = None
    middleName: Optional[str] = None
    lastName: Optional[str]
    mobile: str
    

class UserCreate(UserBase):
    email: EmailStr
    password: str
    admin: Optional[bool] = False
    vendor: Optional[bool] = False

class UserUpdate(UserBase):
    password: Optional[str] = None
    vendor: Optional[bool]
    lastLogin: Optional[datetime]
    intro: Optional[str]
    profile: Optional[str]

class UserInDBBase(UserBase):
    id: Optional[int] = None
    admin: Optional[bool]
    vendor: Optional[bool]
    registeredAt: Optional[datetime]
    lastLogin: Optional[datetime]
    intro: Optional[str]
    profile: Optional[str]
    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    passwordHash: str