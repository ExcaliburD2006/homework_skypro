import pytest

# Общие данные для processing
@pytest.fixture
def sample_data():
    return [
        {"state": "EXECUTED", "date": "2023-10-01T00:00:00.000"},
        {"state": "PENDING", "date": "2023-09-15T12:30:45.123"},
        {"state": "EXECUTED", "date": "2023-11-20T15:45:30.456"},
        {"date": "2023-08-05T08:10:15.789"},
        {"state": "CANCELED", "date": "invalid-date"}
    ]
