import tkinter as tk
from tkinter import ttk


class SideMenuFrame(tk.Frame):
    def __init__(self, parent, frame_manager):

        super().__init__(parent, width=120, bg="#7F7C7C")

        # =========================
        # サイドメニュー(左側)
        # =========================
        self.frame_manager = frame_manager

        self.pack_propagate(False)

        menu_list = [
            ("ホーム", "HomeFrame", True),
            ("備品一覧", "EquipmentListFrame", True),
            ("備品登録", "ItemRegisterFrame", False),
            ("貸出", "RentalFrame", False),
            ("返却", "ReturnFrame", False),
            ("履歴", "HistoryFrame", False),
            ("ユーザー管理", "UserManagementFrame", True),
        ]

        for text, frame_name, is_available in menu_list:
            btn = ttk.Button(
                self,
                text=text,
                command=lambda n=frame_name: self.frame_manager.show_frame(n),
                state="normal" if is_available else "disabled",
            )

            btn.pack(fill="x", padx=5, pady=2)
