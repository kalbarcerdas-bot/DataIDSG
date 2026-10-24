# Indonesia–Singapore Economic Value Capture Observatory | Tahap 1

**Status:** Historical bilateral merchandise trade from the Indonesia reporter perspective, 2003–2025. Extracted 24 October 2026 from official BPS tables and historical BPS publications.

## Files
- `bilateral_trade_bps_2003_2025.csv`: 23 official annual Indonesia reporter observations, export FOB + import CIF, USD million.
- `bilateral_trade_bps_2003_2025.json`: same data, ready for website consumption.
- `source_registry.json`: source identifiers, institutions and metadata.
- `stage1_summary.json`: verified aggregates and descriptive metrics.
- `mirror_singapore_LEADS_UNVERIFIED.csv`: **quarantined research leads** from third-party rendering attributed to UN Comtrade. NOT verified directly against Singapore source; do not present as official, do not merge without validation.
- `stage1_workplan.md`: next acquisition steps including HS commodity breakdown.

## Accounting rules
- BPS exports to Singapore use FOB and partner **destination**, whereas BPS imports from Singapore use CIF and partner **origin**.
- Gross trade is `exports + imports`; net trade is `exports - imports` **from Indonesia's perspective**.
- USD million at contemporary prices; no inflation adjustment.
- Do not treat trade balance, gross trade, Singapore's exports or bilateral reporting asymmetry as Singapore's profit/value capture.
- Partner attribution, entrepot trade, re-exports, valuation, shipping, timing, transshipment and customs regimes may explain mirror differences.
- 2025 is listed by BPS but status/provisional flags require checking before calling it final.
- 2017 has 0.1 million revision differences between an older bulletin and the latest BPS table; the latest table is used.
- Some BPS website routes give HTTP 403 when opened programmatically; the indexed table and two PDF table screenshots were checked. Official PDF source locators are preserved in source_registry.json.

## Data handling
Values copied as published with one decimal USD million; derived balances/totals to one decimal, growth rate to 0.01%. Exports were taken from the currently indexed BPS export partner table, imports from historical BPS PDF tables 6.12.1 plus current BPS partner table.

## Known limitations
- Not Singapore-reporter mirror statistics yet.
- Not HS-level sector data yet.
- Not an attribution of profits, domestic value added, ownership, or trade margins.
- The current package is an auditable manual extraction / research checkpoint, not a reproducible API-pulled raw source dump.

## Citation index
Export: https://www.bps.go.id/en/statistics-table/1/MTAxMCMx/nilai-ekspor-menurut-negara-tujuan-utama-nilai-fob-juta-us-2000-2022.html
Import 2017–2025: https://www.bps.go.id/en/statistics-table/1/MTAzNiMx/value-of-imports-by-major-countries-of-origi
Import 2003–2009: BPS Economic Indicators PDF, Table 6.12.1, p.103, PDF page index 119.
Import 2010–2016: BPS Economic Indicators September 2018 PDF, Table 6.12.1, p.132, PDF page index 150.
Official Singapore sources for follow-up: https://tablebuilder.singstat.gov.sg/table/TS/M450091 and https://tablebuilder.singstat.gov.sg/table/TS/M450081

## Singapore trade taxonomy (official)
SingStat defines `total merchandise exports = domestic exports + re-exports`. Re-exports are goods exported in substantially the same form as originally imported; simple packaging, grading, repacking are not considered substantial transformation. Trade recorded by Singapore can differ from partner-reported imports due to country-of-origin vs country-of-destination conventions. Official definitions: https://www.singstat.gov.sg/find-data/explore-data-themes/trade-investment/merchandise-trade/our-data-explained and https://statlink.enterprisesg.gov.sg/pages/Misc/Glossary.aspx.
