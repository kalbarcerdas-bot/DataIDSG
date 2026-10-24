# Kamus data terpilih

| Field | Satuan dan makna | Risiko salah tafsir |
|---|---|---|
| `coal_production_million_tonnes` | Juta ton produksi tahunan Bayan | Produksi tidak selalu sama dengan penjualan tahunan |
| `consolidated_revenue_usd_million` | Juta dolar AS pendapatan konsolidasi | Bukan laba ataupun manfaat yang menjadi hak Singapura |
| `dividend_total_usd` | Total dividen yang diumumkan, untuk semua pemegang | Bukan pembayaran individu |
| `estimated_dividend_idr` | Hak dividen hasil perkalian dengan proxy saham | Bukan pembayaran neto/uang lintas negara |
| `direct_ownership_percent_calculated` | Hak saham langsung pada tanggal tertentu | Tidak selalu mencerminkan kendali hak suara |
| `amount_nominal` | Nominal hibah/komitmen dalam mata uang aslinya | Donasi diumumkan tidak selalu sudah dicairkan |
| `education_ppm_idr_bn` | Miliar rupiah bidang pendidikan PPM | Bukan seluruh pendidikan Banyan Peduli/yayasan |
| `has_smp`, `has_sma` | Indikator fasilitas setempat per desa | Bukan persentase siswa tidak sekolah |
| `capex_idr_bn`, `annual_opex_school_idr_bn` | Model sekolah hipotetis dalam miliar rupiah | Bukan RAB pemerintah |
| `source_id` | ID hanya unik di tahap asal | Gabungkan dengan namespace tahap, mis. `S9.5:S01` |

Detail skema lengkap setiap CSV berada dalam `catalog/datasets.csv`, kolom `fields`.
