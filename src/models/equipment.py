from dataclasses import dataclass


# 備品：一覧取得用
@dataclass
class Equipment:
    item_id: str
    item_name: str
    item_specification: str | None
    model_no: str | None
    category: str
    quantity: int
    unit_name: str
    loaned_qty: int
    quantity_per_unit: int | None
    content_unit_name: str | None
    remarks: str | None


# 備品：登録用
@dataclass
class EquipmentRegistration:
    item_name: str
    item_specification: str | None
    model_no: str | None
    category: str
    quantity: int
    unit_id: int
    quantity_per_unit: int | None
    content_unit_id: int | None
    remarks: str | None
