from src.repository import fimd_user_repositry
from src.repository.sql_user_get import get_user

#-------------------------------------------
# 社員情報検索-[Method]
#-------------------------------------------
def get_user_list(employee_id):

    rows = fimd_user_repositry.find_users(employee_id)

    users = []

    for row in rows:
        users.append({
            "employee_id": row.employee_id,
            "name": row.name,
            "authority": row.authority,
            "mail_address": row.mail_address
        })

    return users

# 社員情報取得
def get_user_info(employee_id):

    row = get_user(employee_id)

    return row

