from typing import Any, Dict, List
import pytest
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# Убраны классы TestCase, используется стиль pytest
# Тесты для filter_by_currency
def test_basic_filtering(sample_transactions: List[Dict[str, Any]]) -> None:
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    result = list(usd_transactions)
    assert len(result) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)

def test_empty_result(sample_transactions: List[Dict[str, Any]]) -> None:
    gbp_transactions = filter_by_currency(sample_transactions, "GBP")
    assert list(gbp_transactions) == []

def test_empty_input() -> None:
    assert list(filter_by_currency([], "USD")) == []

def test_invalid_structure() -> None:
    with pytest.raises(KeyError):
        list(filter_by_currency([{"invalid": "structure"}], "USD"))

# Тесты для transaction_descriptions
@pytest.mark.parametrize(
    "input_data,expected",
    [
        ([], []),
        ([{"description": "Test"}], ["Test"]),
        ([{"description": "A"}, {"description": "B"}], ["A", "B"]),
        ([{"description": None}], [None]),  # Новый тест
    ]
)
def test_description_generation(input_data: List[Dict], expected: List[str]) -> None:
    gen = transaction_descriptions(input_data)
    assert list(gen) == expected

def test_missing_description_key() -> None:
    with pytest.raises(KeyError):
        list(transaction_descriptions([{}]))

# Тесты для card_number_generator
@pytest.mark.parametrize(
    "start,end,expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
        (0, 0, ["0000 0000 0000 0000"]),  # Граничный случай
    ]
)
def test_range_generation(start: int, end: int, expected: List[str]) -> None:
    assert list(card_number_generator(start, end)) == expected

def test_format_correctness() -> None:
    number = next(card_number_generator(1234567812345678, 1234567812345678))
    assert number == "1234 5678 1234 5678"

def test_invalid_range() -> None:
    with pytest.raises(ValueError):
        list(card_number_generator(5, 1))

def test_edge_cases() -> None:
    assert next(card_number_generator(0, 0)) == "0000 0000 0000 0000"
    assert next(card_number_generator(9999999999999999, 9999999999999999)) == "9999 9999 9999 9999"

# Дополнительные тесты для повышения покрытия
def test_partial_transaction_data(sample_transactions: List[Dict[str, Any]]) -> None:
    # Тест с неполными данными
    partial_data = [{"operationAmount": {"currency": {"code": "USD"}}}]
    result = list(filter_by_currency(partial_data, "USD"))
    assert len(result) == 1

def test_invalid_currency_code(sample_transactions: List[Dict[str, Any]]) -> None:
    # Тест с некорректным кодом валюты
    invalid_data = [{"operationAmount": {"currency": {"code": 123}}}]
    with pytest.raises(TypeError):
        list(filter_by_currency(invalid_data, "USD"))