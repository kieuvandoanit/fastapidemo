from requests import session
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.base_class import Base

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)
    sessionId = Column(String(100), nullable=False)
    token = Column(String(100), nullable=True)
    status = Column(Integer, nullable=False)
    subTotal = Column(Float, nullable=False)
    itemDiscount = Column(Float, nullable=True, default=0)
    tax = Column(Float, nullable=True)
    shipping = Column(Float, nullable=True)
    total = Column(Float, nullable=False, default = 0)
    promo = Column(String(50), nullable=True)
    discount = Column(Float, nullable=False, default=0)
    grandTotal = Column(Float, nullable=True)
    firstName = Column(String(50), nullable=False)
    middleName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    mobile = Column(String(10), nullable=False)
    email = Column(String(50), nullable=True)
    line1 = Column(String(50), nullable=False)
    line2 = Column(String(50), nullable=True)
    city = Column(String(50), nullable=False)
    province = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    createdAt = Column(DateTime, nullable=False, server_default=func.now())
    updatedAt = Column(DateTime, nullable=False, server_default=func.now())
    content = Column(String, nullable=True)

    user = relationship("User", back_populates="order")
    transaction = relationship("Transaction", back_populates="order")
    order_item = relationship("Order_Item", back_populates="order")
