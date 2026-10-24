# TAHAP 2B — Investasi Singapura di Indonesia: sektor dan pendapatan

Diperiksa: 2026-10-24. Scope: sumber publik saja. Berkas siap untuk digabung dengan riset 2A / website nanti.

## Hasil yang benar-benar diekstrak

- Tambahan **31 observasi tahunan 1994–2024** tentang besarnya Indonesia dibanding stok investasi Singapura di seluruh dunia dan di Asia. Nilai denominator SingStat M081971 adalah agregat GLOBAL/ASIA, sedangkan numerator seri Indonesia M084431. Semua dalam **juta SGD posisi akhir tahun**.
- Tahun 2024: Indonesia S$104.285,4 juta; seluruh dunia S$1.652.795,5 juta; Asia S$865.555,8 juta; porsi Indonesia 6.31% global / 12.048% Asia.
- Tahun 2003: Indonesia S$10.303,7 juta; seluruh dunia S$152.968,7 juta; Asia S$75.968,2 juta; porsi Indonesia 6.736% global / 13.563% Asia.
- Statistik dalam laporan tahunan 2024 mengenai distribusi industri adalah **GLOBAL**, bukan rincian khusus Indonesia. Jangan menempelkan persentase global pada Indonesia.

## Sektor — ditemukan sumbernya, belum ada angka per sektor

1. SingStat **M081971** menunjukkan industri dari perusahaan penerima investasi di negara tujuan (destination economy and industry abroad), 330 data series, 1994–2024.
2. SingStat **M082051** menunjukkan industri investor yang berdomisili di Singapura (destination economy and industry of investor in Singapore), 330 data series, 1994–2024.
3. `stage2b_indonesia_sector_import_template.csv` secara sengaja membiarkan field sektor/nilai kosong. Wajib diisi setelah mengunduh CSV lengkap dari portal pemerintah Singapura dan memverifikasi hierarki seri Indonesia.
4. Jangan menjumlahkan dua klasifikasi sektor tersebut; keduanya cara **pengelompokan yang berbeda** atas stok investasi yang sama.

## Pendapatan investasi — status belum diketahui, bukan nol

- Tidak ditemukan seri publik tahunan yang diverifikasi untuk **pendapatan FDI spesifik Singapura <- Indonesia** pada hasil pemeriksaan ini.
- BI menerbitkan neraca pendapatan primer / FDI income **semua mitra**, tetapi jangan diklaim sebagai pendapatan hanya untuk Singapura.
- OECD punya definisi dan dataset pendapatan bilateral, tetapi pastikan cakupan reporting economy dan partner: jangan menganggap Indonesia/Singapura tersedia hanya karena nama Indonesia muncul sebagai counterpart di contoh.
- `stage2b_fdi_income_missingness_2003_2025.csv` menyimpan nilai BLANK untuk 2003–2025. BLANK berarti belum didapat/verifikasi; bukan nilai 0.
- Income = equity earnings (dividends + reinvested earnings) + net interest on intercompany debt, dengan definisi dan penyesuaian yang berlaku. *Total income* tidak boleh ditambahkan lagi kepada masing-masing komponen.
- Stok investasi/pertumbuhan stok **bukan return**.
- Emiten (SGX/BEI) dapat dipakai untuk studi kasus jika bagian laba dari entitas Indonesia bisa dipisah dengan bukti yang cukup. Jangan generalisasikan laba emiten terhadap seluruh populasi.

## Rekomendasi pengumpulan sektor

1. Download langsung CSV publik `d_dea084e8924680c954f1569a27f6d96c` dan `d_3dcfd9108ee04bd2b7978d6eaab1ed9a` dari portal data.gov.sg.
2. Simpan sumber RAW apa adanya; buat fingerprint SHA-256.
3. Pastikan baris Indonesia/industri; periksa total kelompok pada 2024 = 104285.4 juta SGD, toleransi rounding; jika tidak cocok, **jangan publikasikan** angka sektoral.
4. Jika tidak bisa mengunduh langsung di percakapan ini, script `fetch_official_singstat_2b.py` dapat dijalankan secara manual di laptop atau Hermes. Script hanya menggunakan API resmi; **bukan scraping halaman atau login berbayar**.

## Quality gates

- Pastikan denominasi **SGD juta**, angka stok **31 Desember**, bukan realisasi PMA/flows.
- 2025 belum tersedia pada seri SingStat posisi investasi yang diperiksa; jangan interpolasi.
- DataSeries dengan kategori berjenjang dapat menyebabkan double-count: subtotal vs industri, sumber mata modal vs penerima di Indonesia.
- Perubahan klasifikasi SSIC 2025 perlu diperiksa jika membandingkan klasifikasi tahunan 2003–2024.
- Waktu pengambilan, URL, file SHA-256 wajib disimpan.
- Sumber tabel: https://data.gov.sg/datasets/d_dea084e8924680c954f1569a27f6d96c/view dan https://data.gov.sg/datasets/d_3dcfd9108ee04bd2b7978d6eaab1ed9a/view

## Integrasi HTML

- `stage2b_fdi_exposure_shares_1994_2024.json`: siap dipakai langsung untuk grafik.
- `stage2b_preview.html`: offline, data tersemat agar bisa dibuka tanpa server.
- `stage2b_source_registry.csv`: daftar sumber dan status audit.
