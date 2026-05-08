from datetime import datetime
from typing import Dict, List


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует операции по статусу с проверкой типа входных данных"""
    if not isinstance(operations, list):
        raise TypeError("Input must be a list of dictionaries")

    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортирует операции по дате с обработкой некорректных форматов"""
    if not isinstance(operations, list):
        raise TypeError("Input must be a list of dictionaries")

    def get_sort_key(op: Dict) -> datetime:
        date_str = op.get("date", "")
        try:
            return datetime.fromisoformat(date_str)
        except (ValueError, TypeError):
            return datetime.min if reverse else datetime.max

    return sorted(
        operations,
        key=get_sort_key,
        reverse=reverse
    )
