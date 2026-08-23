import tkinter as tk
from tkinter import messagebox, ttk

from src.gui.base_frame import BaseFrame
from src.service import user_service


class UserManagementFrame(BaseFrame):
    def __init__(self, parent, frame_controller):

        super().__init__(parent, frame_controller, bg="white")

        # =========================
        # コンテンツ(右側)
        # =========================
        user_contents_frame = tk.Frame(self)

        user_contents_frame.pack(
            side="right",
            fill="both",  # 横・縦に伸ばす
            expand=True,  # 余ったスペースを使う
        )

        # =========================
        # ユーザー検索
        # =========================
        search_frame = ttk.LabelFrame(
            user_contents_frame,
            text="ユーザー検索",
        )

        search_frame.pack(fill="both")

        # ラベル
        label_id = tk.Label(search_frame, text=" 社員ID")

        label_id.grid(column=0, row=0, pady=(15, 15))

        # 入力エリア
        self.entry_id = tk.Entry(search_frame, font=("Meiryo UI", 12), width=25)

        self.entry_id.grid(column=1, row=0)

        # ボタン
        self.button_search = ttk.Button(
            search_frame, text="検索", command=self.search_user
        )

        self.button_search.grid(column=2, row=0, padx=(15, 0))

        # =========================
        # Treeview
        # =========================
        Treeview_frame = ttk.Frame(user_contents_frame)

        Treeview_frame.pack(fill="both", expand=True, padx=(5, 5))

        # Treeview
        self.tree = ttk.Treeview(
            Treeview_frame,
            columns=("employee_id", "name", "authority"),
            show="headings",
            height=5,
        )

        self.tree.heading("employee_id", text="社員ID")
        self.tree.heading("name", text="氏名")
        self.tree.heading("authority", text="権限")

        self.tree.column("employee_id", width=100)
        self.tree.column("name", width=150)
        self.tree.column("authority", width=150)

        self.tree.pack(fill="both", expand=True, ipady=100)

        # =========================
        # underframe
        # =========================
        serch_under_frame = ttk.Frame(user_contents_frame)
        serch_under_frame.pack(fill="both")

        # 新規登録ボタン
        self.button_new = ttk.Button(
            serch_under_frame,
            text="新規登録",
            command=lambda: self.frame_controller.show_frame("UserFormFrame", mode="New"),
        )

        self.button_new.grid(column=0, row=0, padx=(150, 30), pady=(15, 15))

        # 編集ボタン
        self.button_edit = ttk.Button(
            serch_under_frame, text="編集", command=self.edit_user
        )

        self.button_edit.grid(column=1, row=0, padx=(0, 30))

        # 削除ボタン
        self.button_delete = ttk.Button(
            serch_under_frame, text="削除", command=self.delete_user
        )

        self.button_delete.grid(column=2, row=0, padx=(0, 30))

    # =========================
    # ユーザー検索
    # =========================
    def search_user(self):

        employee_id = self.entry_id.get()
        users = user_service.get_user_list(employee_id)

        # Treeview初期化
        for item in self.tree.get_children():
            self.tree.delete(item)

        # データ追加
        for user in users:
            self.tree.insert(
                "", "end", values=(user["employee_id"], user["name"], user["authority"])
            )

    # =========================
    # ユーザー編集
    # =========================
    def edit_user(self):

        selected = self.tree.selection()

        if not selected:
            messagebox.showerror("エラー", "ユーザーを選択してください。")
            return

        item = self.tree.item(selected[0])

        employee_id = item["values"][0]

        user = user_service.get_user_list(employee_id)[0]

        self.frame_controller.show_frame("UserFormFrame", mode="Edit", user=user)

    # =========================
    # ユーザー削除
    # =========================
    def delete_user(self):

        selected = self.tree.selection()

        if not selected:
            messagebox.showerror("エラー", "ユーザーを選択してください。")
            return

        item = self.tree.item(selected[0])

        result = messagebox.askyesno(
            title="ユーザー削除",
            message=f"""下記のユーザーを削除します。よろしいですか？

        社員ID : {item["values"][0]}
        氏名   : {item["values"][1]}
        権限   : {item["values"][2]}
        """,
        )

        if not result:
            return

        employee_id = item["values"][0]

        try:
            user_service.delete_user_by_employee_id(employee_id)

        except Exception as e:  # noqa: BLE001
            messagebox.showerror("エラー", f"削除に失敗しました。\n{e}")
            return

        self.search_user()

        messagebox.showinfo("完了", "ユーザーを削除しました。")
