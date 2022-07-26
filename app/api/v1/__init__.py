from fastapi import APIRouter

from app.api.v1 import products
from app.api.v1 import user
from app.api.v1 import login

api_router = APIRouter()
api_router.include_router(products.router, prefix="/products", tags=["Products"])
api_router.include_router(user.router, prefix="/users", tags=["Users"])
api_router.include_router(login.router)
