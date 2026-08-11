from logger_config import setup_logging

# Инициализация папки для логов
setup_logging()

# Импорт после настройки логирования
from src.main import main as run_main


if __name__ == "__main__":
    run_main()
