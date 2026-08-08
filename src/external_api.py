from typing import Literal
import requests
import os
from dotenv import load_dotenv  # type: ignore[import-not-found]

load_dotenv()

EXCHANGE_API_KEY: str | None = os.getenv("EXCHANGE_RATES_API_KEY")
BASE_URL: str = "https://api.apilayer.com/exchangerates_data/convert"


def convert_currency(amount: float, from_currency: Literal["USD", "EUR", "RUB"]) -> float:
    """Конвертирует сумму в рубли через API. Возвращает 0.0 при ошибках."""
    if from_currency == "RUB":
        return float(amount)

    if not EXCHANGE_API_KEY:
        return 0.0

    headers: dict[str, str] = {"apikey": EXCHANGE_API_KEY}
    params: dict[str, str | float] = {"from": from_currency, "to": "RUB", "amount": amount}

    try:
        response: requests.Response = requests.get(BASE_URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        result: dict = response.json()

        # Проверяем тип возвращаемого результата
        converted = result.get("result")
        if isinstance(converted, (int, float)):
            return float(converted)
        return 0.0

    except (requests.RequestException, KeyError, TypeError):
        return 0.0
