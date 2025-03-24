def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей для фильтрации.
    :param state: Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей, где 'state' соответствует заданному значению.
    """
    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате.

    :param transactions: Список словарей для сортировки.
    :param reverse: Если True, сортировка по убыванию (по умолчанию)
    Если False, по возрастанию.
    :return: Новый список словарей, отсортированный по дате.
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
