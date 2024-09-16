import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = "mysql+mysqlconnector://{user}:{password}@{host}/{db}".format(
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    db=os.getenv("DATABASE_DB_NAME")
)

