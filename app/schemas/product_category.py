from pydantic import BaseModel
from typing import Optional


class Product_CategoryBase(BaseModel):
    productId: int
    categoryId: int

class Product_CategoryCreate(Product_CategoryBase):
    pass

class Product_CategoryUpdate(Product_CategoryBase):
    pass

class Product_Category(Product_CategoryBase):
    pass

    class Config:
        orm_mode = True