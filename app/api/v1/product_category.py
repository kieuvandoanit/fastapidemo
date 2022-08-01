from http.client import HTTPException
from math import prod
from urllib.error import HTTPError
from fastapi import APIRouter, Depends
from app import models, schemas, crud
from typing import Any, List
from sqlalchemy.orm import Session
from app.api.deps import get_db

router = APIRouter()

@router.get("", response_model=List[schemas.Product_Category])
def read_product_category(
    *,
    db: Session = Depends(get_db),
    product_id: int = None,
    category_id: int = None,
    limit: int = 100,
    skip: int = 0
) -> Any:
    """
    Get all product_category
    """
    if product_id is None and category_id is None:
        result = crud.product_category.get_multi(db=db, skip=skip, limit = limit)
    elif product_id is not None and category_id is None:
        result = crud.product_category.get_by_product_id(db=db, product_id=product_id)
    elif product_id is None and category_id is not None:
        result = crud.product_category.get_by_category_id(db=db, category_id=category_id)
    else:
        result = crud.product_category.get_by_product_category(db=db, product_id=product_id, category_id=category_id)
    return result

@router.post("", response_model=schemas.Product_Category)
def create_product_category(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.Product_CategoryCreate
) -> Any:
    """
    Create product category
    """
    item = crud.product_category.get_by_product_category(db=db, category_id=obj_in.categoryId, product_id = obj_in.productId)
    if item:
        HTTPException(status_code = 400, detail = "Product category is already exists")
    result = crud.product_category.create(db=db, obj_in = obj_in)
    return result

# @router.put()
