# Handoff Penulisan Artikel dan Analisis

## Workflow singkat

1. Pilih topik di `content/articles/INDEX.md`.
2. Temukan klaim dan status di `catalog/claims.csv`.
3. Cari file dan skema melalui `catalog/datasets.csv`.
4. Telusuri URL asli pada `catalog/sources.csv` dan registry per tahap.
5. Analisis angka dengan melihat unit, tahun buku, tanggal transaksi, dan sifat nilai.
6. Jika ingin memublikasikan, pilih CSV pada `public-data/` dan tautkan unduhan dari `docs/downloads`.
7. Lengkapi hak jawab pada klaim kontroversial.

## Contoh analisis terprogram (Python tanpa dependensi)

```python
import csv
path = 'public-data/bayan_annual_2008_2026H1.csv'
with open(path, encoding='utf-8-sig', newline='') as f:
    rows = list(csv.DictReader(f))
period = [r for r in rows if r['period_type'] == 'FY' and 2015 <= int(r['year']) <= 2025]
tonnage = sum(float(r['coal_production_million_tonnes']) for r in period)
print('Produksi (juta ton), 2015-2025:', round(tonnage, 2))
```

Bukan estimasi laba ataupun arus kas lintas negara.

## Kategori angka yang tidak boleh dijumlahkan

- Nilai pasar saham yang dihibahkan dan hasil penjualan saham itu kemudian.
- Dividen perusahaan dan dividen seorang pemegang atas bagian yang sama.
- NUS S$101 juta dan total donasi yayasan 2023 bila sudah termasuk NUS.
- Penerimaan induk multinasional dengan seluruh ekspor industri Indonesia.
- FDI stock, pendapatan investasi, dan arus modal masuk.
