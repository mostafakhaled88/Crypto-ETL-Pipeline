from dags.medallion.gold_curation import curate_crypto_metrics
import json
import os

def test_curate_crypto_metrics():
    os.makedirs("./dags/data/silver", exist_ok=True)
    cleaned_data = [{"symbol": "BTC", "price": 45000}, {"symbol": "ETH", "price": 3000}]
    with open("./dags/data/silver/crypto_cleaned.json", "w") as f:
        json.dump(cleaned_data, f)

    top_crypto = curate_crypto_metrics()
    assert top_crypto[0]["symbol"] == "BTC"
    assert top_crypto[1]["symbol"] == "ETH"
