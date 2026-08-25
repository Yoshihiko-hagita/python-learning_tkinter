import tkinter as tk
from tkinter import messagebox, ttk

from src.gui.base_frame import BaseFrame
from src.gui.common_validators.equipment_validator import EquipmentValidator
from src.models.equipment import EquipmentRegistration
from src.service.equipment_service import EquipmentService


class EquipmentRegistrationFrame(BaseFrame):
    def __init__(self, parent, frame_controller):

        super().__init__(parent, frame_controller, bg="white")

        self.equipment_service = EquipmentService()

        # =========================
        # コンテンツ(右側)-[Widget]
        # =========================
        equipment_register_frame = tk.Frame(self, bg="#FFFFFF")

        equipment_register_frame.pack(side="right", fill="both", expand=True)
        # 行0を伸縮可能にする
        equipment_register_frame.rowconfigure(0, weight=1)
        equipment_register_frame.columnconfigure(0, weight=1)

        # =========================
        # スクロール領域-[Widget]
        # =========================

        # Canvas
        self.canvas = tk.Canvas(
            equipment_register_frame, bg="#FFFFFF", highlightthickness=0
        )

        self.canvas.bind(
            "<Enter>",
            lambda e: self.canvas.bind_all("<MouseWheel>", self._on_mousewheel),
        )

        self.canvas.bind("<Leave>", lambda e: self.canvas.unbind_all("<MouseWheel>"))

        self.canvas.grid(row=0, column=0, sticky="nsew")

        # スクロールバー
        scrollbar = ttk.Scrollbar(
            equipment_register_frame, orient="vertical", command=self.canvas.yview
        )

        scrollbar.grid(row=0, column=1, sticky="ns")

        # CanvasとScrollbarを連動
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # =========================
        # フォーム-[Widget]
        # =========================
        self.equipment_form_frame = tk.LabelFrame(
            self.canvas,
            text="備品登録",
            fg="black",
        )

        # Canvasの中にフォームを配置
        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.equipment_form_frame, anchor="nw"
        )

        # フォームのサイズが変わったら
        # スクロール領域を更新
        self.equipment_form_frame.bind("<Configure>", self._update_scrollregion)

        # Canvasのサイズが変わったら
        # フォームの横幅をCanvasに合わせる
        self.canvas.bind("<Configure>", self._resize_form)

        # =========================
        # 品名-[Widget]
        # =========================
        label_name_important_notes = tk.Label(
            self.equipment_form_frame, text="※必須", font=("Meiryo UI", 8), fg="red"
        )

        label_name_important_notes.grid(row=0, column=1, sticky="w", padx=(20, 0))

        label_name = tk.Label(
            self.equipment_form_frame, text="品名             :", font=("Meiryo UI", 10)
        )

        label_name.grid(row=1, column=0, sticky="w", padx=(10, 0))

        self.entry_name = ttk.Entry(
            self.equipment_form_frame, font=("Meiryo UI", 12), width=30
        )

        self.entry_name.grid(row=1, column=1, sticky="w", padx=(20, 0))

        # =========================
        # 仕様 / 規格-[Widget]
        # =========================
        label_specification_important_notes = tk.Label(
            self.equipment_form_frame, text="※任意", font=("Meiryo UI", 8), fg="gray"
        )

        label_specification_important_notes.grid(
            row=2, column=1, sticky="w", padx=(20, 0), pady=(10, 0)
        )

        label_specification = tk.Label(
            self.equipment_form_frame, text="仕様 / 規格      :", font=("Meiryo UI", 10)
        )

        label_specification.grid(row=3, column=0, sticky="w", padx=(10, 0))

        self.entry_specification = ttk.Entry(
            self.equipment_form_frame, font=("Meiryo UI", 12), width=30
        )

        self.entry_specification.grid(row=3, column=1, sticky="w", padx=(20, 0))

        # =========================
        # 品番-[Widget]
        # =========================
        label_model_no_important_notes = tk.Label(
            self.equipment_form_frame, text="※任意", font=("Meiryo UI", 8), fg="gray"
        )

        label_model_no_important_notes.grid(
            row=4, column=1, sticky="w", padx=(20, 0), pady=(10, 0)
        )

        label_model_no = tk.Label(
            self.equipment_form_frame, text="品番             :", font=("Meiryo UI", 10)
        )

        label_model_no.grid(row=5, column=0, sticky="w", padx=(10, 0))

        self.entry_model_no = ttk.Entry(
            self.equipment_form_frame, font=("Meiryo UI", 12), width=30
        )

        self.entry_model_no.grid(row=5, column=1, sticky="w", padx=(20, 0))

        # =========================
        # カテゴリ-[Widget]
        # =========================
        label_category_important_notes = tk.Label(
            self.equipment_form_frame, text="※必須", font=("Meiryo UI", 8), fg="red"
        )

        label_category_important_notes.grid(
            row=6, column=1, sticky="w", padx=(20, 0), pady=(10, 0)
        )

        label_category = tk.Label(
            self.equipment_form_frame, text="カテゴリ         :", font=("Meiryo UI", 10)
        )

        label_category.grid(row=7, column=0, sticky="w", padx=(10, 0))

        self.entry_category = ttk.Combobox(
            self.equipment_form_frame,
            font=("Meiryo UI", 10),
            width=28,
            values=["備品", "消耗品"],
            state="readonly",
        )

        self.entry_category.grid(row=7, column=1, sticky="w", padx=(20, 0))

        self.entry_category.current(0)

        self.entry_category.bind("<<ComboboxSelected>>", self._on_category_changed)

        # =========================
        # 在庫数-[Widget]
        # =========================
        label_quantity_important_notes = tk.Label(
            self.equipment_form_frame, text="※必須", font=("Meiryo UI", 8), fg="red"
        )

        label_quantity_important_notes.grid(
            row=8, column=1, sticky="w", padx=(20, 0), pady=(10, 0)
        )

        label_quantity = tk.Label(
            self.equipment_form_frame, text="在庫数           :", font=("Meiryo UI", 10)
        )

        label_quantity.grid(row=9, column=0, sticky="w", padx=(10, 0))

        self.entry_quantity = ttk.Entry(
            self.equipment_form_frame, font=("Meiryo UI", 12), width=10
        )

        self.entry_quantity.grid(row=9, column=1, sticky="w", padx=(20, 0))

        # =========================
        # 単位-[Widget]
        # =========================
        label_unit_important_notes = tk.Label(
            self.equipment_form_frame, text="※必須", font=("Meiryo UI", 8), fg="red"
        )

        label_unit_important_notes.grid(
            row=10, column=1, sticky="w", padx=(20, 0), pady=(10, 0)
        )

        label_unit = tk.Label(
            self.equipment_form_frame, text="単位             :", font=("Meiryo UI", 10)
        )

        label_unit.grid(row=11, column=0, sticky="w", padx=(10, 0))

        self.entry_unit = ttk.Combobox(
            self.equipment_form_frame,
            font=("Meiryo UI", 10),
            width=28,
            values=["台", "個", "本", "冊", "箱", "セット", "パック"],
            state="readonly",
        )

        self.entry_unit.grid(row=11, column=1, sticky="w", padx=(20, 0))

        self.entry_unit.current(0)

        # =========================
        # 内容量-[Widget]
        # =========================
        self.label_quantity_per_unit_important_notes = tk.Label(
            self.equipment_form_frame, text="※必須", font=("Meiryo UI", 8), fg="red"
        )

        self.label_quantity_per_unit_important_notes.grid(
            row=12, column=1, sticky="w", padx=(20, 0), pady=(10, 0)
        )

        label_quantity_per_unit = tk.Label(
            self.equipment_form_frame, text="内容量           :", font=("Meiryo UI", 10)
        )

        label_quantity_per_unit.grid(row=13, column=0, sticky="w", padx=(10, 0))

        self.entry_quantity_per_unit = ttk.Entry(
            self.equipment_form_frame, font=("Meiryo UI", 12), width=10
        )

        self.entry_quantity_per_unit.grid(row=13, column=1, sticky="w", padx=(20, 0))

        # =========================
        # 内容量単位-[Widget]
        # =========================
        self.label_content_unit_important_notes = tk.Label(
            self.equipment_form_frame,
            text="※消耗品の場合は必須",
            font=("Meiryo UI", 8),
            fg="red",
        )

        self.label_content_unit_important_notes.grid(
            row=14, column=1, sticky="w", padx=(20, 0), pady=(10, 0)
        )

        label_content_unit = tk.Label(
            self.equipment_form_frame, text="内容量単位       :", font=("Meiryo UI", 10)
        )

        label_content_unit.grid(row=15, column=0, sticky="w", padx=(10, 0))

        self.entry_content_unit = ttk.Combobox(
            self.equipment_form_frame,
            font=("Meiryo UI", 10),
            width=28,
            values=["個", "本", "冊", "箱", "セット", "パック"],
            state="readonly",
        )

        self.entry_content_unit.grid(row=15, column=1, sticky="w", padx=(20, 0))

        self._on_category_changed()

        # =========================
        # 備考-[Widget]
        # =========================
        label_remarks_important_notes = tk.Label(
            self.equipment_form_frame, text="※任意", font=("Meiryo UI", 8), fg="gray"
        )

        label_remarks_important_notes.grid(
            row=16, column=1, sticky="w", padx=(20, 0), pady=(10, 0)
        )

        label_remarks = tk.Label(
            self.equipment_form_frame, text="備考             :", font=("Meiryo UI", 10)
        )

        label_remarks.grid(row=17, column=0, sticky="nw", padx=(10, 0))

        self.entry_remarks = tk.Text(
            self.equipment_form_frame, font=("Meiryo UI", 11), width=30, height=4
        )

        self.entry_remarks.grid(
            row=17,
            column=1,
            sticky="w",
            padx=(20, 0),
            pady=(0, 50),  # 下余白追加
        )

        # =========================
        # underframe-[Widget]
        # =========================
        register_under_frame = ttk.Frame(equipment_register_frame)

        register_under_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

        # 戻るボタン
        self.button_back = ttk.Button(register_under_frame, text="戻る")

        self.button_back.grid(column=0, row=0, padx=(110, 50), pady=(30, 15))

        # 登録ボタン
        self.button_register = ttk.Button(
            register_under_frame,
            text="登録",
            command=self._on_register,
        )

        self.button_register.grid(column=1, row=0, padx=(0, 50), pady=(30, 15))

        # キャンセルボタン
        self.button_cancel = ttk.Button(register_under_frame, text="キャンセル")

        self.button_cancel.grid(column=2, row=0, padx=(0, 50), pady=(30, 15))

    # ----------------------------
    # スクロール領域更新-[Method]
    # ----------------------------
    def _update_scrollregion(self, event=None):

        print(self.canvas.bbox("all"))

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # ----------------------------
    # フォーム横幅調整-[Method]
    # ----------------------------
    def _resize_form(self, event):

        self.canvas.itemconfig(self.canvas_window, width=event.width)

    # ----------------------------
    # マウスホイールスクロール
    # ----------------------------
    def _on_mousewheel(self, event):

        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # ----------------------------
    # カテゴリ変更-[Method]
    # ----------------------------
    def _on_category_changed(self, event=None):

        category = self.entry_category.get()

        if category == "備品":
            # 内容量を無効化
            self.entry_quantity_per_unit.configure(state="disabled")

            # 内容量単位を無効化
            self.entry_content_unit.configure(state="disabled")

            # 必須表示を非表示
            self.label_quantity_per_unit_important_notes.configure(text="")

            self.label_content_unit_important_notes.configure(text="")

        elif category == "消耗品":
            # 内容量を有効化
            self.entry_quantity_per_unit.configure(state="normal")

            # 内容量単位を有効化
            self.entry_content_unit.configure(state="readonly")

            # 必須表示を表示
            self.label_quantity_per_unit_important_notes.configure(text="※必須")

            self.label_content_unit_important_notes.configure(
                text="※消耗品の場合は必須"
            )

    # ----------------------------
    # 備品登録-[Method]
    # ----------------------------
    def _on_register(self):

        item_name = self.entry_name.get()
        category = self.entry_category.get()
        quantity = self.entry_quantity.get()
        quantity_per_unit = self.entry_quantity_per_unit.get()
        content_unit_name = self.entry_content_unit.get()

        response, message = EquipmentValidator.validate_registration(
            item_name,
            category,
            quantity,
            quantity_per_unit,
            content_unit_name,
        )

        if not response:
            messagebox.showerror("入力エラー", message)
            return

        unit_name = self.entry_unit.get()

        unit_id = self.equipment_service.get_unit_id_by_name(unit_name)

        if unit_id is None:
            messagebox.showerror("登録エラー", "単位が見つかりません。")
            return

        content_unit_id = None

        if category == "消耗品":
            content_unit_id = self.equipment_service.get_unit_id_by_name(
                content_unit_name
            )

            if content_unit_id is None:
                messagebox.showerror("登録エラー", "内容量単位が見つかりません。")
                return

        item_specification = self.entry_specification.get()
        model_no = self.entry_model_no.get()
        remarks = self.entry_remarks.get("1.0", "end-1c")

        equipment_registration = EquipmentRegistration(
            item_name=item_name,
            item_specification=item_specification,
            model_no=model_no,
            category=category,
            quantity=int(quantity),
            unit_id=unit_id,
            quantity_per_unit=int(quantity_per_unit) if quantity_per_unit else None,
            content_unit_id=content_unit_id,
            remarks=remarks,
        )

        result = self.equipment_service.register_equipment(equipment_registration)

        if result:
            messagebox.showinfo("登録完了", "備品を登録しました。")
