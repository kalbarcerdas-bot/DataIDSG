# Backlog Tahap 1 — audit and extension

## Already completed
- [x] BPS exports by destination 2003–2025, US$ million FOB
- [x] BPS imports by origin 2003–2025, US$ million CIF
- [x] Derived Indonesia trade balance and YoY growth
- [x] Provenance registry and JSON for future HTML

## Next steps in this chat (do not use Hermes yet)
1. Acquire SingStat merchandise exports **to Indonesia** by reporter Singapore. Separate *domestic exports* from *re-exports* and identify total exports definitions. Confirm Singapore imports *from Indonesia* and origin vs consignment approach.
2. Extract 2003–2025 original reported mirror statistics, noting source changes and conversion from SGD to USD (do not mix currencies).
3. Acquire HS2 priority commodity exports Indonesia→Singapore and imports Singapore→Indonesia (2010, 2015, 2020, 2022, 2023, 2024, 2025 first; then backfill 2003–2025). Preserve HS revision year, nomenclature and reported gross vs net weight.
4. High priority HS: 27 mineral fuels; 15 fats/oils including palm; 72 iron and steel; 75 nickel; 85 electrical goods; 84 machinery; 29 organic chemicals; 39 plastics. Validate relevance against observed top products rather than assume all are large.
5. Import UN Comtrade/ITC Trade Map data where accessible openly, compare with BPS and SingStat, investigate material discrepancies.
6. Release reconciled mirror comparison with caveats and version log, then produce HTML graphics.

## Escalation to Hermes + Scrapling
Only if the official SingStat bulk/API or UN Comtrade preview/free quota cannot efficiently deliver complete historical data, or if retrieving hundreds of historical HS files is required. Use approved public endpoints; do not bypass login, paywalls, or rate limits. Output raw CSV, source page URL, extraction logs, hashes and retries.
