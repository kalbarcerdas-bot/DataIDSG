# Kalcer Research — Kekayaan Indonesia, Value Capture Singapura

**Data repository | snapshot 24 Oktober 2026 | Bahasa Indonesia**

Repositori riset independen untuk artikel, unduhan CSV, visualisasi, dan audit jejak nilai ekonomi dari Indonesia ke pihak-pihak yang memiliki hubungan dengan Singapura. Menyatukan data perdagangan, FDI, jasa, nilai tambah, perusahaan, kepemilikan, Bayan Resources, filantropi, pendidikan di sekitar tambang, simulasi Sekolah Garuda, dan perbandingan antarkonglomerat.

> **Kunci interpretasi:** ekspor bruto ≠ laba; FDI stock ≠ uang masuk baru; saham hibah ≠ transfer kas ke luar negeri; perusahaan berbasis Singapura ≠ seluruh laba milik warga Singapura; donasi ke kampus Singapura ≠ seluruh penerima manfaat warga Singapura.

## Mulai di sini

| Kebutuhan | Lokasi |
|---|---|
| Data mentah/hasil riset lengkap | `research/` (164 file arsip sumber riset; dipertahankan byte-for-byte) |
| Indeks semua dataset & hash | `catalog/datasets.csv` |
| Sumber dan URL yang dilaporkan | `catalog/sources.csv` |
| Klaim, status bukti, caveat | `catalog/claims.csv` |
| Semua pertanyaan data yang belum lengkap | `catalog/research_gaps.csv` |
| CSV pilihan untuk diunduh | `public-data/` (13 dataset, dengan caveat) |
| Website katalog tanpa backend | `docs/index.html` — cocok untuk GitHub Pages / hosting statis |
| Draft dan peta artikel | `content/articles/` |
| Outline 20 slide Kalcer | `content/carousel/20_slide_research_map.md` |
| Validasi arsip | `python scripts/validate.py` |
| Petunjuk GitHub | `GITHUB_SETUP.md` |
| Arsip turunan original pra-restukturisasi | `archive/` |

## Struktur data & audit

- **S1–S8:** perdagangan, investasi, jasa, pendapatan investasi, komoditas, perusahaan SGX, UBO, dan OECD TiVA. Beberapa tabel merupakan template / status `MISSING` dan bukan angka observasi aktual.
- **S9.1:** rekonstruksi produksi, pendapatan, cadangan Bayan 2008–2026 H1.
- **S9.2:** dividen, event, snapshot dan estimasi hak pemegang saham.
- **S9.3:** hibah dan transaksi saham 2024–2026.
- **S9.4:** jaringan entitas Low Singapura, transaksi dan fasilitas pinjaman.
- **S9.5:** donasi pribadi/yayasan dan CSR/PPM; tidak dijumlahkan tanpa eliminasi.
- **S9.6:** pendidikan dan persebaran sekolah di Tabang/Kutai Kartanegara.
- **S9.7:** simulasi anggaran Sekolah Garuda, bukan RAB final.
- **S9.8:** perusahaan sawit/batu bara, dividen lintas kepemilikan, karhutla sebagai jalur audit terpisah.

## Penggunaan

Jalankan `python scripts/validate.py`. Untuk eksplorasi gunakan CSV dengan Python, R, Excel, atau DuckDB. File `.xlsx` penelitian sebelumnya disimpan tanpa diubah. Dataset publik ada pada `docs/downloads/`, sama persis dengan `public-data/`.

**Catatan verifikasi:** sumber dan perhitungan ini merupakan arsip penelitian sebelumnya, bukan pengganti pemeriksaan dokumen primer sebelum publikasi. Tahun parsial jangan dibandingkan langsung dengan tahun penuh; angka 2026 sebagian adalah semester I.
