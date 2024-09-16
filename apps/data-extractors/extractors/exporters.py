from extractors.items import StockData
from .db import Stock, BubbleData, get_or_create_stock, create_stock_bubble, SessionLocal


def export_stock_bubble_into_sql(data: StockData):
    db = SessionLocal()
    newStock = Stock(name=data.name, fa_name=data.fa_name)
    stock = get_or_create_stock(db, newStock)
    new_bubble = BubbleData(
        last_price=data.last_price,
        nav_price=data.nav_price,
        date=data.date,
        stock_name=data.name,
    )
    return create_stock_bubble(db, newBubble=new_bubble)
