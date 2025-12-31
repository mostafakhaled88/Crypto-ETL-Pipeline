from dags.medallion.gold_curation import curate_crypto_metrics

def test_curate_crypto_metrics():
    data = [
        {"symbol": "BTC", "price": 45000}
    ]

    metrics = curate_crypto_metrics(data)

    assert "symbol" in metrics[0]
    assert "price" in metrics[0]
