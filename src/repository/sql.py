from src.db.connection import get_connection

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
# ユーザー更新
# =========================
def update_user(
    employee_id,
    user_name,
    authority,
    mail_address,
    password_hash=None
):

    conn = get_connection()

    cursor = conn.cursor()

    if password_hash:

        sql = """
        UPDATE tbl_users
        SET
            user_name = ?,
            authority = ?,
            mail_address = ?,
            password_hash = ?,
            updated_at = SYSDATETIME()
        WHERE employee_id = ?
        """
        cursor.execute(
            sql,
            (
                user_name,
                authority,
                mail_address,
                password_hash,
                employee_id
            )
    )

    else:

        sql = """
        UPDATE tbl_users
        SET
            user_name = ?,
            authority = ?,
            mail_address = ?,
            updated_at = SYSDATETIME()
        WHERE employee_id = ?
        """

        cursor.execute(
            sql,
            (
                user_name,
                authority,
                mail_address,
                employee_id
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