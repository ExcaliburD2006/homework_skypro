from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number  # Добавляем импорт


def mask_account_card(data: str) -> str:
    """Определяет тип данных (карта/счет) и применяет маскировку"""
    if not isinstance(data, str):
        return ""

    parts = data.split()
    if not parts:
        return data

    if parts[0] == "Счет":
        try:
            return f"Счет {get_mask_account(parts[1])}"
        except (ValueError, TypeError):
            return data
    else:
        try:
            return f"{' '.join(parts[:-1])} {get_mask_card_number(parts[-1])}"
        except (ValueError, TypeError):
            return data


def get_date(date_str: str) -> str:
    """Преобразует дату из ISO формата в DD.MM.YYYY"""
    if not date_str:
        return ""

    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return ""
