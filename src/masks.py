from typing import Union


def get_mask_card_number(card_number: Union[int]):
    # Форматируем номер карты в нужный вид
    masked_card_number = f"{card_number[:4]} {card_number[4:6]} ** {card_number[12:]}"
    return masked_card_number


def get_mask_account(account_number: Union[int]):
    # Форматируем номер счета в нужный вид
    masked_account_number = f"**{account_number[-4:]}"
    return masked_account_number
