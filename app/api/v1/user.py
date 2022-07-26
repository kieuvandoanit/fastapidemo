from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse as FastAPIResponse

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()

@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_admin)
) -> Any:
    """
    <h4>Only <b>admin</b> can access this api</h4>
    <p>Returns a list of user information</p>
    """
    users = crud.user.get_all(db=db)
    return users

@router.get("/me", response_model=schemas.User)
def get_current_user(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user)
) -> schemas.User:
    """
    <p>Get current user info</p>
    """
    return current_user

@router.get("/{user_id}", response_model= schemas.User)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user)
) -> schemas.User:
    """
    <p>Get user by id</p>
    """
    user = crud.user.get(db=db, id=user_id)
    if not user:
        raise HTTPException(status_code=400, detail=f"User id {user_id} is not found")
    return user

@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    current_user: models.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    <h4>Only <b>admin</b> can access this api</h4>
    <p>Create a new user information.</p>
    """
    user = crud.user.get_user(
        db,
        username=user_in.username,
        email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username or email already exists"
        )
    try:
        user = crud.user.create(db, obj_in=user_in)
    except IntegrityError as e:
        raise HTTPException(
            status_code=422,
            detail=str(e.orig.diag.message_detail)
        )
    return user

@router.put("/me", response_model=schemas.User)
def update_current_user(
    obj_in: schemas.UserUpdate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user)
) -> schemas.User:
    user = crud.user.update(db=db,db_obj=current_user, obj_in=obj_in)
    return user

@router.put("/{user_id}", response_model=schemas.User)
def update_user_by_id(
    user_id: int,
    obj_in: schemas.UserUpdate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_admin)
) -> schemas.User:
    user = crud.user.get(db=db, id=user_id)
    if not user:
        raise HTTPException(status_code=400, detail="User is not found")
    user = crud.user.update(db=db, db_obj=user, obj_in=obj_in)
    return user

@router.delete("/{user_id}", response_model=schemas.User)
def remove_user(
    user_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_admin)
) -> schemas.User:
    user = crud.user.get(db=db, id=user_id)
    if not user:
        raise HTTPException(status_code=400, detail="User is not found")
    user = crud.user.remove(db=db, id=user_id)
    return user