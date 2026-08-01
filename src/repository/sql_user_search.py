from src.repository.sql import get_connection


def search_user(employee_id):

    conn = get_connection()
    cursor = conn.cursor()

    if employee_id:
      sql = """
      SELECT
          employee_id,
          user_name,
          authority
      FROM tbl_users
      WHERE employee_id = ?
      """
      cursor.execute(
        sql,
        (employee_id,)
      )
    else:
      sql = """
      SELECT
          employee_id,
          user_name,
          authority
      FROM tbl_users
      """
      cursor.execute(sql)

    rows = cursor.fetchall()

    conn.close()

    return rows