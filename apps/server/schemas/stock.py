from pydantic import BaseModel
from datetime import datetime


class BaseBubbleData(BaseModel):
    last_price: float
    nav_price: float
    date: datetime


class BubbleData(BaseBubbleData):
    id: int
    stock_name: str

    class Config:
        orm_mode = True



class BaseStock(BaseModel):
    name: str
    fa_name: str


class Stock(BaseStock):
    bubbles: list[BubbleData] = []

    class Config:
        orm_mode = True


class StockCreate(BaseStock):
    pass
