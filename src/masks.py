import logging
from typing import NoReturn

logger = logging.getLogger("masks")


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя первые 6 и последние 4 цифры"""
    try:
        if not isinstance(card_number, str):
            error_msg = "Номер карты должен быть строкой"
            logger.error(error_msg)
            raise TypeError(error_msg)

        digits = card_number.replace(" ", "")
        if not digits.isdigit():
            error_msg = "Номер карты должен содержать только цифры"
            logger.error(error_msg)
            raise ValueError(error_msg)
        if len(digits) != 16:
            error_msg = "Номер карты должен содержать 16 цифр"
            logger.error(error_msg)
            raise ValueError(error_msg)

        masked = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
        logger.info(f"Успешно замаскирован номер карты: {masked}")
        return masked
    except (TypeError, ValueError) as e:
        logger.exception(f"Ошибка при маскировании карты: {str(e)}")
        raise


def get_mask_account(account: str) -> str:
    """Маскирует номер счета, оставляя последние 4 цифры"""
    try:
        if not isinstance(account, str):
            error_msg = "Номер счета должен быть строкой"
            logger.error(error_msg)
            raise TypeError(error_msg)

        if not account.isdigit():
            error_msg = "Номер счета должен содержать только цифры"
            logger.error(error_msg)
            raise ValueError(error_msg)
        if len(account) < 4:
            error_msg = "Номер счета должен содержать минимум 4 цифры"
            logger.error(error_msg)
            raise ValueError(error_msg)

        masked = f"**{account[-4:]}"
        logger.info(f"Успешно замаскирован номер счета: {masked}")
        return masked
    except (TypeError, ValueError) as e:
        logger.exception(f"Ошибка при маскировании счета: {str(e)}")
        raise
