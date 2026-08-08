import re
from datetime import datetime
from typing import Any, Dict, List


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """Возвращает операции, в описании которых найдена строка поиска."""
    if not isinstance(data, list):
        raise TypeError("Input must be a list of dictionaries")

    pattern = re.compile(search, re.IGNORECASE)
    return [
        operation for operation in data
        if pattern.search(str(operation.get("description", "")))
    ]


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Возвращает количество операций для каждой категории из поля description."""
    if not isinstance(data, list):
        raise TypeError("Input must be a list of dictionaries")

    result: Dict[str, int] = {category: 0 for category in categories}
    for operation in data:
        description = operation.get("description", "")
        if description in result:
            result[description] += 1
    return result


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
