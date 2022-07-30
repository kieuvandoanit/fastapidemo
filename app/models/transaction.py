from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.base_class import Base

class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key = True, index=True)
    userId = Column(Integer, ForeignKey("user.id"), index=True, nullable=False)
    orderId = Column(Integer, ForeignKey("order.id"), index=True, nullable=False)
    code = Column(String(100), nullable=False)
    type = Column(Integer, nullable = False)
    mode = Column(Integer, nullable=True)
    status = Column(Integer, nullable=False)
    createdAt = Column(DateTime, nullable = True, server_default=func.now())
    updatedAt = Column(DateTime, nullable=False, server_default=func.now())
    content = Column(String, nullable=True)

    user = relationship("User", back_populates="transaction")
    order = relationship("Order", back_populates="transaction")