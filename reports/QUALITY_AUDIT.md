# Audit Kualitas — KALCER Indonesia–Singapura

**Snapshot:** 24 Oktober 2026. **Sumber:** arsip penelitian dari Tahap 1–8 dan Riset Tambahan 1–8.

## Hasil pengepakan

- Arsip awal: **164 berkas**; semua disalin tanpa perubahan byte ke `research/`.
- Structured CSV: **103**; sumber metadata terindeks: **224 entri**. Beberapa URL digunakan berulang antar-penelitian.
- Gap/pertanyaan riset: **144 baris**; tidak selalu merupakan gap unik.
- Status klaim: ESTIMATE: 2, ILLUSTRATION: 1, PLEDGE: 1, RECONSTRUCTION: 2, REGULATORY_ACTION: 1, REPORTED: 3, REPORTED_AND_REGISTRY: 1, REPORTED_SERIES: 1, SCENARIO: 1, UNPROVEN: 2, UNSUPPORTED: 1.
- Unduhan data publik: **13**. Ini masih dataset *research-grade* dengan caveat, bukan jaminan semua observasi final.

## Dua lapisan publikasi

**Internal / research:** seluruh bahan riset dan dokumen pendukung di `research/` beserta registri sumber, tabel tentatif, dan status verifikasi.

**Eksternal / website:** 13 file CSV di `public-data/` dan mirror `docs/downloads/`. Metadata per file mencatat keterbatasan; wajib ada pemeriksaan editorial untuk masing-masing kutipan.

## Red flags interpretasi

1. Beberapa nilai sebelum 2011 masih bersumber sekunder; beberapa periode menunjukkan restatement. Jangan memberi label `audit-grade` pada jumlah historis itu.
2. Angka hak dividen penerima tertentu menggunakan kepemilikan dari tanggal snapshot terdekat, bukan selalu `record date` dividen. Jangan menyebutnya transfer kas.
3. Sekuritas yang dihibahkan kepada WNA adalah transfer hak ekonomi saham, bukan bukti bahwa aset operasi tambang keluar dari Indonesia.
4. Total yayasan, donasi NUS, CSR, dan PPM dapat mengandung cakupan yang saling tumpang tindih; jangan jumlahkan lintas kategori tanpa ledger rekonsiliasi.
5. Biaya Sekolah Garuda mengandung skenario yang tidak bersumber dari RAB final pemerintah; bedakan pembangunan fisik dan total cost of ownership.
6. Ketersediaan SMP dalam suatu desa tidak berarti warga desa lain tidak dapat bersekolah.
7. Kepemilikan saham entitas Singapura tidak otomatis berarti pemilik manfaat akhir warga Singapura.
8. Tidak tersedia bukti representatif untuk menyebut IQ warga Kalimantan paling rendah atau menyetarakan dengan simpanse.
9. Tindakan permintaan dokumen karhutla bukan bukti keterlibatan pelanggaran.
10. Hubungan perusahaan terkait dan pinjaman belum cukup untuk membuktikan aliran langsung dividen BYAN ke investasi lainnya.

## Pengujian

- SHA-256 snapshot original dan jumlah baris CSV: `scripts/validate.py`.
- Copy publik identik pada `public-data/` dan `docs/downloads`.
- Website menggunakan JSON statis; tidak mengakses aplikasi eksternal.
- Pipeline bersifat *read-only* terhadap data yang sudah dikumpulkan: pada saat pengemasan **tidak ada verifikasi web tambahan** atas seluruh sumber asli.

## Rekomendasi perubahan versi

Lakukan update melalui branch/PR, beri ID klaim yang terdampak, tambah tautan dokumen primer dan tanggal pemeriksaan. Jangan mengedit file original tanpa menyimpan versi baru dan menjelaskan alasan perubahan.
