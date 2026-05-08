from typing import Any, Dict, List, Type

import pytest
from pytest import raises

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    """Фикстура предоставляет тестовые данные для модуля processing."""
    return [
        {"state": "EXECUTED", "date": "2023-10-01T00:00:00.000"},
        {"state": "PENDING", "date": "2023-09-15T12:30:45.123"},
        {"state": "EXECUTED", "date": "2023-11-20T15:45:30.456"},
        {"date": "2023-08-05T08:10:15.789"},
        {"state": "CANCELED", "date": "invalid-date"}
    ]


@pytest.mark.parametrize(
    "state, expected_count",
    [
        pytest.param("EXECUTED", 2, id="executed_status"),
        pytest.param("PENDING", 1, id="pending_status"),
        pytest.param("CANCELED", 1, id="canceled_status"),
        pytest.param("UNKNOWN", 0, id="unknown_status"),
    ]
)
def test_filter_by_state(
    sample_data: List[Dict[str, Any]],
    state: str,
    expected_count: int
) -> None:
    """Тестирует фильтрацию операций по статусу."""
    result = filter_by_state(sample_data, state)
    assert len(result) == expected_count
    if expected_count > 0:
        assert all(item["state"] == state for item in result)


def test_filter_by_state_invalid_input() -> None:
    """Тестирует обработку невалидного ввода."""
    with raises(TypeError):
        filter_by_state("not-a-list", "EXECUTED")  # type: ignore


@pytest.mark.parametrize(
    "reverse, expected_dates",
    [
        pytest.param(
            True,
            [
                "2023-11-20T15:45:30.456",
                "2023-10-01T00:00:00.000",
                "2023-09-15T12:30:45.123",
                "2023-08-05T08:10:15.789",
                "invalid-date"
            ],
            id="descending_sort"
        ),
        pytest.param(
            False,
            [
                "2023-08-05T08:10:15.789",
                "2023-09-15T12:30:45.123",
                "2023-10-01T00:00:00.000",
                "2023-11-20T15:45:30.456",
                "invalid-date"
            ],
            id="ascending_sort"
        ),
    ]
)
def test_sort_by_date(
    sample_data: List[Dict[str, Any]],
    reverse: bool,
    expected_dates: List[str],
) -> None:
    """Тестирует сортировку операций по дате."""
    sorted_data = sort_by_date(sample_data, reverse=reverse)
    result_dates = [item.get("date", "") for item in sorted_data]
    assert result_dates == expected_dates


def test_sort_by_date_invalid_input() -> None:
    """Тестирует обработку невалидного ввода при сортировке."""
    with raises(TypeError):
        sort_by_date("not-a-list")  # type: ignore