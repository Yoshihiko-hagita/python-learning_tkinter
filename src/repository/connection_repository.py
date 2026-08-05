import pyodbc


# =========================
# DB接続-[repository]
# =========================
def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=HP-PC;"
        "DATABASE=EquipmentDB;"
        "Trusted_Connection=yes;"
    )