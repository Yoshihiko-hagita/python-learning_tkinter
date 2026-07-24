import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LogInFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#C5C3C3")

        #=========================
        # 入力エリア
        #=========================

        input_frame = tk.Frame(
            self,
            bg="#C5C3C3",
            pady=10
        )

        input_frame.place(
            relx=0.25,
            rely=0.30
        )

        #=========================
        # 入力ラベル
        #=========================

        label_placeholder = tk.Label(
            input_frame,
            text="※ 半角英数字とハイフン(-)のみ入力可能です",
            font=("Meiryo UI", 8),
            fg="red",
            bg="#C5C3C3"
        )

        label_placeholder.grid(
            row=0,
            column=1,
            sticky="w",
            padx=(20, 0)
        )

        label_id = tk.Label(
            input_frame,
            text="社員ID",
            font=("Meiryo UI", 10),
            bg="#C5C3C3"
        )

        label_id.grid(
            row=1,
            column=0,
            sticky="w"
        )

        #=========================
        # 社員ID入力
        #=========================

        vcmd_id = (
            self.register(self.validate_employee_no),
            "%P"
        )

        self.entry_id = ttk.Entry(
            input_frame,
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
        self.entry_id.bind("<KeyRelease>", self.check_input)

        #=========================
        # パスワードラベル
        #=========================
        label_pass_placeholder = tk.Label(
            input_frame,
            text="※ 10文字以上で大小英文字、数字、記号(-又は＠)を組み合わせてください",
            font=("Meiryo UI", 8),
            fg="red",
            bg="#C5C3C3"
        )

        label_pass_placeholder.grid(
            row=2,
            column=1,
            sticky="w",
            padx=(20, 0),
            pady=(20, 0)
        )

        label_password = tk.Label(
            input_frame,
            text="パスワード",
            font=("Meiryo UI",10),
            bg="#C5C3C3"
        )

        label_password.grid(
            row=3,
            column=0
        )

        #=========================
        # パスワード入力
        #=========================

        vcmd_password = (
            self.register(self.validate_password_no),
            "%P"
        )

        self.entry_password = ttk.Entry(
            input_frame,
            show="*",
            font=("Meiryo UI",12),
            width=20,
            validate="key",
            validatecommand=vcmd_password
        )

        self.entry_password.grid(
            row=3,
            column=1,
            sticky="w",
            padx=(20, 0)
        )
        self.entry_password.bind("<KeyRelease>", self.check_input)
        self.entry_password.bind("<Return>",self.enter_login)

        #=========================
        # ログインボタン
        #=========================

        self.button_login = ttk.Button(
            input_frame,
            text="ログイン",
            command=self.login
        )

        self.button_login.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=(30, 0),#上下余白
            padx=(0, 70) #左右余白
        )

        self.check_input()
        self.button_login .bind("<Return>",self.enter_login)

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
                (c.isalnum() or c == "-"or c == "@")
            ):
                return False

        return True
    
    #==================================================
    # 入力チェック
    #==================================================
    def check_input(self, event=None):# event=Noneはbind()で呼び出すときに必要 

        if (
            len(self.entry_id.get()) == 8
            and len(self.entry_password.get()) >= 10
        ):
            self.button_login.state(["!disabled"])
        else:
            self.button_login.state(["disabled"])

    #==================================================
    # ログインチェック
    #==================================================
    def check_login(self):
        password = self.entry_password.get()
        if not (
            any(c.isupper() for c in password)  # 大文字
            and any(c.islower() for c in password)  # 小文字
            and any(c.isdigit() for c in password)  # 数字
            and ("-" in password or "@" in password)
        ):
            messagebox.showerror("エラー","パスワードは半角英大文字、半角英小文字、半角数字、記号(-、@)を\nそれぞれ1文字以上含めてください。")
            self.entry_password.delete(0, tk.END)
            self.check_input()
            self.entry_password.focus_set()
            return False

        return True
    
    
    #==================================================
    # Enterキーでログイン
    #==================================================
    def enter_login(self, event=None):

        if "disabled" not in self.button_login.state():
            self.login()


    #==================================================
    # ログイン
    #==================================================

    def login(self):
        if not self.check_login():
            return
        app = self.master
        app.show_frame(
        "MainFrame"
    )