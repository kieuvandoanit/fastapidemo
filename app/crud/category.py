from app.crud.base import CRUDBase
from app import schemas, models
from app.models.category import Category
from sqlalchemy.orm import Session

class CRUDCategory(CRUDBase[models.Category, schemas.CategoryCreate, schemas.CategoryUpdate]):
    def get_by_title(self, *, db: Session, title: str):
        result = db.query(self.model).filter(self.model.title == title).first()
        return result

category = CRUDCategory(Category)