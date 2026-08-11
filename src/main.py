from typing import Any, Dict, List, Optional, Tuple

from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card

VALID_STATUSES: Tuple[str, ...] = ("EXECUTED", "CANCELED", "PENDING")
FILE_OPTIONS: Dict[str, Tuple[str, str]] = {
    "1": ("data/operations.json", "JSON"),
    "2": ("data/transactions.csv", "CSV"),
    "3": ("data/transactions_excel.xlsx", "XLSX"),
}


def get_currency_code(operation: Dict[str, Any]) -> str:
    """Возвращает код валюты операции для JSON, CSV и Excel форматов."""
    if "currency_code" in operation:
        return str(operation.get("currency_code", "")).upper()
    code = (
        operation.get("operationAmount", {})
        .get("currency", {})
        .get("code", "")
    )
    return str(code).upper()


def get_amount(operation: Dict[str, Any]) -> str:
    """Возвращает сумму операции для JSON, CSV и Excel форматов."""
    if "amount" in operation and "operationAmount" not in operation:
        return str(operation.get("amount", "0"))
    return str(operation.get("operationAmount", {}).get("amount", "0"))


def ask_yes_no(question: str) -> bool:
    """Запрашивает у пользователя ответ Да/Нет."""
    while True:
        print(f"Программа: {question} Да/Нет")
        answer = input("\nПользователь: ").strip().lower()
        if answer == "да":
            return True
        if answer == "нет":
            return False


def get_valid_status() -> str:
    """Запрашивает и возвращает корректный статус операции."""
    while True:
        print(
            "Программа: Введите статус, по которому необходимо выполнить фильтрацию. \n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        status_input = input("\nПользователь: ").strip()
        normalized_status = status_input.upper()
        if normalized_status in VALID_STATUSES:
            return normalized_status
        print(f'Программа: Статус операции "{status_input}" недоступен.')


def choose_file_format() -> Tuple[str, str]:
    """Запрашивает у пользователя формат файла с транзакциями."""
    print(
        "Программа: Привет! Добро пожаловать в программу работы \n"
        "с банковскими транзакциями. \n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    while True:
        choice = input("\nПользователь: ").strip()
        if choice in FILE_OPTIONS:
            file_path, file_format = FILE_OPTIONS[choice]
            print(f"Программа: Для обработки выбран {file_format}-файл.")
            return file_path, file_format
        print("Программа: Неверный пункт меню. Выберите 1, 2 или 3.")


def get_sort_direction() -> bool:
    """Запрашивает направление сортировки. True — по убыванию, False — по возрастанию."""
    while True:
        print("Программа: Отсортировать по возрастанию или по убыванию?")
        direction = input("\nПользователь: ").strip().lower()
        if direction == "по возрастанию":
            return False
        if direction == "по убыванию":
            return True


def filter_rub_transactions(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Оставляет только операции в рублях."""
    return [operation for operation in operations if get_currency_code(operation) == "RUB"]


def format_amount(operation: Dict[str, Any]) -> str:
    """Форматирует сумму операции для вывода в консоль."""
    amount_value = float(get_amount(operation))
    currency_code = get_currency_code(operation)

    if amount_value.is_integer():
        amount_text = str(int(amount_value))
    else:
        amount_text = str(amount_value)

    if currency_code == "RUB":
        return f"{amount_text} руб."
    return f"{amount_text} {currency_code}"


def format_accounts(operation: Dict[str, Any]) -> Optional[str]:
    """Форматирует строку с маскированными счетами и картами."""
    from_account = operation.get("from")
    to_account = operation.get("to")

    if from_account and to_account:
        return f"{mask_account_card(from_account)} -> {mask_account_card(to_account)}"
    if to_account:
        return mask_account_card(to_account)
    if from_account:
        return mask_account_card(from_account)
    return None


def print_transactions(operations: List[Dict[str, Any]]) -> None:
    """Печатает список транзакций в требуемом формате."""
    if not operations:
        print(
            "Программа: Не найдено ни одной транзакции, подходящей под ваши\n"
            "условия фильтрации"
        )
        return

    print("Программа: Распечатываю итоговый список транзакций...\n")
    print("Программа:")
    print(f"Всего банковских операций в выборке: {len(operations)}\n")

    for operation in operations:
        date = get_date(operation.get("date", ""))
        description = operation.get("description", "")
        print(f"{date} {description}")

        accounts_line = format_accounts(operation)
        if accounts_line:
            print(accounts_line)

        print(f"Сумма: {format_amount(operation)}")
        print()


def main() -> None:
    """Основная логика программы работы с банковскими транзакциями."""
    file_path, _ = choose_file_format()
    transactions = load_transactions(file_path)

    status = get_valid_status()
    print(f'Программа: Операции отфильтрованы по статусу "{status}"')

    filtered_transactions = filter_by_state(transactions, status)

    if ask_yes_no("Отсортировать операции по дате?"):
        reverse = get_sort_direction()
        filtered_transactions = sort_by_date(filtered_transactions, reverse=reverse)

    if ask_yes_no("Выводить только рублевые транзакции?"):
        filtered_transactions = filter_rub_transactions(filtered_transactions)

    if ask_yes_no("Отфильтровать список транзакций по определенному слову \nв описании?"):
        print("Программа: Введите слово для поиска в описании операции.")
        search_word = input("\nПользователь: ").strip()
        filtered_transactions = process_bank_search(filtered_transactions, search_word)

    print_transactions(filtered_transactions)
