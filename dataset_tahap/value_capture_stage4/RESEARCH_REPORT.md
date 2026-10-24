# TAHAP 4 — Investment Income Accounting / Pendapatan Investasi Indonesia–Singapura

Tanggal kajian: 24 Oktober 2026. Penelitian menggunakan sumber publik, tanpa akun berbayar.

## HASIL YANG TELAH DIAMBIL

- **11 tahun (2015–2025)** angka resmi **pembayaran pendapatan investasi langsung Indonesia kepada seluruh investor asing** (juta USD), diuraikan menjadi pendapatan ekuitas serta bunga instrumen utang antarpihak terkait.
- **23 baris (2003–2025)** dalam dataset panel; 2003–2014 masih kosong untuk agregat global agar tidak mengarang angka. Ini BUKAN indikasi nilainya nol.
- **23 tahun data khusus Singapura untuk pendapatan investasi tetap kosong**, karena seri bilateral yang cocok belum berhasil ditemukan/ diverifikasi dalam sumber publik yang sudah dicek.
- Seri **stok FDI Singapura ke Indonesia (SGD)** disertakan sebagai konteks terpisah dari Tahap 2; angka stok bukan laba dan tidak dijumlahkan dengan arus pendapatan (USD).

## TEMUAN TERPILIH (SELURUH NEGARA INVESTOR, BUKAN SINGAPURA)

| Tahun | Ekuitas (juta USD) | Bunga (juta USD) | Total pembayaran (juta USD) | Sumber |
|---|---:|---:|---:|---|
| 2015 | 17,153 | 1,440 | 18,593 | BI_2016 |
| 2016 | 16,687 | 1,101 | 17,788 | BI_2016 |
| 2017 | 20,815 | 971 | 21,786 | BI_2019 |
| 2018 | 21,316 | 1,176 | 22,492 | BI_2019 |
| 2019 | 20,841 | 849 | 21,690 | BI_2019 |
| 2020 | 16,219 | 656 | 16,875 | BI_2022 |
| 2021 | 20,543 | 522 | 21,065 | BI_2022 |
| 2022 | 24,458 | 536 | 24,994 | BI_2024 |
| 2023 | 24,066 | 614 | 24,680 | BI_2026 |
| 2024 | 24,327 | 727 | 25,054 | BI_2026 |
| 2025 | 25,114 | 584 | 25,698 | BI_2026 |

## KAIDAH INTERPRETASI

1. 'Pembayaran' pada akun pendapatan investasi neraca pembayaran **tidak otomatis berarti transfer kas**; mencakup laba ditahan yang dicatat sebagai pendapatan terutang dan reinvestasi.
2. 'Pendapatan modal ekuitas' BI adalah kategori **laba investasi atas ekuitas**, BUKAN angka dividen tunai yang terisolasi. Jangan diberi label dividen.
3. 'Pendapatan utang (bunga)' adalah komponen yang berbeda dengan jasa keuangan (Tahap 3) dan berbeda dengan pinjaman pokok yang masuk akun finansial.
4. Total kepada semua investor asing tidak boleh dianggap sebagai pendapatan investor Singapura atau dikalikan proporsi stok investasi Singapura tanpa model dengan asumsi dan rentang ketidakpastian.
5. Persentase yield = income/global stock SG *tidak valid* bila pembilang seluruh investor asing, bukan Singapura. Perubahan stok bukan net investment income.
6. Sumber publik beberapa tahun memiliki status sementara atau telah direvisi; `publication_vintage` disimpan sehingga pembacaan historis transparan.
7. Rounding sekitar US$1 juta diperbolehkan pada rekonsiliasi income credit - debit = saldo.

## SUMBER (HALAMAN PDF)
- **BI_2016:** Laporan NPI Triwulan IV 2016; https://www.bi.go.id/id/publikasi/laporan/Documents/Laporan-NPI-Tw%20-IV-2016-260417.pdf ; halaman tercetak 34, halaman PDF 40
- **BI_2019:** Laporan NPI Triwulan IV 2019; https://www.bi.go.id/id/publikasi/laporan/Documents/NPI_Tw.IV-2019.pdf ; halaman tercetak 36, halaman PDF 42
- **BI_2022:** Laporan NPI Triwulan IV 2022; https://www.bi.go.id/id/publikasi/laporan/Documents/NPI-Tw.IV_2022.pdf ; halaman tercetak 36, halaman PDF 42
- **BI_2024:** Laporan NPI Triwulan IV 2024; https://www.bi.go.id/id/publikasi/laporan/Documents/NPI_Tw-IV_2024.pdf ; halaman tercetak 34, halaman PDF 40
- **BI_2026:** Laporan NPI Triwulan I 2026; https://www.bi.go.id/id/publikasi/laporan/Documents/NPI_Tw-I_2026.pdf ; halaman tercetak 30, halaman PDF 36
- **SINGSTAT:** Singapore Direct Investment Abroad by Destination; https://data.gov.sg/datasets/d_a1db0947cc69ae27d0ffb6ddfaf6cdde/view

## PEMERIKSAAN DATA BILATERAL

- SingStat outward FDI menurut negara tujuan tersedia sebagai **stok**, bukan pendapatan keuntungan tiap negara.
- SingStat *Income of Foreign Direct Investment in Singapore by Source Economy* memiliki arah terbalik: pendapatan atas investasi asing di Singapura, sehingga DILARANG dipakai sebagai pendapatan Singapura dari Indonesia.
- ASEANstats FDI flows by source/destination mengukur **modal investasi**, bukan pendapatan investasi yang berasal dari modal tersebut.
- Statistik pendapatan investasi yang dipublikasi BI menguraikan agregat semua negara; tidak ada pemisahan bilateral pada Tabel 4 yang diverifikasi.
- OECD 'FDI income receipts by partner country' adalah definisi indikator yang sesuai, tetapi tabel indikator publiknya memiliki cakupan terbatas. Belum ditemukan angka SG-ID yang dapat diekstraksi langsung; ini menjadi *research lead*, bukan observasi.

## KELANJUTAN RISET

A. Periksa apakah terdapat tabel OECD/BMD4 untuk pasangan Singapura–Indonesia dengan tahun terukur; simpan definisi immediate investor.
B. Telusuri laporan tahunan anak perusahaan Indonesia dan holding Singapura; simpan laba setelah pajak, laba ditahan, dividen diumumkan/dibayar, bunga pihak berelasi, kepemilikan, dan catatan pajak menurut tahun.
C. Pisahkan *cash dividend* dari reinvested earnings dan pastikan hubungan parent-subsidiary, negara tempat usaha, dan ultimate beneficiary.
D. Jika ekstraksi 100+ PDF diperlukan, sediakan tugas Hermes+Scrapling hanya untuk unduh halaman terbuka dan dokumen laporan resmi (taati ketentuan akses situs, tanpa bypass).

**Catatan akhir:** Belum ada nilai pendapatan investasi Singapura dari Indonesia yang bisa diterbitkan sebagai 'value capture' tahunan spesifik Singapura pada Tahap 4 ini.
