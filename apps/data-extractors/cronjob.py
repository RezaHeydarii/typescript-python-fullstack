print("==================importing FUND_URL====================")
from extractors.constants import FUND_URLS

print("===================importing exporter===============")
from extractors.exporters import export_stock_bubble_into_sql

print("=====================importing extractor=============")
from extractors.extractors import extract_stock_data

print("===================================================")
print("Start getting funds data")

for fund in FUND_URLS:
    stock = extract_stock_data(fund)
    try:
        if stock != None:
            export_stock_bubble_into_sql(stock)
    except Exception as err:
        print(err)

print("Funds data received and stored in db")
print("============================================")
