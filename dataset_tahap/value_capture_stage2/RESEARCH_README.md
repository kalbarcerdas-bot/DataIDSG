# Tahap 2 — Investasi Langsung Singapura di Indonesia

**Diperiksa:** 24 Oktober 2026.

## Hasil
- 31 tahun stok FDI Singapura di Indonesia menurut SingStat, 1994–2024, satuan **juta dolar Singapura**.
- 31 tahun komponen ekuitas dan laba ditahan (equity capital + reserves), 1994–2024.
- Turunan net inter-company lending = total stok minus equity + reserves, 1994–2024; dapat negatif, jangan diperlakukan sebagai pinjaman baru.
- Tujuh observasi realisasi PMA asal Singapura menurut BKPM (2019–2025), satuan **juta dolar AS**. Angka 2019–2023 dan 2025 berasal dari angka miliar USD dibulatkan 1 desimal; 2024 dari BPS dalam jutaan USD.
- 2025 SingStat stock **NULL**; jangan membawa forward nilai 2024.

## Interpretasi penting
- **Stock (SGD)** adalah posisi pada tanggal 31 Desember. Selisih stock tidak sama dengan FDI flows karena perubahan valuasi, kurs, laba ditahan, divestasi dan pinjaman.
- **Equity + reserves** memuat modal serta akumulasi laba ditahan; jumlah ini tidak menunjukkan berapa laba yang dibagikan ke Singapura selama suatu tahun.
- **Net inter-company lending** berbeda dari bunga/penerimaan jasa pinjaman.
- **Realized PMA BKPM (USD)** adalah realisasi proyek dalam cakupan administrasi LKPM; tidak sama dengan investasi langsung dalam neraca pembayaran dan berbeda dari posisi DIA SingStat.
- Jangan jumlahkan angka SGD stock dan USD flow; tidak ada total value capture yang dapat dibuat dari tahap ini.
- Angka negara asal Singapura belum membuktikan pemilik akhir modal berasal dari Singapura.
- `income_capture_sgd_million` dan `ultimate_singapore_beneficiary_capture_sgd_million` sengaja dibiarkan kosong (NULL).

## Berkas
- `singapore_fdi_indonesia_1994_2025.csv` dan `.json`: data tahunan plus provenance.
- `stage2_source_registry.json`: sumber dan metode ekstraksi.
- `stage2_summary.json`: metrik turunan yang terukur.
- `STAGE2_FOLLOWUP.md`: backlog sumber pendapatan investasi dan sektor.
- `stage2_preview.html`: prototipe HTML standalone, datanya tersemat dan tidak memerlukan internet.

## Langkah validasi teknis
1. Unduh CSV asli seri SingStat M084431 dan M082271 untuk rekonsiliasi machine-to-machine. Baris di paket ini ditranskripsi secara manual dari tampilan sumber resmi (bukan arsip mentah hasil API).
2. Cari flow bilateral dari ASEANstats atau BI dan tuliskan metode pelaporan.
3. Cari pendapatan investasi (reinvested earnings, dividends, interest) dari BOP BI/ASEANstats atau corporate filings bila belum tersedia dalam country breakdown resmi.
4. Pada 2025 BPS/BKPM sudah ada realisasi PMA, namun posisi akhir tahun 2025 SingStat belum pada seri yang diperiksa.

## Sumber utama
- SingStat M084431: https://data.gov.sg/datasets/d_a1db0947cc69ae27d0ffb6ddfaf6cdde/view
- SingStat M082271: https://data.gov.sg/datasets/d_ace60be912e6400bbe08db8c704d6ccb/view
- SingStat methodology: https://www.singstat.gov.sg/find-data/explore-data-themes/trade-investment/direct-investment-abroad/our-data-explained
- BPS / BKPM 2024: https://www.bps.go.id/en/statistics-table/2/MTg0MyMy/realisasi-investasi-
- BKPM Renstra 2025–2029: https://jdih-storage.bkpm.go.id/jdih/jdih/2025Permeninveshil006-.pdf
- BKPM 2025 release: https://www.bkpm.go.id/index.php/id/info/siaran-pers/investment-realization-in-2025-exceeds-target-downstream-investment-jumps-43-3-percent
