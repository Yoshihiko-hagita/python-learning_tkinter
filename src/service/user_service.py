from src.db.sql_user_search import search_user
from src.db.sql_user_get import get_user

# 社員情報検索
def get_user_list(employee_id):

    rows = search_user(employee_id)

    users = []

    for row in rows:
        users.append({
            "employee_id": row.employee_id,
            "user_name": row.user_name,
            "authority": row.authority
        })

    return users

# 社員情報取得
def get_user_info(employee_id):

    row = get_user(employee_id)

    return row

