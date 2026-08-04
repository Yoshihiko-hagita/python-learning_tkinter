import bcrypt
from src.repository.connection_repository import get_connection


# =========================
# ユーザー登録
# =========================
def insert_user(user):

    password_hash = bcrypt.hashpw(
        user.password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO tbl_users
    (
        employee_id,
        name,
        mail_address,
        authority,
        password_hash
    )
    VALUES
    (
        ?, ?, ?, ?, ?
    )
    """

    cursor.execute(
        sql,
        (
            user.employee_id,
            user.name,
            user.mail_address,
            user.authority,
            password_hash
        )
    )

    conn.commit()

    conn.close()

# =========================
# ユーザー更新
# =========================
def update_user(user):

    conn = get_connection()
    cursor = conn.cursor()

    if user.password:

        password_hash = bcrypt.hashpw(
            user.password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        sql = """
        UPDATE tbl_users
        SET
            name = ?,
            mail_address = ?,
            authority = ?,
            password_hash = ?
        WHERE employee_id = ?
        """

        cursor.execute(
            sql,
            (
                user.name,
                user.mail_address,
                user.authority,
                password_hash,
                user.employee_id
            )
        )

    else:

        sql = """
        UPDATE tbl_users
        SET
            name = ?,
            mail_address = ?,
            authority = ?
        WHERE employee_id = ?
        """

        cursor.execute(
            sql,
            (
                user.name,
                user.mail_address,
                user.authority,
                user.employee_id
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
        name,
        password_hash,
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