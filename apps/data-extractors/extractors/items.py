from datetime import datetime

class StockUrl:
    url = ""
    name = ""
    fa_name = ""

    def __init__(self, url, name, fa_name) -> None:
        self.url = url
        self.name = name
        self.fa_name = fa_name

class StockData(StockUrl):
    last_price=0
    nav_price=0
    date=datetime.now()
    def __init__(self,url,name,fa_name,last_price,nav_price,date=datetime.now()):
        super().__init__(url,name,fa_name)
        self.last_price=last_price
        self.nav_price=nav_price
        self.date=date