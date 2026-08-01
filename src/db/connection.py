import pyodbc

# =========================
# DB接続
# =========================
def get_connection():

    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=HP-PC;"
        "DATABASE=EquipmentDB;"
        "Trusted_Connection=yes;"
    )

    return conn