

#--------------------------------------------------
# 社員ID入力時の形式チェック-[Method]
#--------------------------------------------------
def validate_employee_id_chars(value):

    if value == "":
        return True

    if len(value) > 8:
        return False

    for c in value:

        if not (
            c.isascii() and
            (c.isalnum() or c == "-")
        ):
            return False

    return True

#--------------------------------------------------
# パスワード入力時の形式チェック-[Method]
#--------------------------------------------------
def validate_password_chars(value):

    if value == "":
        return True

    for c in value:

        if not (
            c.isascii() and
            (c.isalnum() or c == "-"or c == "@")
        ):
            return False

    return True

#--------------------------------------------------
# 入力チェック-[Method]
#--------------------------------------------------
def input_validation(user, mode):

    if not user.employee_id:
        return False, "社員IDを入力してください。"
    
    if not user.name:
        return False, "氏名を入力してください。"
    
    if user.mail_address and "@" not in user.mail_address:
        return False, "メールアドレスの形式が正しくありません。"
    
    if mode == "New":

        if not user.password:
            return False, "パスワードを入力してください。"

        if not user.password_confirm:
            return False, "パスワード確認を入力してください。"
        
    if mode == "Edit":

        # 未入力ならパスワード変更なし
        if not user.password and not user.password_confirm:
            return True, ""

        # 片方だけ入力
        if not user.password or not user.password_confirm:
            return False, "パスワードと確認用を両方入力してください。"
    
    if user.password != user.password_confirm:
        return False, "パスワードが一致しません。"
    
    if not (
        any(c.isupper() for c in user.password)
        and any(c.islower() for c in user.password)
        and any(c.isdigit() for c in user.password)
        and ("-" in user.password or "@" in user.password)
    ):
        return False, "パスワードは半角英大文字、半角英小文字、半角数字、記号(-、@)をそれぞれ1文字以上含めてください。"
    
    return True, ""