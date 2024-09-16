from database.main import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Stock(Base):
    __tablename__ = "stock"
    name = Column(String(256), primary_key=True)
    fa_name = Column(String(256))
    bubbles = relationship("BubbleData", back_populates="stock")


class BubbleData(Base):
    __tablename__ = "bubble_data"
    id = Column(Integer, primary_key=True)
    last_price = Column(Float)
    nav_price = Column(Float)
    date = Column(DateTime)
    stock_name = Column(String(256), ForeignKey("stock.name"))
    stock = relationship("Stock", back_populates="bubbles")
