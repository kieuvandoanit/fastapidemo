from fastapi import HTTPException
from app.crud.base import CRUDBase
from app import schemas, models
from app.models import Product_Category
from sqlalchemy.orm import Session
from app import crud

class CRUDProduct_Category(CRUDBase[Product_Category, schemas.Product_CategoryCreate, schemas.Product_CategoryUpdate]):
    def get_by_product_id(self, db: Session, product_id: int):
        product = crud.product.get(db=db, id=product_id)
        if not product:
            HTTPException(status_code=400, detail = "Product is not found")
        result = db.query(self.model).filter(self.model.productId == product_id).all()
        return result
    
    def get_by_category_id(self, db: Session, category_id: int):
        category = crud.category.get(db=db, id=category_id)
        if not category:
            HTTPException(status=400, detail="Category is not found")

        result = db.query(self.model).filter(self.model.categoryId == category_id).all()
        return result
        
    def get_by_product_category(self, *, db: Session, category_id: int, product_id: int):
        product = crud.product.get(db=db, id=product_id)
        if not product:
            HTTPException(status_code=400, detail = "Product is not found")
        
        category = crud.category.get(db=db, id=category_id)
        if not category:
            HTTPException(status=400, detail="Category is not found")
        
        result = db.query(self.model).filter(self.model.categoryId==category_id,
                self.model.productId == product_id).first()
        return result

product_category = CRUDProduct_Category(Product_Category)