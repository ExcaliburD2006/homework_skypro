import unittest
from unittest.mock import patch, Mock
from src.transactions import get_transaction_amount_rub


class TestTransactions(unittest.TestCase):
    # Тест для RUB без конвертации
    @patch("src.external_api.convert_currency")
    def test_rub_transaction(self, mock_convert: Mock) -> None:
        transaction = {"amount": 100.0, "currency": "RUB"}
        result = get_transaction_amount_rub(transaction)
        self.assertEqual(result, 100.0)
        mock_convert.assert_not_called()

    # Тест для USD с успешной конвертацией
    @patch("src.external_api.convert_currency")
    def test_eur_transaction_success(self, mock_convert: Mock) -> None:
        mock_convert.return_value = 8500.0  # Исправлено: возвращаем float
        transaction = {"amount": 100.0, "currency": "EUR"}
        result = get_transaction_amount_rub(transaction)
        self.assertEqual(result, 8500.0)

    @patch("src.external_api.convert_currency")
    def test_usd_transaction_success(self, mock_convert: Mock) -> None:
        # Указываем, что мок возвращает float
        mock_convert.return_value = 7500.0  # Исправлено: возвращаем float, а не None
        transaction = {"amount": 100.0, "currency": "USD"}
        result = get_transaction_amount_rub(transaction)
        self.assertEqual(result, 7500.0)
        mock_convert.assert_called_once_with(100.0, "USD")

    # Тест для ошибки конвертации
    @patch("src.external_api.convert_currency")
    def test_conversion_failure(self, mock_convert: Mock) -> None:
        mock_convert.return_value = None
        transaction = {"amount": 100.0, "currency": "USD"}
        result = get_transaction_amount_rub(transaction)
        self.assertEqual(result, 0.0)

    # Тест для неизвестной валюты
    def test_unknown_currency(self) -> None:
        transaction = {"amount": 100.0, "currency": "GBP"}
        result = get_transaction_amount_rub(transaction)
        self.assertEqual(result, 0.0)

    # Тест для отсутствия ключа currency
    def test_missing_currency(self) -> None:
        transaction = {"amount": 100.0}
        result = get_transaction_amount_rub(transaction)
        self.assertEqual(result, 100.0)  # Должен использовать RUB по умолчанию

    # Тест для некорректного типа суммы
    def test_invalid_amount_type(self) -> None:
        transaction = {"amount": "100", "currency": "USD"}
        result = get_transaction_amount_rub(transaction)
        self.assertEqual(result, 0.0)

    # Тест для отрицательной суммы
    def test_negative_amount(self) -> None:
        transaction = {"amount": -50.0, "currency": "USD"}
        result = get_transaction_amount_rub(transaction)
        self.assertEqual(result, 0.0)


if __name__ == "__main__":
    unittest.main()
