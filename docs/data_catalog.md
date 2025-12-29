Crypto Pipeline Data Catalog
============================

**Project Name:** Medallion Crypto ETL

**Orchestrator:** Apache Airflow

**Database:** PostgreSQL

**Update Frequency:** Daily (@daily)

🟫 Bronze Layer (Raw)
---------------------

**Table Name:** bronze\_raw\_prices

**Description:** Contains the exact, untouched JSON response from the external APIs. This is the source of truth for all downstream tables.

**ColumnTypeDescription**logical\_dateDATE**Primary Key.** The Airflow execution date (YYYY-MM-DD).source\_nameTEXT**Primary Key.** Either coingecko or coincap.raw\_json\_payloadJSONBThe full, unparsed data returned by the API.extracted\_atTIMESTAMPThe physical time the data was written to the DB.

⬜ Silver Layer (Cleaned)
------------------------

**Table Name:** silver\_clean\_prices

**Description:** Normalized data where different API formats are converted into a single, consistent schema.

**ColumnTypeDescription**coin\_idTEXTUnique ID for the coin (e.g., 'bitcoin').vs\_currencyVARCHARThe currency the price is quoted in (USD, EUR).priceNUMERICThe price at the time of extraction.source\_nameTEXTThe provider that supplied this specific price.source\_timestampTIMESTAMPThe time the API call was made.processed\_timestampTIMESTAMPThe time the Silver transformation ran.

🟨 Gold Layer (Business Metrics)
--------------------------------

**Table Name:** gold\_daily\_metrics

**Description:** High-level daily aggregations and performance indicators. Optimized for dashboards.

**ColumnTypeDescription**metric\_dateDATE**Primary Key.** The date these metrics represent.coin\_idTEXT**Primary Key.** The cryptocurrency ID.vs\_currencyVARCHAR**Primary Key.** The quote currency.avg\_priceNUMERICArithmetic mean of all prices captured that day.min\_priceNUMERICThe lowest price recorded that day.max\_priceNUMERICThe highest price recorded that day.volatility\_pctNUMERICIntraday price swing: ((Max - Min) / Min) \* 100.daily\_change\_pctNUMERICPerformance vs. previous day: ((TodayAvg - PrevAvg) / PrevAvg) \* 100.

### 🛠️ Maintenance & Lineage

*   **Upstream:** CoinGecko API (/simple/price), CoinCap API (/assets).
    
*   **Transformation:** All logic is handled via Python in the medallion package.
    
*   **Ownership:** Data Engineering Team.
