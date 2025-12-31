from dags.medallion.silver_transform import transform_crypto_data

def test_transform_crypto_data():
    raw_data = [
        {"symbol": "BTC", "price": "45000"}
    ]

    cleaned = transform_crypto_data(raw_data)

    assert cleaned[0]["symbol"] == "BTC"
    assert isinstance(cleaned[0]["price"], float)
