from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base_class import Base

class Product_Category(Base):
    __tablename__ = "product_category"

    productId = Column(Integer, ForeignKey("product.id"), primary_key=True, nullable=False)
    categoryId = Column(Integer, ForeignKey("category.id"), primary_key=True, nullable = False)

    category = relationship("Category", back_populates="product_category")
    product = relationship("Product", back_populates="product_category")