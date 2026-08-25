class EquipmentValidator:

    @staticmethod
    def validate_item_name(item_name: str) -> str | None:
        if not item_name.strip():
            return "品名を入力してください。"

        return None

    @staticmethod
    def validate_category(category: str) -> str | None:
        if not category.strip():
            return "カテゴリを選択してください。"

        if category not in ("備品", "消耗品"):
            return "カテゴリが正しくありません。"

        return None

    @staticmethod
    def validate_quantity(quantity: str) -> str | None:
        if not quantity.strip():
            return "在庫数を入力してください。"

        if not quantity.isdigit():
            return "在庫数は整数で入力してください。"

        if int(quantity) < 0:
            return "在庫数は0以上で入力してください。"

        return None

    @staticmethod
    def validate_quantity_per_unit(
        quantity_per_unit: str,
        category: str
    ) -> str | None:

        # 備品の場合は内容量不要
        if category == "備品":
            return None

        # 消耗品の場合
        if not quantity_per_unit.strip():
            return "内容量を入力してください。"

        if not quantity_per_unit.isdigit():
            return "内容量は整数で入力してください。"

        if int(quantity_per_unit) <= 0:
            return "内容量は1以上で入力してください。"

        return None

    @staticmethod
    def validate_content_unit(
        content_unit_name: str,
        category: str
    ) -> str | None:

        # 備品の場合は内容量単位も不要
        if category == "備品":
            return None

        # 消耗品の場合
        if not content_unit_name.strip():
            return "内容量単位を選択してください。"

        return None

    @staticmethod
    def validate_registration(
        item_name: str,
        category: str,
        quantity: str,
        quantity_per_unit: str,
        content_unit_name: str,
    ) -> tuple[bool, str]:

        error = EquipmentValidator.validate_item_name(item_name)
        if error:
            return False, error

        error = EquipmentValidator.validate_category(category)
        if error:
            return False, error

        error = EquipmentValidator.validate_quantity(quantity)
        if error:
            return False, error

        error = EquipmentValidator.validate_quantity_per_unit(
            quantity_per_unit,
            category
        )
        if error:
            return False, error

        error = EquipmentValidator.validate_content_unit(
            content_unit_name,
            category
        )
        if error:
            return False, error

        return True, ""