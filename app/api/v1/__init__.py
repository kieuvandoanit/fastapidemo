from fastapi import APIRouter

from app.api.v1 import products
from app.api.v1 import user
from app.api.v1 import login
from app.api.v1 import category
from app.api.v1 import product_category

api_router = APIRouter()
api_router.include_router(product_category.router, prefix="/product_category", tags=["Product_Category"])
api_router.include_router(category.router, prefix="/category", tags=["Category"])
api_router.include_router(products.router, prefix="/products", tags=["Products"])
api_router.include_router(user.router, prefix="/users", tags=["Users"])
api_router.include_router(login.router)

