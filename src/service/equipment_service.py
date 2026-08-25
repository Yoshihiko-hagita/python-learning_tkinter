from src.models.equipment import EquipmentRegistration
from src.repository.equipment_repository import EquipmentRepository


class EquipmentService:
    def __init__(self):
        self.repository = EquipmentRepository()

    def get_equipment_list(self):
        return self.repository.find_item_all()

    def get_unit_id_by_name(self, unit_name: str) -> int | None:
        return self.repository.find_unit_id_by_name(unit_name)

    def register_equipment(self, equipment_registration: EquipmentRegistration):
        return self.equipment_repository.insert_equipment(equipment_registration)
