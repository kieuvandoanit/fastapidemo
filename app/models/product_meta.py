from sqlalchemy import Integer, String, ForeignKey, Column
from sqlalchemy.orm import relationship
from app.database.base_class import Base

class Product_Meta(Base):
    __tablename__ = "product_meta"

    id = Column(Integer, primary_key=True, index=True)
    productId = Column(Integer, ForeignKey("product.id"), nullable=False)
    key = Column(String(50), nullable=True)
    content = Column(String, nullable=True)

    product = relationship("Product", back_populates="product_meta")