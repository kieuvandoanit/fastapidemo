from typing import Optional, List, Union, Any, Dict

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    # Declare model specific CRUD operation methods.
    def get_user(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        email = obj_in.email.lower() if obj_in.email else None
        db_obj = User(
            email=email,
            passwordHash=get_password_hash(obj_in.password),
            firstName=obj_in.firstName,
            middleName=obj_in.middleName,
            lastName=obj_in.lastName,
            mobile=obj_in.mobile,
            admin=obj_in.admin,
            vendor=obj_in.vendor
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
            passwordHash = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["passwordHash"] = passwordHash
        updated = super().update(db, db_obj=db_obj, obj_in=update_data)
        return updated
    
    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_user(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.passwordHash):
            return None
        return user
    
    def get_all(self, db: Session) -> List[User]:
        return db.query(self.model).all()

user = CRUDUser(User)
