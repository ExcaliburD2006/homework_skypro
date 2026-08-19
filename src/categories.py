import json
from typing import List


class Product:
    """Товар."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Категория товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)


def create_categories_from_json(file_path: str) -> List[Category]:
    """Читает JSON-файл с категориями и товарами и создает объекты Category и Product."""
    with open(file_path, encoding="utf-8") as file:
        raw_categories = json.load(file)

    categories = []
    for raw_category in raw_categories:
        products = [
            Product(
                name=raw_product["name"],
                description=raw_product["description"],
                price=raw_product["price"],
                quantity=raw_product["quantity"],
            )
            for raw_product in raw_category["products"]
        ]
        categories.append(
            Category(
                name=raw_category["name"],
                description=raw_category["description"],
                products=products,
            )
        )

    return categories
