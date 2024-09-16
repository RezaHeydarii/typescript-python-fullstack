
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .constants import DB_URL

print(DB_URL)

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


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


def create_stock_bubble(db: Session, newBubble: BubbleData):
    db.add(newBubble)
    db.commit()
    #db.refresh(newBubble)
    return newBubble


def get_or_create_stock(db: Session, new_stock: Stock):
    in_db = db.query(Stock).filter(Stock.name == new_stock.name).first()
    if in_db == None:
        db.add(new_stock)
        db.commit()
        # db.refresh(new_stock)
    return new_stock
