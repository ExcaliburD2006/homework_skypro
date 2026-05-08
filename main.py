from logger_config import setup_logging

# Инициализация папки для логов
setup_logging()

# Импорт после настройки логирования
from src.masks import get_mask_account, get_mask_card_number
from src.utils import load_transactions


def main() -> None:
    # Пример использования
    try:
        # Загрузка транзакций из разных форматов (демонстрация новой функциональности)
        formats = [
            "data/operations.json",  # JSON
            "data/transactions.csv",  # CSV
            "data/transactions_excel.xlsx"  # Excel
        ]

        for file_path in formats:
            transactions = load_transactions(file_path)
            print(f"Загружено {len(transactions)} транзакций из {file_path}")

        # Маскировка карты
        card = "1234567890123456"
        masked_card = get_mask_card_number(card)
        print(f"Маскированная карта: {masked_card}")

        # Маскировка счета
        account = "1234567890"
        masked_account = get_mask_account(account)
        print(f"Маскированный счет: {masked_account}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
