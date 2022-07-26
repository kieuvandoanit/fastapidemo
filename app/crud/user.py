from typing import Optional, List, Union, Any, Dict

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    # Declare model specific CRUD operation methods.
    def get_user(self, db: Session, *, email: str = None, username: str) -> Optional[User]:
        if not email:
            return db.query(User).filter(User.username == username).first()
        return db.query(User).filter((User.email == email) | (User.username == username)).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        email = obj_in.email.lower() if obj_in.email else None
        db_obj = User(
            email=email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            username=obj_in.username,
            role=obj_in.role
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if 'password' in update_data:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        if 'role' in update_data and update_data['role'] is None:
            update_data['role'] = db_obj.role
        updated = super().update(db, db_obj=db_obj, obj_in=update_data)
        return updated
    
    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_user(db, email=email, username=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
    
    def is_active(self, user: User) -> bool:
        return user.is_active
    
    def get_all(self, db: Session) -> List[User]:
        return db.query(self.model).all()

user = CRUDUser(User)
