from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.base_class import Base

class Order_Item(Base):
    __tablename__ = "order_item"
    id = Column(Integer, primary_key=True, index=True)
    productId = Column(Integer, ForeignKey("product.id"), nullable=False)
    orderId = Column(Integer, ForeignKey("order.id"), nullable=False)
    sku = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    discount = Column(Float, nullable=False, default=0)
    quantity = Column(Integer, nullable=False, default = 1)
    createdAt = Column(DateTime, nullable=False, server_default=func.now())
    updatedAt = Column(DateTime, nullable=False, server_default=func.now())
    content = Column(String, nullable=True)

    product = relationship("Product", back_populates = "order_item")
    order = relationship("Order", back_populates = "order_item")