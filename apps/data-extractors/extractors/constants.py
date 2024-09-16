from extractors.items import StockUrl
from dotenv import load_dotenv
import os

load_dotenv()


FUND_URLS = [
    StockUrl(
        url="your stock url",
        name="your stock url name",
        fa_name="نام فارسی سهام شما",
    ),
]

#DB_URL = "mysql+mysqlconnector://root:12345@0.0.0.0:3306/my-repo"
DB_URL = "mysql+mysqlconnector://{user}:{password}@{host}/{db}".format(
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    db=os.getenv("DATABASE_DB_NAME")
)
