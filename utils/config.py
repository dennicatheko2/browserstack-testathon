import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL")
    BS_USERNAME = os.getenv("BROWSERSTACK_USERNAME")
    BS_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")
