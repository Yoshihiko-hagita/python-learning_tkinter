
from src.repository import user_repository


# -------------------------------------------
# 社員情報検索-[Method]
# -------------------------------------------
def get_user_list(employee_id):

    rows = user_repository.find_users(employee_id)

    users = []

    for row in rows:
        users.append(
            {
                "employee_id": row.employee_id,
                "name": row.name,
                "authority": row.authority,
                "mail_address": row.mail_address,
            }
        )

    return users


# =========================
# ユーザー削除
# =========================
def delete_user_by_employee_id(employee_id):

    user_repository.delete_user(employee_id)


# 社員情報取得
def get_user_info(employee_id):

    row = user_repository.get_user(employee_id)

    return row
