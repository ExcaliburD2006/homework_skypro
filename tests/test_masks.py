import pytest
from src.masks import get_mask_card_number, get_mask_account

# Параметризация для карт
@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("1234987654321098", "1234 98** **** 1098"),
    ("1111 2222 3333 4444", "1111 22** **** 4444"),
    ("0000000000000000", "0000 00** **** 0000"),
])
def test_get_mask_card_number_valid(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("invalid_card, exception", [
    ("1234", ValueError),
    ("abcdefgh", ValueError),
    (None, TypeError)
])
def test_get_mask_card_number_errors(invalid_card, exception):
    with pytest.raises(exception):
        get_mask_card_number(invalid_card)

# Параметризация для счетов
@pytest.mark.parametrize("account, expected", [
    ("1234567890", "**7890"),
    ("9876543210987654", "**7654"),
    ("0000000000000000", "**0000"),
])
def test_get_mask_account_valid(account, expected):
    assert get_mask_account(account) == expected

@pytest.mark.parametrize("invalid_account, exception", [
    ("123", ValueError),
    (None, TypeError)
])
def test_get_mask_account_errors(invalid_account, exception):
    with pytest.raises(exception):
        get_mask_account(invalid_account)