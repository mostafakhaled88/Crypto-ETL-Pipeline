from dags.medallion.silver_transform import transform_crypto_data
import json
import os

def test_transform_crypto_data():
    # Prepare fake raw data
    os.makedirs("./dags/data/bronze", exist_ok=True)
    raw_data = [{"symbol": "BTC", "price": "45000"}]
    with open("./dags/data/bronze/crypto_raw.json", "w") as f:
        json.dump(raw_data, f)

    cleaned = transform_crypto_data()

    assert cleaned[0]["symbol"] == "BTC"
    assert isinstance(cleaned[0]["price"], float)
    assert cleaned[0]["price"] == 45000.0
