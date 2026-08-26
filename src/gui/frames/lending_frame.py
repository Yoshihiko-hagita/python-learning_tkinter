import tkinter as tk
from tkinter import ttk

from src.gui.base_frame import BaseFrame


class LendingFrame(BaseFrame):
    def __init__(self, parent, frame_controller):
        super().__init__(parent, frame_controller, bg="white")

        # =========================
        # コンテンツ(右側)-[Widget]
        # =========================
        lending_frame = tk.Frame(self)
        lending_frame.pack(side="right", fill="both", expand=True)

        # =========================
        # 上部コンテンツ-[Widget]
        # =========================
        content_frame = tk.Frame(lending_frame)
        content_frame.pack(fill="both", expand=True)

        # =========================
        # 備品情報-[Widget]
        # =========================
        equipment_info_frame = ttk.LabelFrame(
            content_frame,
            text="備品情報",
        )

        equipment_info_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(20, 10),
            pady=20,
        )
        # =========================
        # 備品情報-[Label]
        # =========================
        self.label_item_id = ttk.Label(
            equipment_info_frame,
            text="備品ID：",
        )

        self.label_item_id.pack(
            anchor="w",
            padx=20,
            pady=(20, 5),
        )

        self.label_item_name = ttk.Label(
            equipment_info_frame,
            text="品名 / 内容量：",
        )

        self.label_item_name.pack(
            anchor="w",
            padx=20,
            pady=5,
        )

        self.label_item_specification = ttk.Label(
            equipment_info_frame,
            text="仕様 / 規格：",
        )

        self.label_item_specification.pack(
            anchor="w",
            padx=20,
            pady=5,
        )

        self.label_model_no = ttk.Label(
            equipment_info_frame,
            text="品番：",
        )

        self.label_model_no.pack(
            anchor="w",
            padx=20,
            pady=5,
        )

        self.label_category = ttk.Label(
            equipment_info_frame,
            text="カテゴリ：",
        )

        self.label_category.pack(
            anchor="w",
            padx=20,
            pady=5,
        )

        self.label_available_qty = ttk.Label(
            equipment_info_frame,
            text="貸出可能数：",
        )

        self.label_available_qty.pack(
            anchor="w",
            padx=20,
            pady=5,
        )

        self.label_remarks = ttk.Label(
            equipment_info_frame,
            text="備考：",
        )

        self.label_remarks.pack(
            anchor="w",
            padx=20,
            pady=5,
        )
        # =========================
        # 情報入力-[Widget]
        # =========================
        input_frame = ttk.LabelFrame(
            content_frame,
            text="情報入力",
        )

        input_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(10, 20),
            pady=20,
        )
        # =========================
        # 社員ID
        # =========================
        label_employee_id = ttk.Label(
            input_frame,
            text="社員ID：",
        )

        label_employee_id.pack(
            anchor="w",
            padx=20,
            pady=(20, 5),
        )

        self.label_employee_id = ttk.Label(
            input_frame,
            text="",
        )

        self.label_employee_id.pack(
            anchor="w",
            padx=(80, 20),
            pady=(0, 10),
        )


        # =========================
        # 氏名
        # =========================
        label_employee_name = ttk.Label(
            input_frame,
            text="氏名：",
        )

        label_employee_name.pack(
            anchor="w",
            padx=20,
            pady=5,
        )

        self.label_employee_name = ttk.Label(
            input_frame,
            text="",
        )

        self.label_employee_name.pack(
            anchor="w",
            padx=(80, 20),
            pady=(0, 10),
        )


        # =========================
        # 借用数
        # =========================
        label_loaned_qty = ttk.Label(
            input_frame,
            text="借用数：",
        )

        label_loaned_qty.pack(
            anchor="w",
            padx=20,
            pady=5,
        )

        self.entry_loaned_qty = ttk.Combobox(
            input_frame,
            state="readonly",
            width=10,
        )

        self.entry_loaned_qty.pack(
            anchor="w",
            padx=(80, 20),
            pady=(0, 10),
        )


        # =========================
        # 返却日
        # =========================
        label_due_date = ttk.Label(
            input_frame,
            text="返却日：",
        )

        label_due_date.pack(
            anchor="w",
            padx=20,
            pady=5,
        )

        self.entry_due_date = ttk.Entry(
            input_frame,
            width=15,
        )

        self.entry_due_date.pack(
            anchor="w",
            padx=(80, 20),
            pady=(0, 10),
        )
        # =========================
        # 下部ボタン-[Widget]
        # =========================
        button_frame = ttk.Frame(lending_frame)

        button_frame.pack(
            fill="x",
            padx=20,
            pady=(0, 20),
        )

        # 戻るボタン
        self.button_back = ttk.Button(
            button_frame,
            text="戻る",
        )

        self.button_back.pack(
            side="left",
            padx=(100, 30),
        )

        # 決定ボタン
        self.button_decide = ttk.Button(
            button_frame,
            text="決定",
        )

        self.button_decide.pack(
            side="left",
            padx=30,
        )

        # キャンセルボタン
        self.button_cancel = ttk.Button(
            button_frame,
            text="キャンセル",
        )

        self.button_cancel.pack(
            side="left",
            padx=30,
        )

    # ----------------------------
    # 備品情報設定-[Method]
    # ----------------------------
    def set_equipment_info(self, equipment):

        item_id = equipment[0]
        item_name = equipment[1]
        item_specification = equipment[2]
        model_no = equipment[3]
        category = equipment[4]
        available_qty = equipment[5]
        remarks = equipment[6]

        self.label_item_id.config(
            text=f"備品ID：{item_id}"
        )

        self.label_item_name.config(
            text=f"品名 / 内容量：{item_name}"
        )

        self.label_item_specification.config(
            text=f"仕様 / 規格：{item_specification}"
        )

        self.label_model_no.config(
            text=f"品番：{model_no}"
        )

        self.label_category.config(
            text=f"カテゴリ：{category}"
        )

        self.label_available_qty.config(
            text=f"貸出可能数：{available_qty}"
        )

        self.label_remarks.config(
            text=f"備考：{remarks}"
        )

        # =========================
        # 借用数の選択肢を設定
        # =========================
        available_qty_number = int(
            "".join(filter(str.isdigit, available_qty))
        )

        self.entry_loaned_qty["values"] = [
            str(i) for i in range(1, available_qty_number + 1)
        ]

        self.entry_loaned_qty.set("")