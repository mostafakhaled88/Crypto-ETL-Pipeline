from dags.medallion.bronze_extract import extract_crypto_data
import pytest
from unittest.mock import patch, Mock

@patch("dags.medallion.bronze_extract.requests.get")
def test_extract_crypto_data(mock_get):
    # Mock API response
    mock_get.return_value = Mock()
    mock_get.return_value.json.return_value = [
        {"symbol": "BTC", "price": "45000"}
    ]

    data = extract_crypto_data()

    assert isinstance(data, list)
    assert data[0]["symbol"] == "BTC"
    assert float(data[0]["price"]) == 45000
