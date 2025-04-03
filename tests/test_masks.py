from typing import Any, Tuple, Type

import pytest
from pytest import raises

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234987654321098", "1234 98** **** 1098"),
        ("1111 2222 3333 4444", "1111 22** **** 4444"),
        ("0000000000000000", "0000 00** **** 0000"),
    ],
)
def test_get_mask_card_number_valid(card_number: str, expected: str) -> None:
    """Тестирует корректную маскировку номеров карт.

    Args:
        card_number: Номер карты для маскировки
        expected: Ожидаемый результат после маскировки
    """
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "invalid_card, exception",
    [
        ("1234", ValueError),
        ("abcdefgh", ValueError),
        (None, TypeError),
    ],
)
def test_get_mask_card_number_errors(
        invalid_card: Any,
        exception: Type[Exception]
) -> None:
    """Тестирует обработку некорректных номеров карт.

    Args:
        invalid_card: Некорректный номер карты
        exception: Ожидаемый тип исключения
    """
    with raises(exception):
        get_mask_card_number(invalid_card)


@pytest.mark.parametrize(
    "account, expected",
    [
        ("1234567890", "**7890"),
        ("9876543210987654", "**7654"),
        ("0000000000000000", "**0000"),
    ],
)
def test_get_mask_account_valid(account: str, expected: str) -> None:
    """Тестирует корректную маскировку номеров счетов.

    Args:
        account: Номер счета для маскировки
        expected: Ожидаемый результат после маскировки
    """
    assert get_mask_account(account) == expected


@pytest.mark.parametrize(
    "invalid_account, exception",
    [
        ("123", ValueError),
        (None, TypeError),
    ],
)
def test_get_mask_account_errors(
        invalid_account: Any,
        exception: Type[Exception]
) -> None:
    """Тестирует обработку некорректных номеров счетов.

    Args:
        invalid_account: Некорректный номер счета
        exception: Ожидаемый тип исключения
    """
    with raises(exception):
        get_mask_account(invalid_account)