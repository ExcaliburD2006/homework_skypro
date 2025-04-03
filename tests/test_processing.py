import pytest
from src.processing import filter_by_state, sort_by_date

# Тесты для filter_by_state
@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("PENDING", 1),
    ("CANCELED", 1),
    ("UNKNOWN", 0)
])
def test_filter_by_state(sample_data, state, expected_count):
    result = filter_by_state(sample_data, state)
    assert len(result) == expected_count
    if expected_count > 0:
        assert all(item.get("state") == state for item in result)

def test_filter_by_state_type_error():
    with pytest.raises(TypeError):
        filter_by_state("not-a-list", "EXECUTED")

# Тесты для sort_by_date
@pytest.mark.parametrize("reverse, expected_dates", [
    (True, [
        "2023-11-20T15:45:30.456",
        "2023-10-01T00:00:00.000",
        "2023-09-15T12:30:45.123",
        "2023-08-05T08:10:15.789",
        "invalid-date"
    ]),
    (False, [
        "2023-08-05T08:10:15.789",
        "2023-09-15T12:30:45.123",
        "2023-10-01T00:00:00.000",
        "2023-11-20T15:45:30.456",
        "invalid-date"
    ])
])
def test_sort_by_date(sample_data, reverse, expected_dates):
    sorted_data = sort_by_date(sample_data, reverse)
    result_dates = [item.get("date", "") for item in sorted_data]
    assert result_dates == expected_dates

def test_sort_by_date_type_error():
    with pytest.raises(TypeError):
        sort_by_date("not-a-list")