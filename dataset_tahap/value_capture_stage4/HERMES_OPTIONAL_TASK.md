# HERMES TASK — JANGAN JALANKAN SEBELUM TARGET PERUSAHAAN DISETUJUI

Tujuan: gunakan hanya untuk pengumpulan massal laporan tahunan / laporan keuangan publik jika manual tidak efisien. Jangan scraping BI/SingStat bila tabel resmi dapat diunduh dari API atau halaman resminya.

1. Input: daftar URL perusahaan, daftar situs laporan tahunan resmi, periode 2003–2025.
2. Unduh laporan resmi sesuai Terms of Service, robots.txt, rate limit, tanpa melewati login/CAPTCHA/pembatasan akses.
3. Hasil `downloads_manifest.csv`: issuer, legal_entity_name, report_year, document_type, source_url, download_date, local_path, sha256, page_count, extraction_status.
4. Hasil `corporate_income_events.csv`: subsidiary, parent, ownership_pct, accounting_period, transaction_type (declared_dividend/paid_dividend/reinvested_earnings/intercompany_interest/profit), value, currency, original_text, PDF_page, source_document_id, confidence_flag.
5. Jangan menghitung tahun tanpa disclosure; data hilang = kosong. Jangan mengasumsikan laba konsolidasi sepenuhnya dari Indonesia.
6. Semua extraction harus menyimpan kutipan 1–2 kalimat kontekstual dan halaman sumber untuk pemeriksaan manusia.
7. Output CSV/JSON dan arsip file sumber. Import ke ChatGPT untuk validasi dan atribusi akhir.
