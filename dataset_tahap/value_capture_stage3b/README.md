# Indonesia–Singapura Value Capture: Tahap 3B

Paket ini dibuat langsung di ChatGPT. Semua sumber data dirujuk ke statistik publik SingStat. **Tahap 3B belum berisi angka jasa per kategori Indonesia yang telah lolos verifikasi**; jangan menyebut angka nasional/Asia sebagai angka bilateral.

## Cara menggunakan

1. Buka `outputs/stage3b_preview.html` untuk membaca baseline interaktif dari Tahap 3A. Tidak memerlukan server/internet untuk memuat angka di dashboard.
2. Untuk memperoleh data kategori, coba `python build_stage3b.py --download` pada komputer dengan akses internet. Menggunakan API publik, tanpa login dan tanpa library tambahan.
3. Jika mengunduh CSV melalui browser, simpan dengan nama `inputs/exports_category.csv` dan `inputs/imports_category.csv`, lalu jalankan `python build_stage3b.py --offline`.
4. File JSON/CSV/HTML otomatis diperbarui ke `outputs/`. Baca `outputs/stage3b_reconciliation_2003_2025.csv` sebelum menerbitkan peringkat sektor.
5. Jika unduhan publik dari ChatGPT tidak tersedia, lihat `HERMES_API_TASK.md` untuk tugas Hermes. Ini **bukan** instruksi scraping agresif.

## Standar kualitas

Kategori = 12 jenis jasa resmi SingStat. Semua nilai uang adalah SGD juta dan bersumber dari seri negara mitra **Indonesia**. Nilai `na` tetap null. Tahun 2025 bilateral tetap kosong. Saldo jasa merupakan *balance of trade in services*, bukan keuntungan ekonomi bersih. Jika perbedaan dengan total > S$1,5 juta, data ditandai gagal rekonsiliasi.

## Petunjuk penggabungan website

HTML ini adalah prototype mandiri. Website final dapat membaca `outputs/stage3b_dashboard_data.json` dan `outputs/stage3b_services_category_long_2003_2025.csv`. Gaya menggunakan palet editorial navy/teal, bukan merek perusahaan. Status pengambilan data tercatat di `outputs/stage3b_status.json`.
