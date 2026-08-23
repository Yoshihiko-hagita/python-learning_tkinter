import bcrypt

from src.config.settings import PASSWORD_HASH_ROUNDS
from src.db import connection_db


# =========================================
# ユーザー取得-ログイン用(password_hash 無し)
# =========================================
def get_user_for_login(employee_id):

    conn = connection_db.get_connection()

    try:
        cursor = conn.cursor()

        sql = """
        SELECT
            employee_id,
            name,
            mail_address,
            authority
        FROM tbl_users
        WHERE employee_id = ?
        """

        cursor.execute(sql, (employee_id,))

        row = cursor.fetchone()

        return row

    finally:
        conn.close()


# =====================================
# ユーザー取得-通常 (password_hash 有り)
# =====================================
def get_user(employee_id):

    conn = connection_db.get_connection()

    try:
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

        cursor.execute(sql, (employee_id,))

        row = cursor.fetchone()

        return row

    finally:
        conn.close()


# =========================
# ユーザー検索
# =========================
def find_users(employee_id=None):

    conn = connection_db.get_connection()

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

        if employee_id :
            sql += " WHERE employee_id = ?"
            params = (employee_id,)

        cursor.execute(sql, params)

        rows = cursor.fetchall()

        return rows

    finally:
        conn.close()


# =========================
# ユーザー登録
# =========================
def insert_user(user):

    password_hash = bcrypt.hashpw(
        user.password.encode("utf-8"),
        bcrypt.gensalt(rounds=PASSWORD_HASH_ROUNDS),
    ).decode("utf-8")

    conn = connection_db.get_connection()

    try:
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
                user.mail_address or None,
                user.authority,
                password_hash,
            ),
        )

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


# =========================
# ユーザー更新
# =========================
def update_user(user):

    conn = connection_db.get_connection()

    try:
        cursor = conn.cursor()

        if user.password:
            password_hash = bcrypt.hashpw(
                user.password.encode("utf-8"),
                bcrypt.gensalt(rounds=PASSWORD_HASH_ROUNDS),
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
                    user.mail_address or None,
                    user.authority,
                    password_hash,
                    user.employee_id,
                ),
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
                    user.mail_address or None,
                    user.authority,
                    user.employee_id,
                ),
            )

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


# =========================
# ユーザー削除
# =========================
def delete_user(employee_id):

    conn = connection_db.get_connection()

    try:
        cursor = conn.cursor()

        sql = """
        DELETE FROM tbl_users
        WHERE employee_id = ?
        """

        cursor.execute(sql, (employee_id,))

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()
