import os
from dotenv import load_dotenv

load_dotenv()
print("TEST ---------------------------------")
print(os.environ.get("POSTGRES_PORT"))
print(os.environ.get("POSTGRES_USER"))
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")

POSTGRES_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
print(POSTGRES_DATABASE_URL)
print("TEST ---------------------------------")