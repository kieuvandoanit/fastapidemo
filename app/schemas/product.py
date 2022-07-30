from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class ProductBase(BaseModel):
    title: str
    metaTitle: Optional[str] = None
    summary: Optional[str]
    type: Optional[int] = 1
    sku: Optional[str]
    price: Optional[float]
    discount: Optional[float] = 0
    quantity: Optional[int] = 100
    shop: Optional[bool] = True


class ProductCreate(ProductBase):
    userId: Optional[int]
    content: Optional[str] = None


class ProductUpdate(ProductBase):
    userId: Optional[int]
    updatedAt: Optional[datetime]
    publishedAt: Optional[datetime]
    startsAt: Optional[datetime]
    endsAt: Optional[datetime]

class ProductInDBBase(ProductBase):
    id: int
    userId: int
    
    class Config:
        orm_mode = True

class Product(ProductInDBBase):
    pass

class ProductResponse(ProductBase):
    class Config:
        orm_mode = True
