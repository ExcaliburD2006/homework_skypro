from typing import Dict, Any, Optional, cast, Literal
from src.external_api import convert_currency


def get_transaction_amount_rub(transaction: Dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях."""
    amount: float = transaction.get("amount", 0.0)
    currency: str = transaction.get("currency", "RUB").upper()

    # Проверяем, что валюта допустима
    if currency not in ("USD", "EUR", "RUB"):
        return 0.0

    # Явно приводим тип к Literal, чтобы успокоить mypy
    allowed_currency: Literal["USD", "EUR", "RUB"] = cast(Literal["USD", "EUR", "RUB"], currency)

    if allowed_currency == "RUB":
        return amount
    else:
        converted: Optional[float] = convert_currency(amount, allowed_currency)
        return converted if converted is not None else 0.0
