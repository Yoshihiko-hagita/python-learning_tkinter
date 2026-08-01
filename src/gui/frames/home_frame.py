import tkinter as tk
from tkinter import ttk

from src.gui.base_frame import BaseFrame

class HomeFrame(BaseFrame):

    def __init__(self, parent,frame_manager):

        super().__init__(parent,frame_manager,bg="white")


        #=========================
        # コンテンツ(右側)
        #=========================
        home_contents_frame = tk.Frame(
            self,
            bg="#FFFFFF"
        )

        home_contents_frame.pack(
            side="right",
            fill="both",# 横・縦に伸ばす
            expand=True # 余ったスペースを使う
        )

        # =========================
        # 現在貸出中の備品
        # =========================
        rental_frame = ttk.LabelFrame(
            home_contents_frame,
            text="現在貸出中の備品"
        )

        rental_frame.pack(
            fill="both"
        )

        columns = (
            "id",
            "name",
            "model",
            "qty",
            "return_date"
        )

        self.tree = ttk.Treeview(
            rental_frame,
            columns=columns,
            show="headings",
            height=5
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="名称")
        self.tree.heading("model", text="品番")
        self.tree.heading("qty", text="数量")
        self.tree.heading("return_date", text="返却日")

        self.tree.column("id", width=100)
        self.tree.column("name", width=150)
        self.tree.column("model", width=150)
        self.tree.column("qty", width=60, anchor="center")
        self.tree.column("return_date", width=100, anchor="center")

        self.tree.pack(
            fill="both",
            expand=True,
            ipady=100
        )

        # ダミーデータ
        self.tree.insert(
            "",
            "end",
            values=("EQ-A001", "PC", "JPh436R43", "1", "4/12")
        )

        self.tree.insert(
            "",
            "end",
            values=("EQ-A021", "キーボード", "PJ43Y3434", "1", "4/12")
        )

        self.tree.insert(
            "",
            "end",
            values=("EQ-D001", "マウス", "PJ111JRE8", "1", "4/12")
        )

        # =========================
        # お知らせ
        # =========================
        notice_frame = ttk.LabelFrame(
            home_contents_frame,
            text="お知らせ"
        )

        notice_frame.pack(
            fill="both",
            expand=True
        )

        notice_list = tk.Listbox(
            notice_frame,
            font=("Meiryo UI", 10),
            height=5
        )

        notice_list.pack(
            fill="both",
            ipady=30
        )

        notice_list.insert(
            tk.END,
            "返却期限が近い備品があります。"
        )

        notice_list.insert(
            tk.END,
            "新しいVerがリリースされました。"
        )

        notice_list.insert(
            tk.END,
            "最新版をダウンロードしてください。"
        )

        # =========================
        # バージョン表示
        # =========================

        version_label = tk.Label(
            home_contents_frame,
            text="Ver 1.0.0",
            font=("Meiryo UI", 9)
        )

        version_label.place(
            relx=1.0,
            rely=1.0,
            anchor="se"
        )
