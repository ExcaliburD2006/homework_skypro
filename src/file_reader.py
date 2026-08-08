import logging
from typing import Any, Dict, List, cast

import pandas as pd  # type: ignore[import-untyped]

logger = logging.getLogger("file_reader")


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из CSV-файла.

    Args:
        file_path (str): Путь к CSV-файлу

    Returns:
        List[Dict[str, Any]]: Список словарей с транзакциями
    """
    try:
        df = pd.read_csv(file_path)
        transactions = cast(List[Dict[str, Any]], df.to_dict("records"))
        logger.info(f"Успешно загружено {len(transactions)} транзакций из CSV файла: {file_path}")
        return transactions
    except FileNotFoundError:
        logger.error(f"CSV файл не найден: {file_path}")
        return []
    except pd.errors.EmptyDataError:
        logger.error(f"CSV файл пуст: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV файла {file_path}: {str(e)}")
        return []


def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из XLSX-файла.

    Args:
        file_path (str): Путь к XLSX-файлу

    Returns:
        List[Dict[str, Any]]: Список словарей с транзакциями
    """
    try:
        df = pd.read_excel(file_path)
        transactions = cast(List[Dict[str, Any]], df.to_dict("records"))
        logger.info(f"Успешно загружено {len(transactions)} транзакций из Excel файла: {file_path}")
        return transactions
    except FileNotFoundError:
        logger.error(f"Excel файл не найден: {file_path}")
        return []
    except pd.errors.EmptyDataError:
        logger.error(f"Excel файл пуст: {file_path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel файла {file_path}: {str(e)}")
        return []
