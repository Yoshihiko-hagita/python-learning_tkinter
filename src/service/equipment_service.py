from src.repository.equipment_repository import EquipmentRepository


class EquipmentService:

    def __init__(self):
        self.repository = EquipmentRepository()

    def get_equipment_list(self):
        return self.repository.find_item_all()