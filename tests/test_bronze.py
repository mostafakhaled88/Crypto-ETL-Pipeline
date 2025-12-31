from dags.medallion.bronze_extract import extract_crypto_data

def test_extract_crypto_data(mocker):
    mock_response = [
        {"symbol": "BTC", "price": 45000}
    ]

    mocker.patch(
        "dags.medallion.bronze_extract.requests.get",
        return_value=mocker.Mock(json=lambda: mock_response)
    )

    data = extract_crypto_data()

    assert data[0]["symbol"] == "BTC"
