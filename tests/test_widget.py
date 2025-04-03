import pytest
from src.widget import mask_account_card, get_date

# Параметризация для маскировки
@pytest.mark.parametrize("input_str, expected", [
    ("Счет 1234567890123456", "Счет **3456"),
    ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
    ("Maestro 0000000000000000", "Maestro 0000 00** **** 0000"),
    ("Неизвестный формат", "Неизвестный формат"),
    ("", ""),
])
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected

# Параметризация для дат
@pytest.mark.parametrize("raw_date, expected", [
    ("2023-12-31T23:59:59.999", "31.12.2023"),
    ("2024-02-29T00:00:00.000", "29.02.2024"),
    ("invalid-date", ""),
    ("", ""),
])
def test_get_date(raw_date, expected):
    assert get_date(raw_date) == expected