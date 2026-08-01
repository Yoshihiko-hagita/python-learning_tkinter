from src.repository.sql import get_connection


def get_user(employee_id):

    conn = get_connection()

    cursor = conn.cursor()

    sql = """
    SELECT
        employee_id,
        user_name,
        mail_address,
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
