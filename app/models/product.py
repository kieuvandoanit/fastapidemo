from sqlalchemy import Column, DateTime, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.base_class import Base
class Product(Base):
    __tablename__="product"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("user.id"),nullable=True)
    title = Column(String(75), nullable=False)
    metaTitle = Column(String(100), nullable=True, default=None)
    slug = Column(String(100), nullable=True, default=None)
    summary = Column(String, nullable=False)
    type = Column(Integer, nullable=False)
    sku = Column(String(100), nullable=False)
    price = Column(Float, nullable = False)
    discount = Column(Float, nullable=True, default=0)
    quantity = Column(Integer, nullable=True, default=False)
    shop = Column(Boolean, nullable=True, default=False)
    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, server_default=func.now())
    publishedAt = Column(DateTime, nullable=True)
    startsAt = Column(DateTime, nullable=True)
    endsAt = Column(DateTime, nullable=True)
    content = Column(String, nullable=True)

    user = relationship("User", back_populates="product")
    # product_category = relationship("Product_Category", back_populates="product")
    # product_meta = relationship("Product_Meta", back_populates="product")
    # product_review = relationship("Product_Review", back_populates="product")
    # order_item = relationship("Order_Item", back_populates="product")
    # cart_item = relationship("Cart_Item", back_populates="product")
    # product_tag = relationship("Product_Tag", back_populates="product")




