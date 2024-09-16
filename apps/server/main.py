from fastapi import FastAPI, Depends
from model import stock as StockModel
from database.main import SessionLocal, engine, Session
from schemas import stock as SchemaStock
from crud import stock as StockCrud

StockModel.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/stock", response_model=list[SchemaStock.Stock])
def get_stock_list(db: Session = Depends(get_db)):
    data = StockCrud.get_stockList(db)
    return data


@app.get("/bubbles", response_model=list[SchemaStock.BubbleData])
def get_all_bubbles(db: Session = Depends(get_db)):
    data = StockCrud.get_bubbleList(db)
    return data


@app.get("/bubbles/latest", response_model=list[SchemaStock.BubbleData])
def get_today_bubble(db: Session = Depends(get_db)):
    data = StockCrud.get_latest_bubble_data(db)
    return data


@app.get("/bubbles/{stock_name}", response_model=list[SchemaStock.BubbleData])
def get_today_bubble(stock_name: str, db: Session = Depends(get_db)):
    data = StockCrud.get_stock_bubble_data(db, stock_name)
    return data
