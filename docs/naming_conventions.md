Crypto Pipeline Naming Conventions
==================================

1\. Database Objects (PostgreSQL)
---------------------------------

We use **snake\_case** for all database-related identifiers to ensure compatibility across different SQL engines.

*   **Tables:** {layer}\_{description}
    
    *   _Examples:_ bronze\_raw\_prices, silver\_clean\_prices, gold\_daily\_metrics.
        
*   **Columns:** Descriptive nouns.
    
    *   _Examples:_ coin\_id, extracted\_at, volatility\_pct.
        
    *   _Note:_ Always include \_pct for percentages and \_at or \_date for time-based fields.
        
*   **Indexes:** idx\_{table\_name}\_{columns}
    
    *   _Example:_ idx\_gold\_daily\_metrics\_date.
        

2\. Airflow Orchestration
-------------------------

Airflow objects should reflect the business logic and the version of the pipeline.

*   **DAG IDs:** {architecture}\_{domain}\_pipeline\_v{version}
    
    *   _Example:_ medallion\_crypto\_pipeline\_v2.
        
*   **Task IDs:** {layer}\_task or {action}\_{layer}
    
    *   _Examples:_ bronze\_task, silver\_transform\_task.
        
*   **Connection IDs:** {service}\_{environment}
    
    *   _Example:_ postgres\_default, aws\_s3\_production.
        

3\. Python Code & Files
-----------------------

We follow **PEP 8** standards for Python scripts.

*   **Module Names:** Small letters, snake\_case.
    
    *   _Example:_ bronze\_extract.py, gold\_curation.py.
        
*   **Functions:** Verb-based snake\_case.
    
    *   _Example:_ extract\_from\_api(), parse\_payload(), load\_config().
        
*   **Constants:** ALL\_CAPS.
    
    *   _Example:_ CONFIG\_PATH, RETRY\_LIMIT.
        

4\. API Configuration (JSON)
----------------------------

Keys should be lowercase and represent the "type" of data they hold.

*   **Source Keys:** The official brand name of the provider (lowercase).
    
    *   _Example:_ "coingecko", "coincap".
        
*   **Parameters:** Use names that match the destination schema where possible to reduce mapping complexity.
    
    *   _Example:_ Using "vs\_currencies" in JSON because that is the term CoinGecko uses.
        

5\. Medallion Layer Definitions
-------------------------------

To keep the architecture clean, we strictly define what each prefix means:

**PrefixContent TypeRulebronze\_**Immutable / RawNo logic allowed. Raw JSON only.**silver\_**Cleaned / FilteredOne row per event. Type casting and deduplication only.**gold\_**Aggregated / FinalBusiness math only. Prepared for end-user consumption.
