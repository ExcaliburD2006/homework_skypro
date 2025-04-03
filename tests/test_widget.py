import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("input_str, expected", [
    ("Счет 1234567890123456", "Счет **3456"),
    ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
    ("Некорректные данные", "Некорректные данные")
])
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2023-12-31T23:59:59.999", "31.12.2023"),
    ("", ""),
    ("invalid-date", "")
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected