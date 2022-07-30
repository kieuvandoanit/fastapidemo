from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api.deps import get_current_user, get_db

router = APIRouter()


# @router.get("", response_model=List[schemas.Product])
# def read_products(
#     db: Session = Depends(get_db),
#     skip: int = 0, 
#     limit: int = 100
# ) -> Any:
#     """
#     Retrieve all products.
#     """
#     products = crud.product.get_multi(db, skip=skip, limit=limit)
#     return products

@router.get("", response_model=List[schemas.Product])
def get_product_by_userId(
    *,
    db: Session = Depends(get_db),
    user_id: int,
) -> Any:
    user = crud.user.get(db=db, id=user_id)
    if not user:
        raise HTTPException(status_code=400, detail="User is not found")
    products = crud.product.get_by_userId(db=db, user_id=user_id)
    return products

@router.post("", response_model=schemas.Product)
def create_product(
    *, 
    db: Session = Depends(get_db), 
    product_in: schemas.ProductCreate,
    current_user: schemas.User = Depends(get_current_user)
) -> Any:
    """
    Create new products.
    """
    product_in.userId = current_user.id
    product = crud.product.create(db=db, obj_in=product_in)
    return product


@router.put("/{product_id}", response_model=schemas.Product)
def update_product(
    *,
    product_id: int,
    db: Session = Depends(get_db), 
    product_in: schemas.ProductUpdate,
    current_user: schemas.User = Depends(get_current_user)
) -> Any:
    """
    Update existing products.
    """
    product = crud.product.get(db=db, id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    product = crud.product.update(db=db, db_obj=product, obj_in=product_in)
    return product


@router.delete("/{product_id}", response_model=schemas.Message)
def delete_product(
    *, 
    db: Session = Depends(get_db), 
    product_id: int,
    current_user: schemas.User = Depends(get_current_user)
) -> Any:
    """
    Delete existing product.
    """
    product = crud.product.get(db, id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    crud.product.remove(db, id=product_id)
    return {"message": f"Product with ID = {product_id} deleted."}
