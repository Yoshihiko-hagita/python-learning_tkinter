import bcrypt

from src.repository.user_repository import get_user

#--------------------------------------------------
# ログイン前-入力内容の確認-[Method]
#--------------------------------------------------
def validate_password_policy(password):
    
    if not (
        any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
        and ("-" in password or "@" in password)
    ):
        return (
            False,
            "パスワードは半角英大文字、半角英小文字、半角数字、記号(-、@)をそれぞれ1文字以上含めてください。"
        )

    return (
        True,
        None
    )

#--------------------------------------------------
# ログイン処理-[Method]
#--------------------------------------------------
def login_process(employee_id, password):

    user = get_user(employee_id)

    # 社員IDが存在しない
    if user is None:
        return (False,"社員IDまたはパスワードが違います。")

    # password_hash取得
    password_hash = user[2]

    # パスワード照合
    if not bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash.encode("utf-8")
    ):
        return (False,"社員IDまたはパスワードが違います。")

    return (True,None)
