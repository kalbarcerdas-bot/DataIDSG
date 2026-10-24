# Menyimpan riset di GitHub

## Pilihan disarankan: buat repository **private** baru

Nama disarankan: `kalcer-indonesia-singapura-research`. Hindari memasukkan seluruh riset ke repository website `kalcerpost` atau `KalcerBranding101` tanpa pemisahan editorial dan peninjauan data.

1. Buat repository kosong di GitHub; pilih **Private**. Jangan centang inisialisasi README karena folder ini sudah memilikinya.
2. Ekstrak ZIP GitHub-ready, lalu buka terminal pada folder hasil ekstraksi.
3. Jalankan:

```bash
git init
git branch -M main
git add .
git commit -m "Add Kalcer Indonesia-Singapura research repository"
git remote add origin https://github.com/USERNAME/kalcer-indonesia-singapura-research.git
git push -u origin main
```

4. Jalankan pengecekan: `python scripts/validate.py`.
5. Setelah kurasi dan keputusan publikasi, gunakan `docs/` sebagai sumber GitHub Pages pada repository yang memenuhi syarat atau deploy `docs/` ke hosting statis. **Jangan langsung menjadikan seluruh folder `research/` sebagai publik**; terdapat proksi, kajian sementara, dan lisensi sumber pihak ketiga yang harus diperiksa.

## Memperbarui data

Simpan dataset revisi versi baru, perbarui `catalog/claims.csv` dan `docs/data/*.json`, periksa ulang status bukti, lalu jalankan validasi. Hindari mengubah angka historis tanpa jejak versi / perubahan metodologi.

## Unduhan dan API

Website `docs/index.html` memuat metadata `docs/data/catalog.json`, `docs/data/metrics.json`, dan `docs/data/bayan_timeseries.json`. Endpoint ini adalah JSON statis, bukan server API. `docs/downloads/` berisi 13 CSV siap unduh dengan catatan keterbatasan di katalog.

## Hak cipta

Sumber primer eksternal ditautkan, bukan otomatis berlisensi terbuka. Jangan mengasumsikan semua penelitian, kutipan, tabel, atau data pihak ketiga boleh didistribusikan ulang. Baca `PUBLICATION_POLICY.md`.
