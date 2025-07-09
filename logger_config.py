import logging
import os
from pathlib import Path
from typing import Any


def setup_logging() -> None:
    """Настройка логирования для приложения"""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "app.log"

    # Создаем форматтер
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Создаем обработчик файла с перезаписью
    file_handler = logging.FileHandler(log_file, mode="w")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Настраиваем логеры для модулей
    modules = ["masks", "utils"]
    for module in modules:
        logger = logging.getLogger(module)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
        logger.propagate = False
