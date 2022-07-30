from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.base_class import Base

class Cart_Item(Base):
    __tablename__ = "cart_item"
    id = Column(Integer, primary_key = True, index=True)
    productId = Column(Integer, ForeignKey("product.id"), nullable=False)
    cartId = Column(Integer, ForeignKey("cart.id"), nullable=False)
    sku = Column(String(100), nullable = True)
    price = Column(Float, nullable=False)
    discount = Column(Float, nullable=False, default = 0)
    quantity = Column(Integer, nullable=False)
    active = Column(Boolean, default=True)
    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, server_default=func.now())
    content = Column(String, nullable=True)

    product = relationship("Product", back_populates = "cart_item")
    cart = relationship("Cart", back_populates="cart_item")