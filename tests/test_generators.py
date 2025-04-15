from typing import Any, Dict, List
from unittest import TestCase

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тесты для filter_by_currency
class TestFilterByCurrency(TestCase):
    def test_basic_filtering(self, sample_transactions: List[Dict[str, Any]]) -> None:
        usd_transactions = filter_by_currency(sample_transactions, "USD")
        result = list(usd_transactions)
        assert len(result) == 2
        assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)

    def test_empty_result(self, sample_transactions: List[Dict[str, Any]]) -> None:
        gbp_transactions = filter_by_currency(sample_transactions, "GBP")
        assert list(gbp_transactions) == []

    def test_empty_input(self) -> None:
        assert list(filter_by_currency([], "USD")) == []

    def test_invalid_structure(self) -> None:
        with pytest.raises(KeyError):
            list(filter_by_currency([{"invalid": "structure"}], "USD"))


# Тесты для transaction_descriptions
class TestTransactionDescriptions(TestCase):
    @pytest.mark.parametrize(
        "input_data,expected",
        [([], []), ([{"description": "Test"}], ["Test"]), ([{"description": "A"}, {"description": "B"}], ["A", "B"])],
    )
    def test_description_generation(self, input_data: List[Dict[str, str]], expected: List[str]) -> None:
        gen = transaction_descriptions(input_data)
        assert list(gen) == expected

    def test_missing_description_key(self) -> None:
        with pytest.raises(KeyError):
            list(transaction_descriptions([{}]))


# Тесты для card_number_generator
class TestCardNumberGenerator(TestCase):
    @pytest.mark.parametrize(
        "start,end,expected",
        [
            (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
            (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
        ],
    )
    def test_range_generation(self, start: int, end: int, expected: List[str]) -> None:
        assert list(card_number_generator(start, end)) == expected

    def test_format_correctness(self) -> None:
        number = next(card_number_generator(1234567812345678, 1234567812345678))
        assert number == "1234 5678 1234 5678"

    def test_invalid_range(self) -> None:
        with pytest.raises(ValueError):
            list(card_number_generator(5, 1))

    def test_edge_cases(self) -> None:
        assert next(card_number_generator(0, 0)) == "0000 0000 0000 0000"
        assert next(card_number_generator(9999999999999999, 9999999999999999)) == "9999 9999 9999 9999"


# Проверка покрытия
def test_coverage() -> None:
    import coverage

    cov = coverage.Coverage()
    cov.start()

    # Запуск всех тестов
    pytest.main([__file__])

    cov.stop()
    cov.save()
    cov.report()
    assert cov.html_report() >= 80.0