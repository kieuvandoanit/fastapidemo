from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class CategoryBase(BaseModel):
    title: Optional[str]
    parentId: Optional[int] = None
    metaTitle: Optional[str]
    slug: Optional[str]
    content: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryInDBBase(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class Category(CategoryInDBBase):
    pass