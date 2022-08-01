from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base_class import Base

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key = True, index=True)
    parentId = Column(Integer, ForeignKey("category.id"), nullable=True)
    title = Column(String(75), nullable=False)
    metaTitle = Column(String(100), nullable=True)
    slug = Column(String(100), nullable=True)
    content = Column(String, nullable=True)

    children = relationship("Category", back_populates="parent")
    parent = relationship("Category", back_populates="children", remote_side=[id])
    product_category = relationship("Product_Category", back_populates="category")

