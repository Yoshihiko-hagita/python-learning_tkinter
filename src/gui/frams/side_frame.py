import tkinter as tk
from tkinter import ttk

class SideFrame(tk.Frame):

    def __init__(self, parent):

        super().__init__(
            parent,
            width=180,
            bg="#E8E8E8"
        )

        self.pack_propagate(False)

        menu_list = [
            ("ホーム", "HomeFrame"),
            ("備品一覧", "ItemListFrame"),
            ("備品登録", "ItemRegisterFrame"),
            ("貸出", "RentalFrame"),
            ("返却", "ReturnFrame"),
            ("履歴", "HistoryFrame"),
            ("ユーザー管理", "UserManageFrame")
        ]

        for text, frame_name in menu_list:

            btn = ttk.Button(
                self,
                text=text,
                command=lambda n=frame_name:
                    parent.show_content(n)
            )

            btn.pack(
                fill="x",
                padx=5,
                pady=2
            )