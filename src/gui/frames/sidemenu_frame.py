import tkinter as tk
from tkinter import ttk

class SideMenuFrame(tk.Frame):

    def __init__(self, parent, frame_manager):

        super().__init__(
            parent,
            width=180,
            bg="#7F7C7C"
        )

        #=========================
        # サイドメニュー(左側)
        #=========================
        self.frame_manager = frame_manager

        self.pack_propagate(False)

        menu_list = [
            ("ホーム", "HomeFrame"),
            ("備品一覧", "ItemListFrame"),
            ("備品登録", "ItemRegisterFrame"),
            ("貸出", "RentalFrame"),
            ("返却", "ReturnFrame"),
            ("履歴", "HistoryFrame"),
            ("ユーザー管理", "UserManagementFrame")
        ]

        for text, frame_name in menu_list:

            btn = ttk.Button(
                self,
                text=text,
                command=lambda n=frame_name:
                    self.frame_manager.show_frame(n)
            )

            btn.pack(
                fill="x",
                padx=5,
                pady=2
            )