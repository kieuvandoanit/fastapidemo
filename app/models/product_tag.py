from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.database.base_class import Base

class Product_Tag(Base):
    __tablename__ = "product_tag"
    productId = Column(Integer, ForeignKey("product.id"), primary_key=True, index=True)
    tagId = Column(Integer, ForeignKey("tag.id"), primary_key=True, index=True)

    tag = relationship("Tag", back_populates="product_tag")
    product = relationship("Product", back_populates="product_tag")