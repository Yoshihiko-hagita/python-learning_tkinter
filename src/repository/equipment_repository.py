from src.db.connection_db import get_connection
from src.models.equipment import Equipment


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

            cursor.execute("""
                SELECT unit_id
                FROM tbl_units
                WHERE unit_name = ?
            """, (unit_name,))

            row = cursor.fetchone()

            if row is None:
                return None

            return row[0]

        finally:
            conn.close()