# Tahap 3 — Perdagangan Jasa Bilateral Indonesia–Singapura

Dibuat: 2026-10-24. Periode utama: **2003–2025**. Ketersediaan bilateral terverifikasi: **2003–2024**.

## Angka utama (SGD juta, harga berlaku)

- Ekspor jasa Singapura ke Indonesia 2024: **7,857.7**.
- Impor jasa Singapura dari Indonesia 2024: **4,268.7**.
- Surplus jasa Singapura 2024: **3,589.0**.
- Akumulasi ekspor 2003–2024: **103,840.5**.
- Akumulasi impor 2003–2024: **49,114.2**.
- Akumulasi selisih 2003–2024: **54,726.3**.
- CAGR ekspor: **7.36%**, CAGR impor: **6.55%** (21 interval tahunan).
- Saldo positif untuk Singapura dalam **22 dari 22 tahun**.
- Tahun saldo positif tertinggi: **2022** (S$4,781.1 juta).

## Definisi dan batasan

1. Sudut pandang **Singapore reporter**: `exports` adalah jasa yang diberikan residen SG ke residen Indonesia; `imports` kebalikannya.
2. Data nominal dalam **SGD juta**, **bukan USD** dan bukan perdagangan barang.
3. `surplus = exports - imports`, bukan laba dan bukan jumlah value capture pemegang saham.
4. SingStat mengukur transaksi layanan lintas residen; kategori biaya layanan mencakup perjalanan, transportasi, keuangan, bisnis, IP dan lain-lain. Pemeriksaan kategori Indonesia dilakukan tersendiri.
5. Data 2025 untuk mitra Indonesia *tidak tersedia dalam seri M060201/M060211 yang diperiksa*; nilai null tetap null.
6. Jumlah lintas tahun adalah akumulasi **nominal**, bukan nilai riil (belum disesuaikan inflasi/kurs).
7. Angka diekstraksi dari baris Indonesia yang terlihat pada data explorer SingStat; file CSV penerbit asli belum diambil melalui download API, sehingga metadata menyebut bentuk transkripsi dan perlu direkonsiliasi bila CSV asli tersedia.
8. SingStat technical note menjelaskan bahwa sebagian sumber tambahan statistik jasa tidak memiliki pemisahan mitra negara. Karenanya data bilateral bisa berbeda cakupannya dari agregat nasional.

## Sumber primer

- SingStat M060201: https://data.gov.sg/datasets/d_ae32bc57f36f0d99d2f892a1f3241a7b/view
- SingStat M060211: https://data.gov.sg/datasets/d_15fff4cec9a5a41a90655a37195297ef/view
- SingStat kategori ekspor M060261: https://data.gov.sg/datasets/d_bff5c93e3d5a7153df64a968afcc7d5b/view
- SingStat kategori impor M060271: https://data.gov.sg/datasets/d_addeac819bfa848fdcc255dd6637484c/view
- SingStat industri ekspor M060361: https://data.gov.sg/datasets/d_3dbf4c3eec72cfccac3ad1f75e1d3adb/view
- SingStat industri impor M060371: https://data.gov.sg/datasets/d_0267c40931b02c8cad4b56e41e6e35c7/view
- Penjelasan metodologi SingStat: https://www.singstat.gov.sg/find-data/explore-data-themes/trade-investment/trade-in-services/our-data-explained

## Rencana Tahap 3B

1. Unduh empat CSV resmi kategori/industri dari data.gov.sg (via API publik atau ekspor CSV, tidak perlu Scrapling jika API berhasil).
2. Ekstrak hanya Indonesia, pertahankan relasi parent/child kategori secara eksplisit.
3. Rekonsiliasi total 2024: ekspor 7,857.7 dan impor 4,268.7 SGD juta. Jika ada selisih, jelaskan cakupan statistik, tanpa mengisi data sendiri.
4. Kategorikan transport, travel, financial, insurance, business, telekomunikasi, IP. Jangan menggunakan agregat global Singapura sebagai pengganti angka bilateral.
5. Uji aktivitas trading-related services dan nilai tambah tersendiri; hindari double counting terhadap komoditas maupun FDI.
6. Lakukan mirror comparison dengan data Indonesia/OECD BaTIS menggunakan kurs yang konsisten dan cakupan statistik yang dicatat.

## Struktur data

- `bilateral_services_singstat_2003_2025.csv`: panel utama (22 tahun observasi + 2025 NA).
- `bilateral_services_long_2003_2025.csv`: format tidy untuk chart.
- `bilateral_services_full_2000_2024.csv`: tambahan observasi 2000–2002 untuk konteks.
- `bilateral_services_singstat_2003_2025.json`: website feed.
- `category_sector_source_registry.csv`: seri yang masih perlu diambil.
- `services_category_template.csv`: template eksplisit kosong, **BUKAN data numerik**.
- `stage3_preview.html`: halaman HTML lokal dengan data internal yang bisa dibaca offline.
