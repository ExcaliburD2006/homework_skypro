# Проект: Обработка финансовых транзакций

## Описание:

Проект предоставляет набор инструментов для работы с финансовыми транзакциями. Включает функции для фильтрации, сортировки и маскировки данных, таких как номера карт и счетов. Проект написан на Python и может быть легко интегрирован в другие приложения для обработки финансовых данных.

## Установка:

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/ваш-репозиторий.git
   ```

2. Установите зависимости:
```
pip install -r requirements.txt
```

## Использование:

1. Файл masks.py:
```
Содержит функции для маскировки номеров карт и счетов.


Функции:
get_mask_card_number(card_number: Union[int]) -> str
Маскирует номер карты, оставляя первые 4 цифры и последние 4 цифры.
Пример:
masked_card = get_mask_card_number("1234567890123456")
print(masked_card)  # "1234 56** **** 3456"


get_mask_account(account_number: Union[int]) -> str
Маскирует номер счета, оставляя последние 4 цифры.
Пример:
masked_account = get_mask_account("1234567890")
print(masked_account)  # "**7890"
```
2. Файл processing.py:
```
Содержит функции для фильтрации и сортировки транзакций.


Функции:
filter_by_state(transactions: list[dict], state: str = 'EXECUTED') -> list[dict]
Фильтрует список транзакций по значению ключа state.
Пример:
filtered_transactions = filter_by_state(transactions, state='EXECUTED')


sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]
Сортирует список транзакций по дате. По умолчанию сортировка по убыванию.
Пример:
sorted_transactions = sort_by_date(transactions, reverse=False)
```
3. Файл widget.py:
```
Содержит функции для маскировки номеров карт и счетов, а также преобразования дат.


Функции:
mask_card_number(number: str) -> str
Маскирует номер карты, оставляя первые 4 и последние 4 цифры.
Пример:
masked_card = mask_card_number("1234567890123456")
print(masked_card)  # "1234 56** **** 3456"


mask_account_number(number: str) -> str
Маскирует номер счета, оставляя последние 4 цифры.
Пример:
masked_account = mask_account_number("1234567890")
print(masked_account)  # "**7890"


mask_card_or_account(text: str) -> str
Маскирует номер карты или счета в переданной строке.
Пример:
masked_text = mask_card_or_account("Счет 1234567890")
print(masked_text)  # "Счет **7890"


get_date(date_str: str) -> str
Преобразует дату из формата ISO 8601 в строку формата ДД.ММ.ГГГГ.
Пример:
formatted_date = get_date("2023-10-01T12:34:56")
print(formatted_date)  # "01.10.2023"
```


## Документация:
Дополнительную информацию о структуре проекта и API можно найти в [документации](docs/README.md).


## Лицензия:
Проект распространяется под [лицензией MIT](LICENSE).