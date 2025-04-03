def mask_card_number(number: str) -> str:
    # Маскирует номер карты, оставляя первые 4 и последние 4 цифры.
    cleaned = "".join(filter(str.isdigit, number))
    if len(cleaned) < 16:
        return number
    return f"{cleaned[:4]} {cleaned[4:6]}** **** {cleaned[-4:]}"


def mask_account_number(number: str) -> str:
    # Маскирует номер счета, оставляя последние 4 цифры.
    cleaned = "".join(filter(str.isdigit, number))
    if len(cleaned) < 4:
        return number
    return f"**{cleaned[-4:]}"


def mask_card_or_account(text: str) -> str:
    # Маскирует номер карты или счета в переданной строке.
    parts = text.rsplit(" ", 1)
    if len(parts) != 2:
        return text

    type_name, number = parts

    if type_name.lower() == "счет":
        masked_number = mask_account_number(number)
    else:
        masked_number = mask_card_number(number)

    return f"{type_name} {masked_number}"


def get_date(date_str: str) -> str:
    # Преобразует дату из формата ISO 8601 в строку формата ДД.ММ.ГГГГ.
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
