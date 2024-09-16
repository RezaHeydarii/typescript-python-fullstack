from extractors.items import StockUrl, StockData
import requests


def extract_stock_data(stock: StockUrl, retry: int = 3):
    try:
        res = requests.get(stock.url)
        mainSection = str(res.content).split(";")[0]
        prices = str(mainSection).split(",")
        print("stock data received ", stock.name)
        return StockData(
            url=stock.url,
            name=stock.name,
            fa_name=stock.fa_name,
            nav_price=prices[-1],
            last_price=prices[2],
        )
    except:
        if retry == 0:
            print(f"cannot extract data from {stock.name}, skipping...")
            return None

        print(f"cannot resolve {stock.name}, retrying...")
        return extract_stock_data(stock, retry=retry - 1)
