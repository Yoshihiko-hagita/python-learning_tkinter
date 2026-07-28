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

# =========================
# ユーザー登録
# =========================
def insert_user(
    employee_id,
    user_name,
    password,
    authority,
    mail_address
):

    conn = get_connection()

    cursor = conn.cursor()

    sql = """
    INSERT INTO tbl_users
    (
        employee_id,
        user_name,
        password_hash,
        authority,
        mail_address
    )
    VALUES
    (
        ?, ?, ?, ?, ?
    )
    """

    cursor.execute(
        sql,
        (
            employee_id,
            user_name,
            password,
            authority,
            mail_address
        )
    )

    conn.commit()

    conn.close()

    

# =========================
# ユーザー取得
# =========================
def get_user(employee_id):

    conn = get_connection()

    cursor = conn.cursor()

    sql = """
    SELECT
        employee_id,
        user_name,
        password_hash,
        authority
    FROM tbl_users
    WHERE employee_id = ?
    """

    cursor.execute(
        sql,
        (employee_id,)
    )

    row = cursor.fetchone()

    conn.close()

    return row