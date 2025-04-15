from typing import List, Iterator


def filter_by_currency(transactions: List[dict], currency: str) -> Iterator[dict]:
    """Фильтрует транзакции по заданной валюте и возвращает итератор"""
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)


# Пример использования
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions: list) -> Iterator[list]:
    """Генератор, возвращающий описание операций из транзакций"""
    for transaction in transactions:
        yield transaction["description"]


# Пример использования
transactions = [
    {"description": "Перевод организации"},
    {"description": "Перевод со счета на счет"},
    {"description": "Перевод со счета на счет"},
    {"description": "Перевод с карты на карту"},
    {"description": "Перевод организации"},
]

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор номеров карт в формате XXXX XXXX XXXX XXXX"""
    for num in range(start, end + 1):
        # Преобразуем число в 16-значную строку с ведущими нулями
        full_number = str(num).zfill(16)
        # Форматируем с пробелами каждые 4 символа
        yield " ".join(full_number[i: i + 4] for i in range(0, 16, 4))


# Пример использования
for card_number in card_number_generator(1, 5):
    print(card_number)
