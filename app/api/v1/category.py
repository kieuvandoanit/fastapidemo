from typing import Any, List
from unicodedata import name

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api.deps import get_db

router = APIRouter()

@router.get("", response_model=List[schemas.Category])
def read_categories(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Return list category
    """
    category = crud.category.get_multi(db=db, skip=skip, limit=limit)
    return category

@router.get("/${category_id}", response_model=schemas.Category)
def read_category(
    *,
    db: Session = Depends(get_db),
    category_id: int
) -> Any:
    """
    Return category
    """
    category = crud.category.get(db=db, id=category_id)
    if not category:
        HTTPException(status_code = 400, detail="Category is not found")
    return category


@router.post("", response_model=schemas.Category)
def create_category(
    *,
    db: Session = Depends(get_db),
    obj_in: schemas.CategoryCreate
) -> Any:
    """
    Create category
    """
    category = crud.category.get_by_title(db=db, title=obj_in.title)
    if category:
        HTTPException(status_code=400, detail="Category is already exist in database")
    category = crud.category.create(db=db, obj_in=obj_in)
    return category

@router.put("/${category_id}", response_model=schemas.Category)
def update_category(
    *,
    db: Session = Depends(get_db),
    category_id: int,
    obj_in: schemas.CategoryUpdate
) -> Any:
    """
    Update category
    """
    category = crud.category.get(db=db, id=category_id)
    if not category:
        HTTPException(status_code=400, detail="Category is not found")
    result = crud.category.update(db=db,db_obj=category,obj_in=obj_in)
    return result

@router.delete("/${category_id}")
def delete_category(
    *,
    db: Session = Depends(get_db),
    category_id: int
) -> Any:
    """
    Delete category
    """
    category = crud.category.get(db=db, id=category_id)
    if not category:
        HTTPException(status_code=400, detail="Category is not found")
    result = crud.category.remove(db=db, id=category_id)
    return result