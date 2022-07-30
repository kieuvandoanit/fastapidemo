from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.product import Product
from app import schemas


class CRUDProduct(CRUDBase[Product, schemas.ProductCreate, schemas.ProductUpdate]):
    # Declare model specific CRUD operation methods.
    def get_by_userId(self, *, db: Session, user_id: int):
        products = db.query(self.model).filter(self.model.userId == user_id).all()
        return products


product = CRUDProduct(Product)
