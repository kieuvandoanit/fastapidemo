from typing import TYPE_CHECKING
from xml.dom import ValidationErr

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship, validates
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import expression
from app.database.base_class import Base

VALID_ROLES = ['admin', 'user']

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True, nullable=True, default=None)
    email = Column(String, unique=True, index=True, nullable=True, default=None)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default = True)
    username = Column(String, index=True, unique=True)
    role = Column(String, nullable=True)
    push_notification = Column(Boolean(), server_default=expression.true(), default=False)

    @validates('role')
    def validate_role(self, key, role):
        assert (role in VALID_ROLES), "%s not a valid role" % role
        return role
    
    @property
    def has_admin_access(self):
        return self.role == 'admin'
    
    def has_user_access(self):
        return self.role in VALID_ROLES