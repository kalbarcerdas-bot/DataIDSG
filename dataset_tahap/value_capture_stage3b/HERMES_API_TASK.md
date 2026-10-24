# Task untuk Hermes (HANYA jika diperlukan)

**Penting:** ini adalah *pengambilan data publik melalui API resmi*, bukan scraping halaman JS. Gunakan standard Python `urllib` atau `requests` lebih dahulu. Scrapling tidak diperlukan kecuali semua API resmi dan unduhan gagal serta syarat situs mengizinkan crawling. Jangan meminta autentikasi, bypass anti-bot, atau menghindari pembatasan akses.

## Sasaran

Unduh dataset lengkap berikut tanpa menyaring baris ketika mengambil arsip mentah:

1. https://data.gov.sg/datasets/d_bff5c93e3d5a7153df64a968afcc7d5b/view — M060261, ekspor jasa menurut negara + kategori.
2. https://data.gov.sg/datasets/d_addeac819bfa848fdcc255dd6637484c/view — M060271, impor jasa menurut negara + kategori.

Masing-masing versi yang diperiksa terdiri dari **286 baris**, periode 2000–2024. Gunakan API publik data.gov.sg (mis. `api-production.data.gov.sg/v2/public/api/datasets/{dataset_id}/list-rows` dengan pagination, atau mekanisme initiate-download / poll-download di `api-open.data.gov.sg`). Ikuti aturan rate limit platform. Jangan berasumsi halaman Data Explorer hanya menampilkan 10 baris sebagai keseluruhan tabel.

## Keluaran wajib

- `exports_category.csv`: **semua baris** M060261, `DataSeries`, dan setiap kolom tahun dari penerbit.
- `imports_category.csv`: **semua baris** M060271, kolom yang sama.
- `manifest.json`: URL tepat, ID dataset, waktu (Asia/Jakarta), jumlah baris, nama kolom, unit, SHA256, metode unduhan, status sukses.
- Jangan mengestimasi nilai yang tidak ada, jangan menghapus hierarchy seperti `Indonesia` diikuti subbaris jenis layanan, jangan mengubah `na` menjadi 0.

## Perintah validasi

Pastikan satu baris judul `Indonesia` tersedia di **masing-masing** dataset dan bagian berikutnya memuat kategori yang sesuai. JANGAN menggabungkan nilai dari `Asia` atau `ASEAN` untuk mengisi Indonesia. Data ini harus dapat direkonsiliasi ke S$7.857,7 juta ekspor dan S$4.268,7 juta impor (2024) dalam sumber total Tahap 3A. Jika tidak cocok, laporkan perbedaan tanpa merekayasa angka.

## Untuk pengguna

Setelah Hermes selesai, ambil dua CSV saja, unggah kembali ke chat ChatGPT ini. Alternatifnya, jalankan file `build_stage3b.py` pada komputer dengan internet:

```bash
python build_stage3b.py --download
```

Atau setelah dua file diunduh:

```bash
python build_stage3b.py --exports exports_category.csv --imports imports_category.csv
```

Program mengekstrak angka Indonesia, menghitung saldo, menguji rekonsiliasi, dan membuat CSV, JSON, HTML otomatis. Jika struktur sumber berubah, berhenti untuk memeriksa blok kategori, bukan melakukan pencocokan angka sembarangan.
