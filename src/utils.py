import json
import logging
from pathlib import Path
from typing import Any, Dict, List

# Создаем отдельный логер для модуля
logger = logging.getLogger("utils")

# Настраиваем handler и formatter
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
log_file = log_dir / "utils.log"

handler = logging.FileHandler(log_file, mode="w")
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает данные о финансовых транзакциях из JSON-файла"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            logger.warning(f"Файл {file_path} содержит не список, а {type(data).__name__}")
            return []

        logger.info(f"Успешно загружено {len(data)} транзакций из {file_path}")
        return data
    except FileNotFoundError as e:
        logger.error(f"Файл не найден: {file_path} - {str(e)}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {str(e)}")
        return []
    except Exception as e:
        logger.exception(f"Непредвиденная ошибка при загрузке файла {file_path}: {str(e)}")
        return []
