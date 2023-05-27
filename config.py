import dotenv
import os


# Initialize environment variables
dotenv.load_dotenv('/home/elizabeth/managing_db/.env')
conn_row = os.getenv("CONNECTION_ROW")

host = os.getenv("HOST")
user = os.getenv("USER")
passwd = os.getenv("PASSWD")
database = os.getenv("DB")
