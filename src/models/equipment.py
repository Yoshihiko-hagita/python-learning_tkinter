from dataclasses import dataclass


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
