import tkinter as tk
import bcrypt
from tkinter import ttk
from tkinter import messagebox
from src.db.sql import insert_user, get_user
from src.gui.frames.sidemenu_frame import SideMenuFrame
from src.service.user_service import get_user_info


class UserRegisterFrame(tk.Frame):

    def __init__(self, parent):

        super().__init__(
            parent,
            bg="white"
        )

        #=========================
        # サイドメニュー(左側)
        #=========================
        self.sidemenu_frame = SideMenuFrame(self)

        self.sidemenu_frame.pack(
            side="left",
            fill="y"
        )

        #=========================
        # コンテンツ(右側)
        #=========================
        user_register_frame = tk.Frame(
            self
        )

        user_register_frame.pack(
            side="right",
            fill="both",# 横・縦に伸ばす
            expand=True # 余ったスペースを使う
        )

        # =========================
        # 新規登録フレーム
        # =========================
        self.nwe_register_frame = ttk.LabelFrame(
            user_register_frame,
            text="ユーザー新規登録",
        )

        self.nwe_register_frame.pack(
            fill="both",
            padx=(5,5)
        )

        # =========================
        # 社員ID
        # =========================
        # 社員ID 注意書き
        label_new_placeholder = tk.Label(
            self.nwe_register_frame,
            text="※ (必須)半角英数字とハイフン(-)のみ入力可能です",
            font=("Meiryo UI", 8),
            fg="red"
        )

        label_new_placeholder.grid(
            row=0,
            column=1,
            sticky="w",
            padx=(20, 0)
        )
        # 社員IDラベル
        label_new_id = tk.Label(
            self.nwe_register_frame,
            text="社員ID         :",
            font=("Meiryo UI", 10)
        )

        label_new_id.grid(
            row=1,
            column=0,
            sticky="w",
            padx=(10, 0)
        )

        # 社員ID入力
        vcmd_id = (
            self.register(self.validate_employee_no),
            "%P"
        )

        self.new_entry_id = ttk.Entry(
            self.nwe_register_frame,
            font=("Meiryo UI",12),
            width=20,
            validate="key",
            validatecommand=vcmd_id
        )

        self.new_entry_id.grid(
            row=1,
            column=1,
            sticky="w",
            padx=(20, 0)
        )

        self.new_entry_id.focus_set()

        # =========================
        # 氏名
        # =========================
        # 氏名 注意書き
        label_newname_placeholder = tk.Label(
            self.nwe_register_frame,
            text="※ (必須)",
            font=("Meiryo UI", 8),
            fg="red"
        )

        label_newname_placeholder.grid(
            row=2,
            column=1,
            sticky="w",
            padx=(20, 0),
            pady=(10, 0)
        )
        # 氏名ラベル
        label_newname = tk.Label(
            self.nwe_register_frame,
            text="氏 名        　　:",
            font=("Meiryo UI", 10)
        )

        label_newname.grid(
            row=3,
            column=0,
            sticky="w",
            padx=(10, 0)
        )

        # 氏名入力
        self.new_entry_name = ttk.Entry(
            self.nwe_register_frame,
            font=("Meiryo UI",12),
            width=20,
        )

        self.new_entry_name.grid(
            row=3,
            column=1,
            sticky="w",
            padx=(20, 0)
        )
        # =========================
        # メールアドレス
        # =========================
        # メール 注意書き
        label_newmail_placeholder = tk.Label(
            self.nwe_register_frame,
            text="※ (任意)",
            font=("Meiryo UI", 8),
            fg="gray"
        )

        label_newmail_placeholder.grid(
            row=4,
            column=1,
            sticky="w",
            padx=(20, 0),
            pady=(10, 0)
        )
        # メールラベル
        label_newmail = tk.Label(
            self.nwe_register_frame,
            text="メールアドレス   :",
            font=("Meiryo UI", 10)
        )

        label_newmail.grid(
            row=5,
            column=0,
            sticky="w",
            padx=(10, 0)
        )

        # メール入力
        self.new_entry_mail = ttk.Entry(
            self.nwe_register_frame,
            font=("Meiryo UI",12),
            width=20,
        )

        self.new_entry_mail.grid(
            row=5,
            column=1,
            sticky="w",
            padx=(20, 0)
        )

        # =========================
        # 権限
        # =========================
        # 権限 注意書き
        label_newauthority_placeholder = tk.Label(
            self.nwe_register_frame,
            text="※ (必須)",
            font=("Meiryo UI", 8),
            fg="red"
        )

        label_newauthority_placeholder.grid(
            row=6,
            column=1,
            sticky="w",
            padx=(20, 0),
            pady=(10, 0)
        )
        # 権限ラベル
        label_newauthority = tk.Label(
            self.nwe_register_frame,
            text="権 限          　:",
            font=("Meiryo UI", 10)
        )

        label_newauthority.grid(
            row=7,
            column=0,
            sticky="w",
            padx=(10, 0)
        )

        # 権限ドロップダウン
        self.new_entry_authority = ttk.Combobox(
            self.nwe_register_frame,
            font=("Meiryo UI",10),
            width=20,
            values=["管理者", "一般"],
            state="readonly"
        )

        self.new_entry_authority.grid(
            row=7,
            column=1,
            sticky="w",
            padx=(20, 0)
        )

        # 権限初期値
        self.new_entry_authority.current(1)

        # =========================
        # パスワード
        # =========================
        # パスワードラベル 注意書き
        label_new_pass_placeholder = tk.Label(
            self.nwe_register_frame,
            text="※ (必須)10文字以上で大小英文字、数字、記号(-又は＠)を組み合わせてください",
            font=("Meiryo UI", 8),
            fg="red",
        )

        label_new_pass_placeholder.grid(
            row=10,
            column=1,
            sticky="w",
            padx=(20, 0),
            pady=(10, 0)
        )

        # パスワードラベル
        label_new_password = tk.Label(
            self.nwe_register_frame,
            text="パスワード      　:",
            font=("Meiryo UI",10),
        )

        label_new_password.grid(
            row=11,
            column=0,
            sticky="w",
            padx=(10, 0),
            pady=(0, 20)
        )

        # パスワード入力
        vcmd_password = (
            self.register(self.validate_password_no),
            "%P"
        )
        self.new_entry_password = ttk.Entry(
            self.nwe_register_frame,
            font=("Meiryo UI",12),
            width=20,
            validate="key",
            validatecommand=vcmd_password,
            show="*"
        )

        self.new_entry_password.grid(
            row=11,
            column=1,
            sticky="w",
            padx=(20, 0),
            pady=(0, 20)
        )

        # パスワードラベル(確認用)
        label_new_password_confirm = tk.Label(
            self.nwe_register_frame,
            text="パスワード (確認) :",
            font=("Meiryo UI",9),
        )

        label_new_password_confirm.grid(
            row=12,
            column=0,
            sticky="w",
            padx=(10, 0),
            pady=(0, 20)
        )

        # パスワード入力(確認用)
        vcmd_password = (
            self.register(self.validate_password_no),
            "%P"
        )
        self.new_entry_password_confirm = ttk.Entry(
            self.nwe_register_frame,
            font=("Meiryo UI",12),
            width=20,
            validate="key",
            validatecommand=vcmd_password,
            show="*"
        )

        self.new_entry_password_confirm.grid(
            row=12,
            column=1,
            sticky="w",
            padx=(20, 0),
            pady=(0, 20)
        )

        # パスワード表示用変数
        self.show_password_var = tk.BooleanVar()

        # パスワード表示チェックボックス
        self.check_show_password = tk.Checkbutton(
            self.nwe_register_frame,
            text="パスワード表示",
            variable=self.show_password_var,
            command=self.toggle_password
        )

        self.check_show_password.grid(
            row=13,
            column=0,
            sticky="w",
            padx=(10, 0)
        )

        # =========================
        # underframe
        # =========================
        register_under_frame = ttk.Frame(
            user_register_frame
        )

        register_under_frame.pack(
            fill="both"
        )

        #戻るボタン
        self.button_new_back = ttk.Button(
            register_under_frame,
            text="戻る" ,
            command=lambda: self.master.show_frame("UserManagementFrame")
        )

        self.button_new_back.grid(
            column=0,
            row=0,
            padx=(110,50),
            pady=(30,15)
        )

        #保存ボタン
        self.button_new_save = ttk.Button(
            register_under_frame,
            text="保存",
            command=self.save_user
        )

        self.button_new_save.grid(
            column=1,
            row=0,
            padx=(0,50),
            pady=(30,15)
        )

        #キャンセルボタン
        self.button_new_cancel = ttk.Button(
            register_under_frame,
            text="キャンセル",
            command=self.clear_form
        )

        self.button_new_cancel.grid(
            column=2,
            row=0,
            padx=(0,50),
            pady=(30,15)
        )

    # =========================
    # パスワード表示切替
    # =========================
    def toggle_password(self):

        if self.show_password_var.get():

            self.new_entry_password.config(
                show=""
            )

            self.new_entry_password_confirm.config(
                show=""
            )

        else:

            self.new_entry_password.config(
                show="*"
            )

            self.new_entry_password_confirm.config(
                show="*"
            )


    #==================================================
    # 社員IDチェック
    #==================================================
    def validate_employee_no(self, new_value):

        if new_value == "":
            return True

        if len(new_value) > 8:
            return False

        for c in new_value:

            if not (
                c.isascii() and
                (c.isalnum() or c == "-")
            ):
                return False

        return True
    
    #==================================================
    # パスワードチェック
    #==================================================
    def validate_password_no(self, new_value):

        if new_value == "":
            return True

        for c in new_value:

            if not (
                c.isascii() and
                (c.isalnum() or c == "-" or c == "@")
            ):
                return False

        return True

    # =========================
    # button処理
    # =========================
    def  clear_form(self):
        self.new_entry_id.delete(0, tk.END)
        self.new_entry_name.delete(0, tk.END)
        self.new_entry_mail.delete(0, tk.END)
        self.new_entry_authority.current(1)
        self.new_entry_password.delete(0, tk.END)
        self.new_entry_password_confirm.delete(0, tk.END)
        self.new_entry_id.focus_set()
    
    # =========================
    # ユーザー登録
    # =========================
    def save_user(self):
        employee_id = self.new_entry_id.get()
        user_name = self.new_entry_name.get()
        mail_address = self.new_entry_mail.get()
        authority = self.new_entry_authority.get()
        password = self.new_entry_password.get()
        password_confirm = self.new_entry_password_confirm.get()

        if password != password_confirm:
            messagebox.showerror(
                "入力エラー",
                "パスワードが一致しません。"
            )

            self.new_entry_password.focus_set()
            return

        password_hash = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        # 社員ID
        if not employee_id:
            messagebox.showerror(
                "入力エラー",
                "社員IDを入力してください。"
            )

            self.new_entry_id.focus_set()
            return
        
        if len(employee_id) != 8:

            messagebox.showerror(
                "入力エラー",
                "社員IDは8文字で入力してください。"
            )
            return

        # 社員ID重複チェック
        user = get_user(employee_id)

        if user is not None:

            messagebox.showerror(
                "入力エラー",
                "その社員IDは既に登録されています。"
            )

            self.new_entry_id.focus_set()

            return

        # 氏名
        if not user_name:
            messagebox.showerror(
                "入力エラー",
                "氏名を入力してください。"
            )

            self.new_entry_name.focus_set()
            return


        # パスワード
        if not password:
            messagebox.showerror(
                "入力エラー",
                "パスワードを入力してください。"
            )

            self.new_entry_password.focus_set()
            return
        
        if len(password) < 10:

            messagebox.showerror(
                "入力エラー",
                "パスワードは10文字以上で入力してください。"
            )

            self.new_entry_password.focus_set()

            return
        
        if not (
                any(c.isupper() for c in password)
                and any(c.islower() for c in password)
                and any(c.isdigit() for c in password)
                and ("-" in password or "@" in password)
            ):

            messagebox.showerror(
                "入力エラー",
                "パスワードは半角英大文字、半角英小文字、半角数字、記号(-、@)をそれぞれ1文字以上含めてください。"
            )

            self.new_entry_password.focus_set()

            return

        if authority == "管理者":
            authority = "ADMIN"
        else:
            authority = "USER"

        try:

            insert_user(
                employee_id,
                user_name,
                password_hash,
                authority,
                mail_address if mail_address else None
            )

            messagebox.showinfo(
                "完了",
                "登録しました。"
            )

        except Exception as e:

            messagebox.showerror(
                "エラー",
                str(e)
        )
                
    # =========================
    # show処理
    # =========================
    def on_show(self, employee_id=None):

        self.button_new_cancel.config(
            state="disabled"
        )

        self.nwe_register_frame.config(
            text="ユーザー編集"
        )

        user = get_user_info(employee_id)

        self.new_entry_id.delete(
            0,
            tk.END
        )

        self.new_entry_id.insert(
            0,
            user.employee_id
        )
        self.new_entry_name.delete(
            0,
            tk.END
        )

        self.new_entry_name.insert(
            0,
            user.user_name
        )

        self.new_entry_mail.delete(
            0,
            tk.END
        )

        if user.mail_address:
            self.new_entry_mail.insert(
                0,
                user.mail_address
            )

        if user.authority == "ADMIN":
            self.new_entry_authority.set("管理者")
        else:
            self.new_entry_authority.set("一般")

        self.new_entry_password.delete(0, tk.END)
        self.new_entry_password_confirm.delete(0, tk.END)
        self.new_entry_id.focus_set()