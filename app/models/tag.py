from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String

from app.database.base_class import Base

class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(75), nullable=True)
    metaTitle = Column(String(100), nullable=True)
    slug = Column(String(100), nullable=True)
    content = Column(String, nullable=True)

    product_tag = relationship("Product_Tag", back_populates="tag")