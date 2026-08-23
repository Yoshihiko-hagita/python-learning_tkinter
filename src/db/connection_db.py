import os

import pyodbc
from dotenv import load_dotenv

load_dotenv()


# =========================
# DB接続
# =========================
def get_connection():
    return pyodbc.connect(
        f"DRIVER={{{os.getenv('DB_DRIVER')}}};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_DATABASE')};"
        "Trusted_Connection=yes;"
    )
