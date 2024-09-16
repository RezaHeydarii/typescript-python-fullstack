from database.main import Session
import schemas.stock as schemas
from model import stock as model


def create_stock(db: Session, new_stock: schemas.BaseStock):
    db_stock = model.Fund(name=new_stock.name, fa_name=new_stock.fa_name)
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock


def get_or_create_stock(db: Session, new_stock: model.Stock):
    in_db = db.query(model.Stock).filter(model.Stock.name == new_stock.name).first()
    if in_db == None:
        db.add(new_stock)
        db.commit()
        # db.refresh(new_stock)
    return new_stock


def create_stock_bubble2(
    db: Session, newBubble: schemas.BaseBubbleData, stock_name: str
):
    db_bubble = model.BubbleData(**newBubble.model_dump(), stock_name=stock_name)
    db.add(db_bubble)
    db.commit()
    return db_bubble


def create_stock_bubble(db: Session, newBubble: model.BubbleData):
    db.add(newBubble)
    db.commit()
    db.refresh(newBubble)
    return newBubble


def get_bubbleList(db: Session, skip: int = 0, limit: int = 100):
    list = db.query(model.BubbleData).offset(skip).limit(limit).all()
    return list


def get_stockList(db: Session, skip: int = 0, limit: int = 100):
    list = db.query(model.Stock).offset(skip).limit(limit).all()
    return list


def get_latest_bubble_data(db: Session, skip: int = 0, limit: int = 100):
    funds = db.query(model.Stock).all()
    bubble_list = []
    for f in funds:
        bubble_list.append(f.bubbles[-1])
    return bubble_list


def get_stock_bubble_data(db: Session, stock_name: str):
    bubble_list = (
        db.query(model.BubbleData)
        .filter(model.BubbleData.stock_name == stock_name)
        .all()
    )

    return bubble_list
