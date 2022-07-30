from typing import TYPE_CHECKING
from xml.dom import ValidationErr

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship, validates
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import expression, func
from app.database.base_class import Base

VALID_ROLES = ['admin', 'user']

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(50), nullable=True, default=None)
    middleName = Column(String(50), nullable=True, default=None)
    lastName = Column(String(50), nullable=False)
    mobile = Column(String(10), nullable=True, default=None)
    email = Column(String, unique=True, index=True, nullable=True, default=None)
    passwordHash = Column(String(100), nullable=False)
    admin = Column(Boolean, default=False)
    vendor = Column(Boolean, default=False)
    registeredAt = Column(DateTime(timezone=True), server_default=func.now())
    lastLogin = Column(DateTime(timezone=True), server_default=func.now())
    intro = Column(String, nullable=True, default=None)
    profile = Column(String, nullable=True, default=None)

    product = relationship("Product", back_populates="user")
    # order = relationship("Order", back_populates="user")
    # transaction = relationship("Transaction", back_populates="user")
    # cart = relationship("Cart", back_populates="user")
    
    @property
    def has_admin_access(self):
        return self.admin == True