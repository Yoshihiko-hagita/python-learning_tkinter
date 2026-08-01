import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

from src.service import login_service

class LogInFrame(tk.Frame):

    def __init__(self, parent, frame_manager):
        super().__init__(parent)
        self.frame_manager = frame_manager

        #=========================
        # 入力エリア
        #=========================
        input_frame = tk.Frame(self,pady=10)
        input_frame.place(relx=0.25,rely=0.30)

        #=========================
        # 入力ラベル
        #=========================
        label_placeholder = tk.Label(
            input_frame,
            text="※ 半角英数字とハイフン(-)のみ入力可能です",
            font=("Meiryo UI", 8),
            fg="red"
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
            font=("Meiryo UI", 10)
        )

        label_id.grid(
            row=1,
            column=0,
            sticky="w"
        )

        #=========================
        # 社員ID入力
        #=========================
        vcmd_id = (self.register(login_service.validate_employee_id),"%P")

        self.id_var = tk.StringVar(value="ABC-1234")

        self.entry_id = ttk.Entry(
            input_frame,
            textvariable=self.id_var,
            font=("Meiryo UI", 12),
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
        )

        label_password.grid(row=3,column=0)

        #=========================
        # パスワード入力
        #=========================
        vcmd_password = (self.register(login_service.validate_password),"%P")

        self.password_var = tk.StringVar(value="Awertyuiop@123")
        self.entry_password = ttk.Entry(
            input_frame,
            textvariable=self.password_var,
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
    # 入力チェック(処理)
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
    # Enterキーでログイン(処理)
    #==================================================
    def enter_login(self, event=None):

        if "disabled" not in self.button_login.state():
            self.login()
            
    # =================================================
    # ログイン処理(処理)
    #==================================================
    def login(self):

        employee_id = self.entry_id.get().strip()
        password = self.entry_password.get()

        success, message = login_service.pre_login_check(password)

        if not success:
            messagebox.showerror("ログインエラー",message)
            self.button_login.state(["disabled"])
            self.entry_password.focus_set()
            return

        success, message = login_service.login_process(employee_id,password)

        if not success:
            messagebox.showerror("ログインエラー",message)
            return

        self.frame_manager.show_frame("HomeFrame")