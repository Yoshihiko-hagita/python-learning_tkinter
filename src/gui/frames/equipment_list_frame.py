import tkinter as tk
from tkinter import ttk

from src.gui.base_frame import BaseFrame
from src.service.equipment_service import EquipmentService


class EquipmentListFrame(BaseFrame):
    def __init__(self, parent, frame_controller):

        self.equipment_service = EquipmentService()

        super().__init__(parent, frame_controller, bg="white")

        # =========================
        # コンテンツ(右側)-[Widget]
        # =========================
        equipment_list_frame = tk.Frame(self, bg="#FFFFFF")

        equipment_list_frame.pack(
            side="right",
            fill="both",  # 横・縦に伸ばす
            expand=True,  # 余ったスペースを使う
        )

        # =========================
        # 備品一覧-[Widget]
        # =========================
        rental_frame = ttk.LabelFrame(equipment_list_frame, text="備品一覧")

        rental_frame.pack(fill="both")

        columns = (
            "item_id",
            "item_name",
            "item_specification",
            "model_no",
            "category",
            "quantity",
            "available_qty",
            "remarks",
        )

        self.tree = ttk.Treeview(
            rental_frame, columns=columns, show="headings", height=5
        )

        self.tree.heading("item_id", text="備品ID")
        self.tree.heading("item_name", text="品名 / 内容量")
        self.tree.heading("item_specification", text="仕様 / 規格")
        self.tree.heading("model_no", text="品番")
        self.tree.heading("category", text="カテゴリ")
        self.tree.heading("quantity", text="在庫数")
        self.tree.heading("available_qty", text="貸出可能数")
        self.tree.heading("remarks", text="備考")

        self.tree.column("item_id", width=80)
        self.tree.column("item_name", width=180)
        self.tree.column("item_specification", width=230)
        self.tree.column("model_no", width=160)
        self.tree.column("category", width=80, anchor="center")
        self.tree.column("quantity", width=80, anchor="center")
        self.tree.column("available_qty", width=95, anchor="center")
        self.tree.column("remarks", width=150)

        self.tree.pack(fill="both", expand=True, ipady=100)

        style = ttk.Style()

        style.configure("Treeview.Heading", font=("Arial", 9, "bold"))

        # =========================
        # underframe
        # =========================
        under_frame = ttk.Frame(equipment_list_frame)
        under_frame.pack(fill="both",expand=True)

        # 備品登録ボタン
        self.button_new_equipment = ttk.Button(
            under_frame,
            text="備品登録",
            command=lambda: self.frame_controller.show_frame("EquipmentRegistrationFrame"),
        )

        self.button_new_equipment.grid(column=0, row=0, padx=(150, 30), pady=(15, 15))

        # 貸出ボタン
        self.button_Lending = ttk.Button(
            under_frame,
            text="貸出",
        )

        self.button_Lending.grid(column=1, row=0, padx=(0, 30))

    def load_equipment_list(self):

        # 既存行削除
        for item in self.tree.get_children():
            self.tree.delete(item)

        equipments = self.equipment_service.get_equipment_list()

        for equipment in equipments:
            item_name = (
                f"{equipment.item_name} ({equipment.quantity_per_unit}{equipment.content_unit_name})"
                if equipment.quantity_per_unit is not None
                else equipment.item_name
            )

            item_specification = (
                "-"
                if equipment.item_specification is None
                else equipment.item_specification
            )

            model_no = "-" if equipment.model_no is None else equipment.model_no

            quantity = f"{equipment.quantity}{equipment.unit_name}"
            available_qty = equipment.quantity - equipment.loaned_qty
            available_qty = (
                "-"
                if equipment.item_id.startswith("CON")
                else f"{available_qty}{equipment.unit_name}"
            )
            remarks = "" if equipment.remarks is None else equipment.remarks

            values = (
                equipment.item_id,
                item_name,
                item_specification,
                model_no,
                equipment.category,
                quantity,
                available_qty,
                remarks,
            )

            self.tree.insert("", "end", values=values)
