import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    DB_URL = os.getenv("DB_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    expire_delta = int(os.getenv("Token_expire_date", 30))

settings = Settings() # -> create object from this class