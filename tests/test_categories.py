from typing import List

import pytest

from src.categories import Category, Product, create_categories_from_json


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    """Сбрасывает счетчики класса Category перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def products() -> List[Product]:
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


def test_product_init() -> None:
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_category_init(products: List[Product]) -> None:
    category = Category("Смартфоны", "Описание категории смартфонов", products)

    assert category.name == "Смартфоны"
    assert category.description == "Описание категории смартфонов"
    assert category.products == products


def test_category_count(products: List[Product]) -> None:
    Category("Смартфоны", "Описание категории смартфонов", products)
    assert Category.category_count == 1

    Category("Телевизоры", "Описание категории телевизоров", products[:1])
    assert Category.category_count == 2


def test_product_count(products: List[Product]) -> None:
    Category("Смартфоны", "Описание категории смартфонов", products)
    assert Category.product_count == len(products)

    Category("Телевизоры", "Описание категории телевизоров", products[:1])
    assert Category.product_count == len(products) + 1


def test_create_categories_from_json() -> None:
    categories = create_categories_from_json("data/products.json")

    assert len(categories) == 2
    assert Category.category_count == 2

    smartphones = categories[0]
    assert smartphones.name == "Смартфоны"
    assert len(smartphones.products) == 3
    assert smartphones.products[0].name == "Samsung Galaxy S23 Ultra"

    assert Category.product_count == 4
