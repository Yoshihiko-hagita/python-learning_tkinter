from src.repository.user_repository import get_connection

# =========================
# ユーザー検索-[repository]
# =========================
def find_users(employee_id=None):

    conn = get_connection()

    try:
        cursor = conn.cursor()

        sql = """
        SELECT
            employee_id,
            name,
            authority,
            mail_address
        FROM tbl_users
        """

        params = ()

        if employee_id:
            sql += " WHERE employee_id = ?"
            params = (employee_id,)

        cursor.execute(sql, params)

        rows = cursor.fetchall()

        return rows

    finally:
        conn.close()