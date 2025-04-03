import pytest
from src.processing import filter_by_state, sort_by_date
from datetime import datetime

@pytest.fixture
def sample_data():
    return [
        {"state": "EXECUTED", "date": "2023-10-01T00:00:00.000"},
        {"state": "PENDING", "date": "2023-09-15T12:30:45.123"},
        {"state": "EXECUTED", "date": "2023-11-20T15:45:30.456"},
        {"date": "2023-08-05T08:10:15.789"}  # Элемент без 'state'
    ]

def test_filter_by_state(sample_data):
    filtered = filter_by_state(sample_data, "EXECUTED")
    assert len(filtered) == 2
    assert all(item["state"] == "EXECUTED" for item in filtered)

def test_filter_by_state_empty(sample_data):
    filtered = filter_by_state(sample_data, "UNKNOWN")
    assert len(filtered) == 0

def test_sort_by_date_desc(sample_data):
    sorted_data = sort_by_date(sample_data)
    dates = [item["date"] for item in sorted_data if "date" in item]
    expected = [
        "2023-11-20T15:45:30.456",
        "2023-10-01T00:00:00.000",
        "2023-09-15T12:30:45.123",
        "2023-08-05T08:10:15.789"
    ]
    assert dates == expected

def test_sort_by_date_asc(sample_data):
    sorted_data = sort_by_date(sample_data, reverse=False)
    dates = [item["date"] for item in sorted_data if "date" in item]
    expected = [
        "2023-08-05T08:10:15.789",
        "2023-09-15T12:30:45.123",
        "2023-10-01T00:00:00.000",
        "2023-11-20T15:45:30.456"
    ]
    assert dates == expected