import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number_valid():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number("1234 5678 9012 3456") == "1234 56** **** 3456"

def test_get_mask_card_number_invalid():
    with pytest.raises(ValueError):
        get_mask_card_number("1234")
    with pytest.raises(ValueError):
        get_mask_card_number("abcdefgh")

def test_get_mask_account_valid():
    assert get_mask_account("1234567890") == "**7890"

def test_get_mask_account_invalid():
    with pytest.raises(ValueError):
        get_mask_account("123")
    with pytest.raises(ValueError):
        get_mask_account("abcd")