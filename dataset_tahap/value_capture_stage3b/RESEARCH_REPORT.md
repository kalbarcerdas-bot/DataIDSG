# Tahap 3B — Rincian Jasa Bilateral Indonesia–Singapura

**Per tanggal 24 Oktober 2026. Status: ekstraksi kategori belum selesai; program validasi dan visualisasi siap digunakan.**

## Pertanyaan riset

Dari ekspor jasa Singapura ke Indonesia dan impor jasa Singapura dari Indonesia, kategori mana yang mencatat nilai transaksi dan surplus paling besar setiap tahun? Bisakah perubahan tersebut dijelaskan oleh transportasi, jasa keuangan, jasa bisnis, perjalanan, asuransi, IP, atau kategori lain?

## Bukti yang sudah diperoleh

1. SingStat **M060261**: Exports Of Services By Major Trading Partner And Services Category, Annual (2000–2024; 286 baris), https://data.gov.sg/datasets/d_bff5c93e3d5a7153df64a968afcc7d5b/view
2. SingStat **M060271**: Imports Of Services By Major Trading Partner And Services Category, Annual (2000–2024; 286 baris), https://data.gov.sg/datasets/d_addeac819bfa848fdcc255dd6637484c/view
3. Definisi dan daftar **12 kategori**: https://www.singstat.gov.sg/find-data/explore-data-themes/trade-investment/trade-in-services/our-data-explained
4. Sumber kontrol total dari Tahap 3A: SingStat M060201 (ekspor) dan M060211 (impor). Tahun 2024: ekspor S$7.857,7 juta; impor S$4.268,7 juta; saldo S$3.589,0 juta.
5. Portal data.gov.sg memuat opsi unduhan resmi CSV, tetapi halaman yang dapat dibaca di sesi riset ini hanya membuka sejumlah baris paling awal (**Asia**), bukan seluruh baris khusus Indonesia. Koneksi API dari lingkungan berkas ini gagal. **Belum ada angka rinci Indonesia yang terverifikasi**. Nominal Asia/nasional tidak digunakan sebagai pengganti.

## Struktur kerja

- Ekstrak baris `Indonesia` + 12 kategori turunannya dari kedua CSV.
- Pertahankan nilai mentah, sumber, tanda `na`, tahun, satuan **juta dolar Singapura (SGD juta)**.
- Hitung `saldo = exports - imports` tiap kategori dan tahun, asalkan keduanya tersedia.
- Hitung `sum(exports_category)` serta `sum(imports_category)`, dan bandingkan dengan total dari M060201/M060211. Toleransi selisih pembulatan sementara **S$1,5 juta**. Jika melebihi ambang, **wajib investigasi sumber/methodology**; jangan menyesuaikan angka otomatis.
- Jika ada nilai kategori kosong, seri tidak dinyatakan lengkap; sel kosong **bukan nol**.
- Tahun 2025 tetap belum tersedia untuk serangkaian data bilateral yang digunakan.
- Publikasi peringkat kategori hanya untuk **tahun dengan rekonsiliasi lengkap**.

## Batas interpretasi

Surplus jasa bukan laba bersih, bukan nilai tambah Singapura, dan bukan pendapatan pemegang saham. Klasifikasi statistik didasarkan pada jasa menurut transaksi residen lintas negara (SingStat/BOP). Misalnya pengeluaran turis untuk perjalanan dapat muncul sebagai `travel` tetapi tidak menjelaskan laba bersih hotel atau perusahaan induk. Layanan keuangan yang dibeli Indonesia juga tidak sama dengan arus bunga atas utang atau dividen investasi. Jangan tambahkan jasa yang sama kembali dari laporan keuangan perusahaan.

## Isi berkas

- `outputs/stage3b_preview.html` — panel interaktif mandiri dengan data total Tahap 3A dan sel kategori kosong secara jujur.
- `outputs/stage3b_services_category_long_2003_2025.csv` — template 12 kategori × 23 tahun; sel kosong akan diisi pipeline setelah sumber diperoleh.
- `outputs/stage3b_reconciliation_2003_2025.csv` — tabel quality gate tahunan.
- `outputs/stage3b_dashboard_data.json` — payload HTML siap pakai.
- `build_stage3b.py` — program pengambilan API publik, pemilahan Indonesia, kalkulasi, validasi dan ekspor HTML.
- `HERMES_API_TASK.md` — instruksi hanya untuk memperoleh dua CSV melalui API resmi bila dibutuhkan.
- `inputs/bilateral_services_singstat_2003_2025.csv` — arsip angka agregat hasil Tahap 3A (tetap memerlukan recheck terhadap file primer penerbit).

## Kesiapan

Kita bisa menerbitkan HTML *baseline* sekarang, tetapi bukan grafik kontribusi kategori sampai CSV primer Indonesia lolos quality gate. Ambang selesai Tahap 3B: 12 kategori diekstraksi, 2003–2024 diisi sejauh tersedia, 2024 cocok dengan angka kontrol dan setiap tahun punya status lolos / gagal / kurang data.
