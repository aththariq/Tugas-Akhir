# Audit Diksi dan Ejaan Rawan

Laporan ini dibuat otomatis dari sumber `.tex`. Setiap temuan adalah kandidat yang perlu dicek manual, bukan vonis final.

Total temuan pola rawan: 17
Total kandidat spellcheck Aspell: 0

Catatan spellcheck: Spellcheck Aspell tidak diaktifkan. Jalankan dengan --spellcheck untuk audit kamus penuh.

## Pola Rawan


### Bab II - Studi.tex

- Baris 27: `metadata` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: yang sering tidak memiliki struktur metadata lengkap untuk ditelusuri kembali

### Bab III - Analisis.tex

- Baris 93: `metadata` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: individual dan tidak memiliki dasar metadata yang memadai untuk dipertahankan

### Bab IV - Perancangan.tex

- Baris 96: `metadata` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: Pencatatan Aktivitas & Aktivitas penting memiliki konteks waktu, sumber, dan hubungan ke kontainer agar dapat ditelusuri ulang. & Model audit, riwayat kontainer, dan metadata inspeksi. \\
- Baris 529: `edge` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \node[action] (edge) at (3.1,-0.95) {Akuisisi \textit{frame}\\dan inferensi awal};
- Baris 542: `edge` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \draw[flow] (camera) -- (edge);
- Baris 543: `edge` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \draw[flow] (edge) -- (ocr);
- Baris 544: `edge` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \draw[videoflow] (edge.east) -- ++(0.65,0) \|- node[pos=0.72, above, fill=white, inner sep=1pt] {video beranotasi} (live.west);
- Baris 722: `edge` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \node[block] (edge) at (-5.40,1.35) {Cargovision\\\textit{Edge}};
- Baris 726: `interface` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \node[block, minimum width=3.35cm] (interface) at (3.30,0) {\textit{Integration Interface}\\Kontrak dan Validasi Pesan};
- Baris 734: `edge` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \draw[line] (edge.east) -- (core.160);
- Baris 737: `interface` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \draw[target] (core.east) -- (interface.west);
- Baris 739: `interface` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \draw[trunk] (interface.east) -- (split);
- Baris 897: `edge` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \node[comp] (edge) at (-6.40,0.00) {Cargovision \textit{Edge}\\OCR dan pemindaian awal};
- Baris 908: `edge` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \draw[line] (camera.south) -- (edge.north);
- Baris 909: `edge` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \draw[line] (edge.south) -- (localBuffer.north);
- Baris 910: `edge` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \draw[line] (edge.east) -- (http.west);
- Baris 913: `edge` - Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.
  Cuplikan: \draw[videoline] (edge.south east) -- (wsEntry) -- (ws.west);

## Kandidat Spellcheck Aspell

Tidak ada kandidat tambahan dari spellcheck Aspell.
