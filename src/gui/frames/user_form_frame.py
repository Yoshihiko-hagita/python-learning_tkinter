import tkinter as tk

from tkinter import ttk
from tkinter import messagebox
from src.models.user import User
from src.repository import user_repository
from src.gui.base_frame import BaseFrame
from src.gui.common_validators import ui_validator

class UserFormFrame(BaseFrame):
        
    AUTHORITY_MAP = {
            "管理者": "ADMIN",
            "一般": "USER",
        }
    
    def __init__(self, parent,frame_manager):

        super().__init__(parent,frame_manager,bg="white")

        #=========================
        # コンテンツ(右側)-[Widget]
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
        # フレーム-[Widget]
        # =========================
        self.user_form_frame = ttk.LabelFrame(
            user_register_frame
        )

        self.user_form_frame.pack(
            fill="both",
            padx=(5,5)
        )

        # =========================
        # 社員ID-[Widget]
        # =========================
        # 社員ID 注意書き
        label_id_important_notes = tk.Label(
            self.user_form_frame,
            text="※ (必須)半角英数字とハイフン(-)のみ入力可能です",
            font=("Meiryo UI", 8),
            fg="red"
        )

        label_id_important_notes.grid(
            row=0,
            column=1,
            sticky="w",
            padx=(20, 0)
        )
        # 社員IDラベル
        label_id = tk.Label(
            self.user_form_frame,
            text="社員ID         :",
            font=("Meiryo UI", 10)
        )

        label_id.grid(
            row=1,
            column=0,
            sticky="w",
            padx=(10, 0)
        )

        # 社員ID入力
        vcmd_id = (self.register(ui_validator.validate_employee_id_chars),"%P")

        self.entry_id = ttk.Entry(
            self.user_form_frame,
            font=("Meiryo UI",12),
            width=20,
            validate="key",
            validatecommand=vcmd_id
        )

        self.entry_id.grid(
            row=1,
            column=1,
            sticky="w",
            padx=(20, 0)
        )

        self.entry_id.focus_set()

        # =========================
        # 氏名-[Widget]
        # =========================
        # 氏名 注意書き
        label_name_important_notes = tk.Label(
            self.user_form_frame,
            text="※ (必須)",
            font=("Meiryo UI", 8),
            fg="red"
        )

        label_name_important_notes.grid(
            row=2,
            column=1,
            sticky="w",
            padx=(20, 0),
            pady=(10, 0)
        )
        # 氏名ラベル
        label_name = tk.Label(
            self.user_form_frame,
            text="氏 名        　　:",
            font=("Meiryo UI", 10)
        )

        label_name.grid(
            row=3,
            column=0,
            sticky="w",
            padx=(10, 0)
        )

        # 氏名入力
        self.entry_name = ttk.Entry(
            self.user_form_frame,
            font=("Meiryo UI",12),
            width=20,
        )

        self.entry_name.grid(
            row=3,
            column=1,
            sticky="w",
            padx=(20, 0)
        )
        # =========================
        # メールアドレス-[Widget]
        # =========================
        # メール 注意書き
        label_mail_important_notes = tk.Label(
            self.user_form_frame,
            text="※ (任意)",
            font=("Meiryo UI", 8),
            fg="gray"
        )

        label_mail_important_notes.grid(
            row=4,
            column=1,
            sticky="w",
            padx=(20, 0),
            pady=(10, 0)
        )
        # メールラベル
        label_mail = tk.Label(
            self.user_form_frame,
            text="メールアドレス   :",
            font=("Meiryo UI", 10)
        )

        label_mail.grid(
            row=5,
            column=0,
            sticky="w",
            padx=(10, 0)
        )

        # メール入力
        self.entry_maill = ttk.Entry(
            self.user_form_frame,
            font=("Meiryo UI",12),
            width=20,
        )

        self.entry_maill.grid(
            row=5,
            column=1,
            sticky="w",
            padx=(20, 0)
        )

        # =========================
        # 権限選択-[Widget]
        # =========================
        # 権限 注意書き
        label_authority_important_notes = tk.Label(
            self.user_form_frame,
            text="※ (必須)",
            font=("Meiryo UI", 8),
            fg="red"
        )

        label_authority_important_notes.grid(
            row=6,
            column=1,
            sticky="w",
            padx=(20, 0),
            pady=(10, 0)
        )
        # 権限ラベル
        label_authority = tk.Label(
            self.user_form_frame,
            text="権 限          　:",
            font=("Meiryo UI", 10)
        )

        label_authority.grid(
            row=7,
            column=0,
            sticky="w",
            padx=(10, 0)
        )

        # 権限ドロップダウン
        self.entry_authority = ttk.Combobox(
            self.user_form_frame,
            font=("Meiryo UI",10),
            width=20,
            values=["管理者", "一般"],
            state="readonly"
        )

        self.entry_authority.grid(
            row=7,
            column=1,
            sticky="w",
            padx=(20, 0)
        )

        # 権限初期値
        self.entry_authority.current(1)

        # =========================
        # パスワード-[Widget]
        # =========================
        # パスワードラベル 注意書き
        label_password_important_notes = tk.Label(
            self.user_form_frame,
            text="※ (必須)10文字以上で大小英文字、数字、記号(-又は＠)を組み合わせてください",
            font=("Meiryo UI", 8),
            fg="red",
        )

        label_password_important_notes.grid(
            row=10,
            column=1,
            sticky="w",
            padx=(20, 0),
            pady=(10, 0)
        )

        # パスワードラベル
        label_password = tk.Label(
            self.user_form_frame,
            text="パスワード      　:",
            font=("Meiryo UI",10),
        )

        label_password.grid(
            row=11,
            column=0,
            sticky="w",
            padx=(10, 0),
            pady=(0, 20)
        )

        # パスワード入力
        vcmd_password = (self.register(ui_validator.validate_password_chars),"%P")
        self.entry_password = ttk.Entry(
            self.user_form_frame,
            font=("Meiryo UI",12),
            width=20,
            validate="key",
            validatecommand=vcmd_password,
            show="*"
        )

        self.entry_password.grid(
            row=11,
            column=1,
            sticky="w",
            padx=(20, 0),
            pady=(0, 20)
        )

        # パスワードラベル(確認用)
        label_password_confirm = tk.Label(
            self.user_form_frame,
            text="パスワード (確認) :",
            font=("Meiryo UI",9),
        )

        label_password_confirm.grid(
            row=12,
            column=0,
            sticky="w",
            padx=(10, 0),
            pady=(0, 20)
        )

        # パスワード入力(確認用)
        vcmd_password = (self.register(ui_validator.validate_password_chars),"%P")
        self.entry_password_confirm = ttk.Entry(
            self.user_form_frame,
            font=("Meiryo UI",12),
            width=20,
            validate="key",
            validatecommand=vcmd_password,
            show="*"
        )

        self.entry_password_confirm.grid(
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
            self.user_form_frame,
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
        # underframe-[Widget]
        # =========================
        register_under_frame = ttk.Frame(user_register_frame)

        register_under_frame.pack(fill="both")

        #戻るボタン
        self.button_back = ttk.Button(
            register_under_frame,
            text="戻る" ,
            command=lambda: self.frame_manager.show_frame("UserManagementFrame")
        )

        self.button_back.grid(
            column=0,
            row=0,
            padx=(110,50),
            pady=(30,15)
        )

        #保存ボタン
        self.button_save = ttk.Button(
            register_under_frame,
            text="保存",
            command=self.save_user
        )

        self.button_save.grid(
            column=1,
            row=0,
            padx=(0,50),
            pady=(30,15)
        )

        #キャンセルボタン
        self.button_cancel = ttk.Button(
            register_under_frame,
            text="キャンセル",
            command=self.clear_form
        )

        self.button_cancel.grid(
            column=2,
            row=0,
            padx=(0,50),
            pady=(30,15)
        )

    #----------------------------
    # パスワード表示切替-[Method]
    #----------------------------
    def toggle_password(self):
        show = "" if self.show_password_var.get() else "*"
        self.entry_password.config(show=show)
        self.entry_password_confirm.config(show=show)

    #----------------------------
    # キャンセルボタン-[Method]
    #----------------------------
    def  clear_form(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_maill.delete(0, tk.END)
        self.entry_authority.current(1)
        self.entry_password.delete(0, tk.END)
        self.entry_password_confirm.delete(0, tk.END)
        self.entry_id.focus_set()
    
    #----------------------------
    # ユーザー登録-[Method]
    #----------------------------
    def save_user(self):

        user = User(
            employee_id=self.entry_id.get(),
            name=self.entry_name.get(),
            mail_address=self.entry_maill.get(),
            authority=self.AUTHORITY_MAP.get(self.entry_authority.get()),
            password=self.entry_password.get(),
            password_confirm=self.entry_password_confirm.get()
        )

        response,mesage =ui_validator.input_validation(user,self.mode)

        if not response:
            messagebox.showerror("入力エラー",mesage)
            return
        
        try:
            if self.mode == "New":
                user_repository.insert_user(user)

            else:
                user_repository.update_user(user)
            self.clear_form()

        except Exception as e:
            messagebox.showerror("エラー",str(e))
            return

    def set_user_info(self,user):

        self.user = user
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_maill.delete(0, tk.END)

        self.entry_id.insert(0, user["employee_id"])
        self.entry_name.insert(0, user["name"])

        if user["mail_address"]:
            self.entry_maill.insert(0, user["mail_address"])

        self.entry_authority.set(
            self.AUTHORITY_MAP.get(user["authority"], "")
        )
