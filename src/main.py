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


def print_program(message: str) -> None:
    """Выводит сообщение программы с префиксом."""
    print(f"Программа: {message}")


def read_user_input() -> str:
    """Считывает ввод пользователя."""
    return input("\nПользователь: ").strip()


def ask_yes_no(question: str) -> bool:
    """Запрашивает у пользователя ответ Да/Нет."""
    while True:
        print_program(f"{question} Да/Нет")
        answer = read_user_input().lower()
        if answer == "да":
            return True
        if answer == "нет":
            return False


def get_valid_status() -> str:
    """Запрашивает и возвращает корректный статус операции."""
    while True:
        print_program(
            "Введите статус, по которому необходимо выполнить фильтрацию. \n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        status_input = read_user_input()
        normalized_status = status_input.upper()
        if normalized_status in VALID_STATUSES:
            return normalized_status
        print_program(f'Статус операции "{status_input}" недоступен.')


def choose_file_format() -> Tuple[str, str]:
    """Запрашивает у пользователя формат файла с транзакциями."""
    print_program(
        "Привет! Добро пожаловать в программу работы \n"
        "с банковскими транзакциями. \n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    while True:
        choice = read_user_input()
        if choice in FILE_OPTIONS:
            file_path, file_format = FILE_OPTIONS[choice]
            print_program(f"Для обработки выбран {file_format}-файл.")
            return file_path, file_format
        print_program("Неверный пункт меню. Выберите 1, 2 или 3.")


def get_sort_direction() -> bool:
    """Запрашивает направление сортировки. True — по убыванию, False — по возрастанию."""
    while True:
        print_program("Отсортировать по возрастанию или по убыванию?")
        direction = read_user_input().lower()
        if direction == "по возрастанию":
            return False
        if direction == "по убыванию":
            return True


def filter_rub_transactions(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Оставляет только операции в рублях."""
    rub_operations: List[Dict[str, Any]] = []
    for operation in operations:
        currency_code = (
            operation.get("operationAmount", {})
            .get("currency", {})
            .get("code", "")
            .upper()
        )
        if currency_code == "RUB":
            rub_operations.append(operation)
    return rub_operations


def format_amount(operation: Dict[str, Any]) -> str:
    """Форматирует сумму операции для вывода в консоль."""
    amount_data = operation.get("operationAmount", {})
    amount = amount_data.get("amount", "0")
    currency_code = amount_data.get("currency", {}).get("code", "RUB")

    amount_value = float(amount)
    if amount_value.is_integer():
        amount_text = str(int(amount_value))
    else:
        amount_text = str(amount)

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
        print_program(
            "Не найдено ни одной транзакции, подходящей под ваши\n"
            "условия фильтрации"
        )
        return

    print_program("Распечатываю итоговый список транзакций...\n")
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
    print_program(f'Операции отфильтрованы по статусу "{status}"')

    filtered_transactions = filter_by_state(transactions, status)

    if ask_yes_no("Отсортировать операции по дате?"):
        reverse = get_sort_direction()
        filtered_transactions = sort_by_date(filtered_transactions, reverse=reverse)

    if ask_yes_no("Выводить только рублевые транзакции?"):
        filtered_transactions = filter_rub_transactions(filtered_transactions)

    if ask_yes_no("Отфильтровать список транзакций по определенному слову \nв описании?"):
        print_program("Введите слово для поиска в описании операции.")
        search_word = read_user_input()
        filtered_transactions = process_bank_search(filtered_transactions, search_word)

    print_transactions(filtered_transactions)
