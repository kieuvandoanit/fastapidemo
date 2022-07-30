from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.base_class import Base

class Product_Review(Base):
    __tablename__ = "product_review"

    id = Column(Integer, primary_key=True, index=True)
    productId = Column(Integer, ForeignKey("product.id"), nullable=False)
    parentId = Column(Integer, ForeignKey("product_review.id"), nullable=True)
    title = Column(String(100), nullable=False)
    rating = Column(Integer, nullable=False)
    published = Column(Boolean, nullable=False, default=True)
    createdAt = Column(DateTime, nullable=False, server_default=func.now())
    publishedAt = Column(DateTime, nullable=False, server_default=func.now())
    content = Column(String, nullable=False)

    parent = relationship("Product_Review", back_populates="children")
    children = relationship("Product_Review", back_populates="parent")
    product = relationship("Product", back_populates="product_review")