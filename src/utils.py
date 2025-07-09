import json
from typing import Dict, List


def load_transactions(file_path: str) -> List[Dict]:
    """Загружает данные о финансовых транзакциях из JSON-файла."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Проверяем, что данные являются списком
            if not isinstance(data, list):
                return []

            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
