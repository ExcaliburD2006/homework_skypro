def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя первые 6 и последние 4 цифры"""
    if not isinstance(card_number, str):
        raise TypeError("Номер карты должен быть строкой")

    digits = card_number.replace(" ", "")
    if not digits.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")
    if len(digits) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"


def get_mask_account(account: str) -> str:
    """Маскирует номер счета, оставляя последние 4 цифры"""
    if not isinstance(account, str):
        raise TypeError("Номер счета должен быть строкой")

    if not account.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")
    if len(account) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{account[-4:]}"
