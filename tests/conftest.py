from typing import Any, Dict, List

import pytest


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    """Фикстура предоставляет тестовые данные для модуля processing.

    Returns:
        List[Dict[str, Any]]: Список словарей с тестовыми транзакциями, включая:
            - корректные данные с state и date
            - данные без state
            - данные с невалидной датой
    """
    return [
        {"state": "EXECUTED", "date": "2023-10-01T00:00:00.000"},
        {"state": "PENDING", "date": "2023-09-15T12:30:45.123"},
        {"state": "EXECUTED", "date": "2023-11-20T15:45:30.456"},
        {"date": "2023-08-05T08:10:15.789"},
        {"state": "CANCELED", "date": "invalid-date"}
    ]
@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
     return [
         {
             "operationAmount": {
                 "currency": {"code": "USD"},
                 "amount": "100.00"
             },
             "description": "Payment 1"
         },
         {
             "operationAmount": {
                 "currency": {"code": "EUR"},
                 "amount": "200.00"
             },
             "description": "Payment 2"
         },
         {
             "operationAmount": {
                 "currency": {"code": "USD"},
                 "amount": "300.00"
             },
             "description": "Payment 3"
         }
     ]