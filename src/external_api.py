import os
import requests
from typing import Optional, Literal, Any
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_API_KEY: Optional[str] = os.getenv("EXCHANGE_RATES_API_KEY")
BASE_URL: str = "https://api.apilayer.com/exchangerates_data/convert"


def convert_currency(amount: float, from_currency: Literal["USD", "EUR", "RUB"]) -> Optional[float]:
    """Конвертирует сумму в рубли через API."""
    if from_currency == "RUB":
        return amount

    if not EXCHANGE_API_KEY:
        return None

    headers: dict[str, str] = {"apikey": EXCHANGE_API_KEY}
    params: dict[str, str | float] = {"from": from_currency, "to": "RUB", "amount": amount}

    try:
        response: requests.Response = requests.get(BASE_URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        result: dict[str, Any] = response.json()
        return result.get("result")  # type: ignore[no-any-return]
    except (requests.RequestException, KeyError):
        return None
