import json
import logging
from typing import Any, Dict, List
from src.file_reader import read_csv_file, read_excel_file

logger = logging.getLogger("utils")


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные о финансовых транзакциях из файла (JSON, CSV, XLSX).

    Args:
        file_path (str): Путь к файлу с транзакциями

    Returns:
        List[Dict[str, Any]]: Список словарей с транзакциями
    """
    try:
        if file_path.endswith('.json'):
            return _load_json(file_path)
        elif file_path.endswith('.csv'):
            return read_csv_file(file_path)
        elif file_path.endswith('.xlsx'):
            return read_excel_file(file_path)
        else:
            logger.error(f"Неподдерживаемый формат файла: {file_path}")
            return []
    except Exception as e:
        logger.error(f"Ошибка при загрузке файла {file_path}: {str(e)}")
        return []


def _load_json(file_path: str) -> List[Dict[str, Any]]:
    """Внутренняя функция для загрузки JSON файлов"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            logger.warning(f"Файл {file_path} содержит не список, а {type(data).__name__}")
            return []

        logger.info(f"Успешно загружено {len(data)} транзакций из {file_path}")
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Ошибка загрузки JSON файла {file_path}: {str(e)}")
        return []