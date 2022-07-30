from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.base_class import Base

class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key = True, index=True)
    userId = Column(Integer, ForeignKey("user.id"), nullable=False)
    sessionId = Column(String(100), nullable=True)
    token = Column(String(100), nullable=True)
    status = Column(Integer, nullable=False)
    firstName = Column(String(50), nullable=False)
    middleName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    mobile = Column(String(10), nullable=False)
    email = Column(String(50), nullable=False)
    line1 = Column(String(50), nullable=False)
    line2 = Column(String(50), nullable=True)
    city = Column(String(50), nullable=False)
    province = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    createdAt = Column(DateTime, nullable=False, server_default = func.now())
    updatedAt = Column(DateTime, nullable=False, server_default=func.now())
    content = Column(String, nullable = True)

    user = relationship("User", back_populates = "cart")
    cart_item = relationship("Cart_Item", back_populates="cart")