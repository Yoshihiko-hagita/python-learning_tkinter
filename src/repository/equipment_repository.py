from src.db.connection_db import get_connection
from src.models.equipment import Equipment, EquipmentRegistration


class EquipmentRepository:
    def find_item_all(self):

        conn = get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    i.item_id,
                    i.item_name,
                    i.item_specification,
                    i.model_no,
                    i.category,
                    i.quantity,
                    u.unit_name AS unit_name,
                    i.loaned_qty,
                    i.quantity_per_unit,
                    cu.unit_name AS content_unit_name,
                    i.remarks
                FROM tbl_items AS i
                INNER JOIN tbl_units AS u
                    ON i.unit_id = u.unit_id
                LEFT JOIN tbl_units AS cu
                    ON i.content_unit_id = cu.unit_id
                ORDER BY i.item_id
            """)

            rows = cursor.fetchall()

            equipments = []

            for row in rows:
                equipment = Equipment(
                    item_id=row[0],
                    item_name=row[1],
                    item_specification=row[2],
                    model_no=row[3],
                    category=row[4],
                    quantity=row[5],
                    unit_name=row[6],
                    loaned_qty=row[7],
                    quantity_per_unit=row[8],
                    content_unit_name=row[9],
                    remarks=row[10],
                )

                equipments.append(equipment)

            return equipments

        finally:
            conn.close()

    def find_unit_id_by_name(self, unit_name: str) -> int | None:
        conn = get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT unit_id
                FROM tbl_units
                WHERE unit_name = ?
            """,
                (unit_name,),
            )

            row = cursor.fetchone()

            if row is None:
                return None

            return row[0]

        finally:
            conn.close()

    def insert_equipment(self, equipment_registration: EquipmentRegistration):
        item_id = self.generate_item_id(equipment_registration.category)
        conn = get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO tbl_items (
                    item_id,
                    item_name,
                    item_specification,
                    model_no,
                    category,
                    quantity,
                    unit_id,
                    quantity_per_unit,
                    content_unit_id,
                    loaned_qty,
                    remarks
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item_id,
                    equipment_registration.item_name,
                    equipment_registration.item_specification,
                    equipment_registration.model_no,
                    equipment_registration.category,
                    equipment_registration.quantity,
                    equipment_registration.unit_id,
                    equipment_registration.quantity_per_unit,
                    equipment_registration.content_unit_id,
                    0,
                    equipment_registration.remarks,
                ),
            )

            conn.commit()
            return True

        finally:
            conn.close()

    def generate_item_id(self, category: str) -> str:
        conn = get_connection()

        try:
            cursor = conn.cursor()

            if category == "備品":
                prefix = "EQ"
            else:
                prefix = "CON"

            cursor.execute(
                """
                SELECT MAX(item_id)
                FROM tbl_items
                WHERE item_id LIKE ?
                """,
                (f"{prefix}%",),
            )

            row = cursor.fetchone()

            if row[0] is None:
                number = 1
            else:
                number = int(row[0][len(prefix) :]) + 1

            return f"{prefix}{number:05d}"

        finally:
            conn.close()
