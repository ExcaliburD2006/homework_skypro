import logging
import os
from pathlib import Path

def setup_logging() -> None:
    """Создаёт папку для логов и базовую конфигурацию"""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)