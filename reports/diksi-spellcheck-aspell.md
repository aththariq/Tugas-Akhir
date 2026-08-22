# Audit Diksi dan Ejaan Rawan

Laporan ini dibuat otomatis dari sumber `.tex`. Setiap temuan adalah kandidat yang perlu dicek manual, bukan vonis final.

Total temuan pola rawan: 0
Total kandidat spellcheck Aspell: 429

## Pola Rawan

Tidak ada temuan dari daftar pola yang diperiksa.

## Kandidat Spellcheck Aspell

Bagian ini memakai kamus `aspell-id` dan allowlist teknis lokal. Kandidat nama diri atau istilah teknis dapat ditambahkan ke allowlist.

- `algoritma` - muncul 3 kali
  Contoh: 11 Daftar Algoritma.tex:6: \addcontentsline{toc}{chapter}{DAFTAR ALGORITMA}
  Contoh: 4 Pernyataan Penggunaan AI.tex:28: 8 & Penyusunan konsep desain atau algoritma & ChatGPT & Rendah & Penyusunan alternatif struktur penjelasan \\
  Contoh: Bab I - Pendahuluan.tex:132: arsitektur data, bukan pada implementasi detail algoritma deteksi, strategi

- `analitik` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:161: & Sistem menyajikan akses terstruktur untuk pelaporan dan analitik & Sedang \\
  Contoh: Bab III - Analisis.tex:332: analitik proses. Selain itu, pihak eksternal dapat berlangganan \textit{event}
  Contoh: Bab III - Analisis.tex:376: yang baik dengan sistem pelaporan dan analitik agar manfaat \textit{data

- `antaraktor` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:72: Ketiadaan \textit{metadata} dan mekanisme ketertelusuran membuat data inspeksi sulit dimanfaatkan untuk analisis tren ataupun audit kepatuhan. Model interaksi antaraktor dan titik masalah utama pada sistem manual diringkas pada Gambar~\ref{fig:model_konseptual_saat_ini}.
  Contoh: Bab III - Analisis.tex:342: \textit{event} dapat menimbulkan perbedaan status antaraktor, sehingga
  Contoh: Bab III - Analisis.tex:366: tanggung jawab antaraktor menjadi lebih jelas melalui kepemilikan data,

- `antardomain` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:290: terdefinisi dan kontrak antardomain yang terdokumentasi.
  Contoh: Bab III - Analisis.tex:304: Keterbatasannya terletak pada kebutuhan tata kelola antardomain yang konsisten.
  Contoh: Bab III - Analisis.tex:463: \textit{interoperability}, kontrak antardomain dapat dirancang sebagai

- `antarpemangku` - muncul 3 kali
  Contoh: 5 Abstrak.tex:17: di antaranya fragmentasi informasi antarpemangku kepentingan, pencatatan hasil
  Contoh: Bab II - Studi.tex:292: pertukaran data elektronik antarpemangku kepentingan melalui platform
  Contoh: Bab III - Analisis.tex:56: antarpemangku kepentingan tanpa mekanisme pelacakan formal.

- `antarpetugas` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:154: & Sistem menjaga konsistensi interpretasi hasil antarpetugas & Tinggi \\
  Contoh: Bab III - Analisis.tex:397: Keselarasan Proses & Kemampuan untuk menyediakan standardisasi proses inspeksi dan konsistensi hasil antarpetugas serta antarlokasi. \\
  Contoh: Bab IV - Perancangan.tex:81: Petugas inspeksi melakukan pemeriksaan visual berdasarkan panduan inspeksi standar. Namun, penerapan panduan ini sangat bergantung pada interpretasi subjektif setiap petugas, menghasilkan variabilitas tinggi dalam hasil inspeksi. Tidak ada mekanisme validasi konsistensi antarpetugas.

- `arsitektural` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:162: menyeluruh, melainkan untuk menjelaskan bagaimana keputusan arsitektural
  Contoh: Bab III - Analisis.tex:12: Analisis sistem saat ini dilakukan untuk mengidentifikasi keterbatasan mendasar yang menjadi akar permasalahan arsitektural, sehingga kebutuhan sistem yang dirumuskan kemudian benar-benar merespons celah yang teridentifikasi.
  Contoh: Bab III - Analisis.tex:83: Analisis terhadap model konseptual sistem saat ini menghasilkan identifikasi tiga kategori masalah arsitektural. Kategorisasi ini disusun berdasarkan pengelompokan tematik terhadap keterbatasan yang teridentifikasi pada dimensi \textit{people}, \textit{process}, \textit{technology}, dan \textit{data}. Setiap kategori masalah mencerminkan celah arsitektural yang menghambat pencapaian standardisasi, integrasi, dan keandalan operasional.

- `aththariq` - muncul 3 kali
  Contoh: 1 Halaman Judul.tex:18: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 2 Lembar Pengesahan.tex:19: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 5 Abstrak.tex:10: Aththariq Lisan Quran Daulah Sentono\\

- `berfokus` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:131: \item Tugas akhir ini berfokus pada perancangan arsitektur sistem dan
  Contoh: Bab IV - Perancangan.tex:126: integrasi masih berfokus pada alur internal proyek, sedangkan sinkronisasi ke
  Contoh: Bab IV - Perancangan.tex:210: integrasi aktual masih berfokus pada interaksi internal antara komponen

- `berinteraksi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:197: Arsitektur berbasis kejadian merupakan pola desain yang membuat komponen sistem berinteraksi melalui notifikasi perubahan status, memungkinkan independensi temporal dan fungsional antara komponen \autocite{hohpe2003}. Dalam pendekatan ini, komponen yang menghasilkan informasi tidak perlu mengetahui komponen mana yang akan merespons informasi tersebut, dan sebaliknya. Konsep ini menciptakan sistem yang lebih fleksibel karena komponen baru dapat ditambahkan untuk merespons kejadian yang sudah ada tanpa mengubah komponen penghasil kejadian. Pendekatan berbasis kejadian ini selaras dengan kebutuhan inspeksi kargo yang memerlukan penelusuran perubahan status kontainer sepanjang alur pemeriksaan secara transparan.
  Contoh: Bab III - Analisis.tex:26: mengelola alur kontainer di area pelabuhan dan berinteraksi dengan
  Contoh: Bab III - Analisis.tex:191: & Sistem berinteraksi dengan berbagai sistem pelabuhan (TOS, PCS, Inaportnet) tanpa modifikasi signifikan pada sistem eksternal. \textit{Interface} integrasi mengikuti standar industri logistik. \\

- `berisiko` - muncul 3 kali
  Contoh: Bab II - Studi.tex:53: berisiko sedang sehingga proses dapat dipercepat tanpa pembongkaran fisik.
  Contoh: Bab II - Studi.tex:56: berisiko tinggi, \textit{physical inspection} tetap diperlukan sebagai validasi
  Contoh: Bab III - Analisis.tex:276: perubahan yang terstruktur, lapisan orkestrasi justru berisiko menjadi hambatan

- `berkomunikasi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:210: memungkinkan komponen heterogen untuk berkomunikasi secara efektif
  Contoh: Bab III - Analisis.tex:255: berkomunikasi melalui kontrak pertukaran informasi standar. Alur informasi
  Contoh: Bab VI - Evaluasi.tex:21: penyimpanan dapat berkomunikasi sesuai dengan rancangan arsitektur. Kedua,

- `black` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:179: box/.style={rectangle, rounded corners, draw=black, align=center, minimum width=0.78\textwidth, minimum height=0.95cm},
  Contoh: TA.tex:149: linkcolor=black,
  Contoh: TA.tex:150: citecolor=black,

- `bottom` - muncul 3 kali
  Contoh: TA.tex:222: bottom=3cm
  Contoh: TA.tex:287: capposition=bottom
  Contoh: TA.tex:354: bottom=3cm

- `capposition` - muncul 3 kali
  Contoh: TA.tex:287: capposition=bottom
  Contoh: TA.tex:295: capposition=top,
  Contoh: TA.tex:307: capposition=top

- `chapter` - muncul 3 kali
  Contoh: 10 Daftar Persamaan.tex:6: \addcontentsline{toc}{chapter}{DAFTAR PERSAMAAN}
  Contoh: 11 Daftar Algoritma.tex:6: \addcontentsline{toc}{chapter}{DAFTAR ALGORITMA}
  Contoh: 12 Daftar Listing.tex:4: \addcontentsline{toc}{chapter}{DAFTAR \textit{LISTING}}

- `chatgpt` - muncul 3 kali
  Contoh: 4 Pernyataan Penggunaan AI.tex:14: 1 & Pemeriksaan ejaan dan tata bahasa & ChatGPT & Rendah & Semua bab \\
  Contoh: 4 Pernyataan Penggunaan AI.tex:16: 2 & Pembuatan teks & ChatGPT & Rendah & Bab I--Bab VII \\
  Contoh: 4 Pernyataan Penggunaan AI.tex:20: 4 & Pencarian informasi atau referensi & ChatGPT & Rendah & Studi literatur dan perumusan draf \\

- `cobit` - muncul 3 kali
  Contoh: Bab II - Studi.tex:229: COBIT (Control Objectives for Information and Related Technologies) merupakan kerangka kerja tata kelola dan manajemen teknologi informasi yang dikembangkan oleh ISACA \autocite{isaca2019}. COBIT 2019 menyediakan prinsip-prinsip untuk menyelaraskan TI dengan tujuan bisnis organisasi dan memastikan penggunaan teknologi yang efektif dan bertanggung jawab.
  Contoh: Bab II - Studi.tex:229: COBIT (Control Objectives for Information and Related Technologies) merupakan kerangka kerja tata kelola dan manajemen teknologi informasi yang dikembangkan oleh ISACA \autocite{isaca2019}. COBIT 2019 menyediakan prinsip-prinsip untuk menyelaraskan TI dengan tujuan bisnis organisasi dan memastikan penggunaan teknologi yang efektif dan bertanggung jawab.
  Contoh: Bab II - Studi.tex:231: Prinsip dasar COBIT menekankan bahwa sistem harus dirancang untuk memenuhi

- `container` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.

- `ctpat` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab III - Analisis.tex:40: berdasarkan \textit{checklist} standar seperti CTPAT \textit{Seven Point

- `customs` - muncul 3 kali
  Contoh: Bab II - Studi.tex:15: Inspeksi kargo merupakan elemen krusial dalam rantai logistik global yang menjamin keamanan, kepatuhan regulasi, dan integritas barang dalam perdagangan internasional. Menurut World Customs Organization (WCO), inspeksi kargo yang efektif mencegah penyalahgunaan perdagangan, melindungi keamanan publik, dan mendukung kelancaran alur barang di perbatasan \autocite{worldbank2023}. Dalam konteks Indonesia, proses inspeksi kontainer di pelabuhan masih menghadapi tantangan signifikan terkait efisiensi, akurasi, dan integrasi sistem \autocite{pwc2023, crifasia2023}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:23: World Customs Organization (WCO) mengklasifikasikan metode inspeksi kargo ke dalam beberapa kategori berdasarkan tingkat intrusivitas dan prinsip dasar teknologi yang digunakan \autocite{wco2020}. Klasifikasi ini penting untuk memahami dampak operasional, biaya, dan kelayakan pendekatan inspeksi dalam konteks pelabuhan.

- `daulah` - muncul 3 kali
  Contoh: 1 Halaman Judul.tex:18: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 2 Lembar Pengesahan.tex:19: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 5 Abstrak.tex:10: Aththariq Lisan Quran Daulah Sentono\\

- `depo` - muncul 3 kali
  Contoh: Lampiran-B.tex:14: Priok, yang dikunjungi pada tanggal 3 Februari 2026. Lokasi kedua adalah Depo
  Contoh: Lampiran-B.tex:153: pelabuhan dan depo peti kemas. Karena wawancara tidak direkam dalam bentuk
  Contoh: Lampiran-B.tex:201: \textbf{Lokasi} & Depo Peti Kemas Tanjung Priok PT Salam Pacific Indonesia Lines (SPIL) \\ \addlinespace

- `design` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:185: \node[box, below=of literature] (design) {Perancangan arsitektur sistem, arsitektur data, dan alur informasi};
  Contoh: Bab I - Pendahuluan.tex:192: \draw[line] (literature) -- (design);
  Contoh: Bab I - Pendahuluan.tex:193: \draw[line] (design) -- (demo);

- `diakses` - muncul 3 kali
  Contoh: Bab II - Studi.tex:262: dicatat, serta \textit{accessibility} agar jejak audit dapat diakses untuk
  Contoh: Bab III - Analisis.tex:98: informasi. Data inspeksi belum dapat diakses secara waktu nyata oleh sistem
  Contoh: Bab IV - Perancangan.tex:119: diakses oleh pemangku kepentingan yang berwenang. Notifikasi dikirimkan ketika

- `diaudit` - muncul 3 kali
  Contoh: Bab II - Studi.tex:48: yang terstruktur dan dapat diaudit. Tahap awalnya adalah \textit{targeting},
  Contoh: Bab II - Studi.tex:59: digital dan dokumentasi yang dapat diaudit.
  Contoh: Bab III - Analisis.tex:324: peristiwa yang dapat diaudit.

- `difokuskan` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:140: \item Evaluasi tugas akhir ini difokuskan pada kesesuaian rancangan arsitektur
  Contoh: Bab II - Studi.tex:104: Dalam tugas akhir ini, atribut kualitas yang digunakan difokuskan pada
  Contoh: Bab IV - Perancangan.tex:235: Realisasi aktual difokuskan pada pengolahan data inspeksi, integrasi internal,

- `diimplementasikan` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:380: yang diimplementasikan di lokasi inspeksi. Pada realisasi saat ini, sumber data
  Contoh: Bab IV - Perancangan.tex:503: seluruhnya telah diimplementasikan.
  Contoh: Bab IV - Perancangan.tex:633: Bab ini telah menyajikan desain arsitektur sistem inspeksi kargo digital terintegrasi yang dirancang untuk mengatasi permasalahan yang telah diidentifikasi di Bab III. Desain ini berfokus pada integrasi komponen, pemrosesan responsif, dan konsistensi alur data sebagai dasar realisasi sistem yang diimplementasikan.

- `diintegrasikan` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:513: siap diintegrasikan.
  Contoh: Bab IV - Perancangan.tex:123: Sistem dirancang agar siap diintegrasikan dengan sistem operasional eksternal
  Contoh: Bab VII - Penutup.tex:24: media penyimpanan dapat diintegrasikan sehingga membentuk alur data yang utuh,

- `diorganisasikan` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:253: lapisan orkestrasi. Komponen sistem diorganisasikan sebagai layanan tematik,
  Contoh: Bab III - Analisis.tex:353: jalur eskalasi yang terdokumentasi. Komponen sistem diorganisasikan mengikuti
  Contoh: Bab IV - Perancangan.tex:183: Sistem diorganisasikan dalam empat lapisan utama: (1) \textbf{\textit{Presentation Layer}} untuk interaksi pengguna melalui aplikasi web, (2) \textbf{\textit{Application Layer}} untuk logika bisnis, autentikasi, dan orkestrasi data melalui layanan API, (3) \textbf{\textit{Data Layer}} untuk penyimpanan data terstruktur dan artefak visual, dan (4) \textbf{\textit{Edge Layer}} untuk akuisisi aliran video, inferensi, dan pengiriman hasil inspeksi dari lapangan.

- `diposisikan` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:61: Kapabilitas di atas diturunkan dari analisis kebutuhan untuk mendukung \textbf{kemudahan pemeliharaan} melalui modularitas, \textbf{interoperabilitas} melalui kontrak layanan yang jelas, \textbf{auditabilitas} melalui ketertelusuran aktivitas, dan \textbf{keandalan operasi}. Pada realisasinya, kapabilitas tersebut diwujudkan melalui pemisahan komponen \textit{edge}, layanan API, aplikasi web, dan lapisan penyimpanan data, sedangkan interoperabilitas dengan sistem eksternal diposisikan sebagai kesiapan perluasan.
  Contoh: Bab IV - Perancangan.tex:127: sistem eksternal diposisikan sebagai arah pengembangan lanjutan. Dengan
  Contoh: Bab IV - Perancangan.tex:225: Sistem eksternal pada diagram diposisikan sebagai sasaran integrasi, bukan

- `direalisasikan` - muncul 3 kali
  Contoh: 6 Kata Pengantar.tex:20: direalisasikan dalam bentuk implementasi; pihak Terminal Pelindo Peti Kemas
  Contoh: Bab I - Pendahuluan.tex:101: mengevaluasi kesesuaian rancangan terhadap sistem yang direalisasikan.
  Contoh: Bab I - Pendahuluan.tex:123: direalisasikan pada proyek pengembangan sistem.

- `entitas` - muncul 3 kali
  Contoh: 13 Daftar Simbol.tex:16: \{id\} & Menunjukkan parameter identitas entitas pada jalur \textit{endpoint} layanan, misalnya identitas kontainer atau sumber daya tertentu. \\
  Contoh: 5 Abstrak.tex:33: pemantauan hasil inspeksi. Pada aspek data, entitas kontainer ditempatkan
  Contoh: 5 Abstrak.tex:40: entitas kontainer melalui OCR, propagasi nomor kontainer ke alur pemindaian

- `eskalasi` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:353: jalur eskalasi yang terdokumentasi. Komponen sistem diorganisasikan mengikuti
  Contoh: Bab IV - Perancangan.tex:711: Validator & Verifikasi hasil deteksi otomatis, penanganan kasus anomali, eskalasi keputusan & Pengetahuan kerusakan kontainer, prosedur penanganan \\
  Contoh: Bab IV - Perancangan.tex:729: sedangkan prosedur operasional mencakup SOP penggunaan sistem, eskalasi

- `evaluation` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:187: \node[box, below=of demo] (evaluation) {Evaluasi kesesuaian rancangan terhadap realisasi dan bukti integrasi};
  Contoh: Bab I - Pendahuluan.tex:194: \draw[line] (demo) -- (evaluation);
  Contoh: Bab I - Pendahuluan.tex:195: \draw[line] (evaluation) -- (communication);

- `false` - muncul 3 kali
  Contoh: TA.tex:241: breakatwhitespace=false,
  Contoh: TA.tex:247: showspaces=false,
  Contoh: TA.tex:248: showstringspaces=false,

- `fondasi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:19: Transformasi menuju pendekatan digital menuntut pemahaman yang mendalam terhadap teori inspeksi kargo, prinsip-prinsip arsitektur sistem, dan kerangka tata kelola yang dapat mendukung operasi yang konsisten, terukur, dan berkelanjutan. Literatur yang ada menyediakan fondasi teoretis yang kuat untuk merancang sistem yang tidak hanya efisien secara teknis tetapi juga sesuai dengan kebutuhan operasional dan regulasi pelabuhan.
  Contoh: Bab II - Studi.tex:98: Prinsip-prinsip ini membentuk fondasi untuk merancang sistem yang tidak hanya efektif secara fungsional tetapi juga dapat dipelihara, dikembangkan, dan diadaptasi sesuai dengan perubahan kebutuhan operasional.
  Contoh: Bab III - Analisis.tex:8: Bab ini menyajikan analisis mendalam terhadap sistem inspeksi kontainer yang ada saat ini, identifikasi kebutuhan sistem, eksplorasi alternatif solusi konseptual, dan justifikasi pemilihan solusi berdasarkan kriteria objektif. Analisis ini menjadi fondasi untuk perancangan arsitektur konseptual yang dipaparkan pada Bab IV.

- `holistik` - muncul 3 kali
  Contoh: Bab II - Studi.tex:234: kelola organisasi. COBIT juga menekankan pendekatan holistik terhadap faktor
  Contoh: Bab II - Studi.tex:334: \textbf{Celah 1: Kerangka Arsitektur Konseptual yang Komprehensif.} Meskipun literatur tentang teknologi inspeksi individual (NII, IRT, \textit{computer vision}) telah berkembang, belum ada kerangka arsitektur konseptual yang mengintegrasikan seluruh komponen dalam alur informasi yang holistik. Penelitian yang ada cenderung fokus pada aspek teknis spesifik tanpa memberikan \textit{blueprint} arsitektur yang dapat dijadikan acuan untuk implementasi sistem terintegrasi.
  Contoh: Bab III - Analisis.tex:16: Sistem inspeksi kontainer yang berlaku saat ini dapat dianalisis melalui kerangka \textit{People–Process–Technology–Data} untuk memahami komponen utama dan interaksinya. Kerangka ini memungkinkan identifikasi sistematis terhadap keterbatasan pada setiap dimensi, sehingga rancangan solusi dapat merespons seluruh aspek masalah secara holistik.

- `htbp` - muncul 3 kali
  Contoh: Bab II - Studi.tex:131: \begin{figure}[htbp]
  Contoh: Bab IV - Perancangan.tex:198: \begin{figure}[htbp]
  Contoh: Bab IV - Perancangan.tex:269: \begin{figure}[htbp]

- `http` - muncul 3 kali
  Contoh: 14 Daftar Singkatan.tex:17: HTTP & \textit{Hypertext Transfer Protocol} \\
  Contoh: Bab IV - Perancangan.tex:25: komunikasi diterapkan dengan menggunakan HTTP untuk data terstruktur dan
  Contoh: Bab IV - Perancangan.tex:287: dilakukan secara sinkron melalui HTTP untuk data terstruktur dan

- `iicl` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab II - Studi.tex:271: Institute of International Container Lessors (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC) menetapkan pedoman klasifikasi kerusakan dan dokumentasi yang menjadi dasar konsistensi penilaian kontainer \autocite{iicl2016, icswsc2023}. Standar ini mendefinisikan pola penilaian kerusakan yang konsisten, kategori kerusakan berdasarkan jenis dan tingkat keparahan, serta pentingnya dokumentasi yang mengikuti standar untuk keperluan audit dan klaim.

- `implementasinya` - muncul 3 kali
  Contoh: Bab V - Implementasi.tex:121: menyediakan data operasional kepada pengguna. Pada implementasinya, komponen
  Contoh: Bab V - Implementasi.tex:152: Pada implementasinya, aplikasi web membuka koneksi \textit{WebSocket} langsung ke
  Contoh: Bab V - Implementasi.tex:208: muatan yang tercatat. Pada implementasinya, data manifes diisikan melalui

- `inaportnet` - muncul 3 kali
  Contoh: Bab II - Studi.tex:342: \textbf{Celah 5: Kerangka Interoperabilitas untuk Ekosistem Pelabuhan Indonesia.} Meskipun prinsip interoperabilitas telah mapan secara teoretis, belum ada kerangka spesifik yang mendefinisikan standar antarmuka dan protokol komunikasi untuk integrasi sistem inspeksi dengan ekosistem digital pelabuhan Indonesia, termasuk Inaportnet, TOS, dan PCS.
  Contoh: Bab III - Analisis.tex:68: masih terisolasi dari sistem TOS, PCS, atau Inaportnet. Akibatnya, interpretasi
  Contoh: Bab III - Analisis.tex:191: & Sistem berinteraksi dengan berbagai sistem pelabuhan (TOS, PCS, Inaportnet) tanpa modifikasi signifikan pada sistem eksternal. \textit{Interface} integrasi mengikuti standar industri logistik. \\

- `independen` - muncul 3 kali
  Contoh: Bab II - Studi.tex:92: \textit{Modularity} mengarahkan sistem agar tersusun dari unit independen yang
  Contoh: Bab II - Studi.tex:151: independen ketika koneksi dengan pusat terganggu. \textit{Scalability}
  Contoh: Bab II - Studi.tex:163: terdekomposisi, \textit{loosely coupled}, dan dapat dikelola secara independen

- `informatika` - muncul 3 kali
  Contoh: 1 Halaman Judul.tex:35: {\large SEKOLAH TEKNIK ELEKTRO DAN INFORMATIKA}\\
  Contoh: 2 Lembar Pengesahan.tex:26: {\large Sekolah Teknik Elektro dan Informatika}\\
  Contoh: 6 Kata Pengantar.tex:9: Studi Sistem dan Teknologi Informasi, Sekolah Teknik Elektro dan Informatika,

- `inkonsistensi` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:46: Ketiadaan standar formal untuk penilaian kerusakan maupun dokumentasi digital yang terintegrasi dengan alur informasi pelabuhan mengakibatkan fragmentasi proses dan inkonsistensi keluaran. Setiap tahapan dilakukan secara manual tanpa dukungan sistem yang memvalidasi kelengkapan atau kebenaran data.
  Contoh: Bab III - Analisis.tex:100: dimasukkan ulang ke beberapa sistem, sehingga risiko kesalahan dan inkonsistensi
  Contoh: Bab III - Analisis.tex:298: penerapan kontrol akses dan menekan risiko inkonsistensi. Selain itu, strategi

- `inspection` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.

- `investigasi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:263: keperluan investigasi atau kepatuhan.
  Contoh: Bab IV - Perancangan.tex:96: Tidak ada pencatatan sistematis untuk melacak siapa yang melakukan inspeksi, kapan, dan perubahan apa yang dilakukan pada data. Hal ini mengakibatkan kesulitan dalam investigasi klaim, penyelesaian sengketa, dan kepatuhan audit. Transparansi dan akuntabilitas proses inspeksi sangat rendah.
  Contoh: Bab IV - Perancangan.tex:573: juga menekankan jejak audit untuk penelusuran dan investigasi, pemantauan

- `justifikasi` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:8: Bab ini menyajikan analisis mendalam terhadap sistem inspeksi kontainer yang ada saat ini, identifikasi kebutuhan sistem, eksplorasi alternatif solusi konseptual, dan justifikasi pemilihan solusi berdasarkan kriteria objektif. Analisis ini menjadi fondasi untuk perancangan arsitektur konseptual yang dipaparkan pada Bab IV.
  Contoh: Bab III - Analisis.tex:440: Berdasarkan matriks evaluasi dan analisis terhadap karakteristik setiap alternatif, \textbf{Alternatif 3: Arsitektur Modular Berbasis Domain} dipilih sebagai solusi yang paling sesuai untuk mengatasi masalah sistem inspeksi kontainer di Indonesia. Justifikasi pemilihan disusun berdasarkan empat perspektif: kebutuhan operasional, atribut kualitas ISO/IEC 25010, prinsip arsitektur, dan kepatuhan terhadap standar dan regulasi.
  Contoh: Bab III - Analisis.tex:493: Berdasarkan justifikasi dari empat perspektif tersebut, arsitektur modular

- `kapabilitas` - muncul 3 kali
  Contoh: Bab II - Studi.tex:152: dipenuhi melalui pusat pemrosesan yang menyediakan kapabilitas elastis untuk
  Contoh: Bab III - Analisis.tex:111: inspeksi. Proses juga belum memiliki kapabilitas untuk menyesuaikan kapasitas
  Contoh: Bab III - Analisis.tex:123: Temuan pada sistem saat ini diterjemahkan menjadi kebutuhan sistem yang merespons celah arsitektural secara langsung. Analisis kebutuhan dibagi menjadi dua kategori: kebutuhan fungsional yang mendefinisikan kapabilitas sistem, dan kebutuhan nonfungsional yang menentukan atribut kualitas agar sistem dapat beroperasi secara andal dalam konteks pelabuhan Indonesia.

- `karakteristik` - muncul 3 kali
  Contoh: Bab II - Studi.tex:41: Tabel \ref{tbl:inspeksi_klasifikasi} menggambarkan empat pendekatan utama inspeksi kargo yang umum digunakan dalam industri logistik. Setiap pendekatan memiliki karakteristik dan aplikasi yang berbeda, dan pemilihan pendekatan yang tepat bergantung pada kebutuhan operasional, regulasi, dan konteks pelabuhan.
  Contoh: Bab II - Studi.tex:49: yaitu seleksi risiko berdasarkan profil data historis, karakteristik pengirim,
  Contoh: Bab II - Studi.tex:73: Pendekatan representasi visual digunakan untuk mengidentifikasi deformasi struktural pada permukaan kontainer melalui analisis pola. Literatur memaparkan konsep ini sebagai proses representasi visual yang digunakan untuk memahami pola dan karakteristik objek secara konsisten.

- `keberlangsungan` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:561: keberlangsungan pemantauan maupun pencatatan data sesuai kondisi layanan yang
  Contoh: Bab VI - Evaluasi.tex:287: pemindai, keberlangsungan layanan, dan prosedur pengelolaan insiden menunjukkan
  Contoh: Lampiran-B.tex:220: \textit{screening} kontainer, dokumen tingkat layanan dan keberlangsungan layanan alat

- `kepabeanan` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:55: terintegrasi dengan alur kerja pelabuhan dan sistem kepabeanan. Ketiadaan
  Contoh: Bab II - Studi.tex:58: \textit{compliance decision}, yaitu keputusan kepabeanan berdasarkan bukti
  Contoh: Bab II - Studi.tex:275: World Customs Organization SAFE \textit{Framework of Standards} merupakan kerangka kerja internasional untuk mengamankan dan memfasilitasi perdagangan global \autocite{wco2025}. Kerangka ini menyediakan prinsip-prinsip untuk inspeksi kargo berbasis risiko dan pertukaran informasi elektronik antara otoritas kepabeanan.

- `keparahan` - muncul 3 kali
  Contoh: Bab II - Studi.tex:271: Institute of International Container Lessors (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC) menetapkan pedoman klasifikasi kerusakan dan dokumentasi yang menjadi dasar konsistensi penilaian kontainer \autocite{iicl2016, icswsc2023}. Standar ini mendefinisikan pola penilaian kerusakan yang konsisten, kategori kerusakan berdasarkan jenis dan tingkat keparahan, serta pentingnya dokumentasi yang mengikuti standar untuk keperluan audit dan klaim.
  Contoh: Bab III - Analisis.tex:89: kategori kerusakan, tingkat keparahan, atau kriteria keputusan inspeksi. Hasil
  Contoh: Bab IV - Perancangan.tex:111: Modul analisis visual melakukan deteksi otomatis terhadap berbagai jenis kerusakan berdasarkan model analisis yang dilatih. Setiap deteksi disertai dengan tingkat keyakinan dan tingkat keparahan. Hasil deteksi dapat divalidasi oleh petugas untuk perbaikan berkelanjutan melalui umpan balik.

- `ketertelusuran` - muncul 3 kali
  Contoh: 5 Abstrak.tex:18: inspeksi yang belum terintegrasi, keterbatasan ketertelusuran bukti inspeksi,
  Contoh: 5 Abstrak.tex:49: Kata kunci: arsitektur sistem, inspeksi kargo digital, integrasi data, pelabuhan, ketertelusuran.
  Contoh: Bab I - Pendahuluan.tex:77: otomasi pemeriksaan, tetapi juga mendukung integrasi data, ketertelusuran

- `kompleksitas` - muncul 3 kali
  Contoh: Bab II - Studi.tex:119: \textbf{\textit{Usability}} & \textit{Operability}, \textit{learnability} & Antarmuka dan alur informasi harus mudah dioperasikan oleh pengguna operasional tanpa menambah kompleksitas pemeriksaan \\
  Contoh: Bab III - Analisis.tex:272: memelihara kontrak dan katalog pertukaran informasi. Kompleksitas koordinasi
  Contoh: Bab III - Analisis.tex:339: skema \textit{event} tidak dikendalikan, kompleksitas meningkat dan konsistensi

- `komputasi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:145: Konsep \textit{edge-cloud computing} mengacu pada model arsitektur komputasi yang membagi beban pemrosesan antara komponen di lokasi sumber data dan pusat pemrosesan terpusat \autocite{shi2016}. Shi dkk. mendefinisikan \textit{edge computing} sebagai paradigma yang menempatkan komputasi dan penyimpanan data di dekat sumber data untuk mengoptimalkan respons dan efisiensi sistem.
  Contoh: Bab II - Studi.tex:145: Konsep \textit{edge-cloud computing} mengacu pada model arsitektur komputasi yang membagi beban pemrosesan antara komponen di lokasi sumber data dan pusat pemrosesan terpusat \autocite{shi2016}. Shi dkk. mendefinisikan \textit{edge computing} sebagai paradigma yang menempatkan komputasi dan penyimpanan data di dekat sumber data untuk mengoptimalkan respons dan efisiensi sistem.
  Contoh: Bab II - Studi.tex:179: \textit{Computer vision} merupakan bidang yang mempelajari bagaimana sistem komputasi dapat memperoleh pemahaman tingkat tinggi dari citra atau video digital \autocite{szeliski2022}. Prinsip dasar melibatkan transformasi informasi visual mentah menjadi representasi semantik yang dapat digunakan untuk pengambilan keputusan. Konsep ini dipaparkan dalam literatur sebagai pendekatan untuk memahami karakteristik interpretasi visual yang konsisten. Dalam konteks inspeksi kontainer, pendekatan ini relevan karena kerusakan struktural memiliki pola tepi, bentuk, dan tekstur yang dapat dipelajari model secara sistematis.

- `konektivitas` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:401: Keberlanjutan Operasional & Kemampuan untuk menjaga kontinuitas operasional meskipun terjadi gangguan infrastruktur atau konektivitas, serta adaptabilitas terhadap perubahan regulasi. \\
  Contoh: Bab IV - Perancangan.tex:136: Komponen lokal tetap menjalankan akuisisi video, inferensi, dan pemantauan aliran secara dekat dengan sumber data. Pemisahan ini mengurangi ketergantungan terhadap layanan terpusat untuk fungsi yang membutuhkan respons cepat, sekaligus menjaga bahwa penyimpanan hasil inspeksi tetap mengikuti alur terstruktur melalui layanan API saat konektivitas tersedia.
  Contoh: Bab IV - Perancangan.tex:656: tanpa menunggu respons dari sistem terpusat. Konektivitas jaringan pelabuhan

- `labelsep` - muncul 3 kali
  Contoh: TA.tex:283: labelsep=space,
  Contoh: TA.tex:291: labelsep=space,
  Contoh: TA.tex:301: labelsep=space,

- `latensi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:149: mengoptimalkan penggunaan \textit{bandwidth} dan mengurangi latensi.
  Contoh: Bab IV - Perancangan.tex:27: tersebar digunakan untuk menempatkan fungsi yang sensitif terhadap latensi di
  Contoh: Bab IV - Perancangan.tex:357: Gambar \ref{fig:deployment_architecture} menunjukkan distribusi komponen sistem antara perangkat \textit{edge} dan layanan terpusat. Pada sisi \textit{edge}, sistem menjalankan layanan untuk akuisisi aliran video, inferensi, dan siaran video langsung. Pada sisi terpusat, layanan API menangani persistensi dan penyediaan data, MongoDB menyimpan data terstruktur, media penyimpanan objek menyimpan artefak visual, dan aplikasi web menyediakan antarmuka bagi pengguna. Arsitektur ini menempatkan pemrosesan yang sensitif terhadap latensi di dekat sumber data, sementara penyimpanan dan penyajian informasi dipusatkan untuk menjaga konsistensi.

- `lines` - muncul 3 kali
  Contoh: 6 Kata Pengantar.tex:21: Tanjung Priok serta pihak PT Salam Pacific Indonesia Lines (SPIL) yang telah
  Contoh: Lampiran-B.tex:15: Peti Kemas Tanjung Priok PT Salam Pacific Indonesia Lines (SPIL), yang
  Contoh: Lampiran-B.tex:201: \textbf{Lokasi} & Depo Peti Kemas Tanjung Priok PT Salam Pacific Indonesia Lines (SPIL) \\ \addlinespace

- `listing` - muncul 3 kali
  Contoh: Bab VI - Evaluasi.tex:365: Listing~\ref{lst:container-entity-sample} memperlihatkan bahwa hasil OCR,
  Contoh: Lampiran-A.tex:43: Listing~\ref{lst:tracking-payload} menunjukkan contoh kanal data tambahan yang
  Contoh: Lampiran-B.tex:343: Cuplikan pada Listing~\ref{lst:container-entity-sample} memperlihatkan bahwa

- `literature` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:184: \node[box, below=of objective] (literature) {Studi literatur dan analisis kebutuhan};
  Contoh: Bab I - Pendahuluan.tex:191: \draw[line] (objective) -- (literature);
  Contoh: Bab I - Pendahuluan.tex:192: \draw[line] (literature) -- (design);

- `manifest` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:416: pemindaian, keputusan sistem, dan lampiran bukti inspeksi. Entitas MANIFEST
  Contoh: Bab IV - Perancangan.tex:433: tugas akhir ini, pusat model data berada pada entitas KONTAINER dan MANIFEST,
  Contoh: Bab V - Implementasi.tex:193: menyimpan identitas kontainer, hasil OCR, ringkasan manifest, hasil pemindaian

- `memetakan` - muncul 3 kali
  Contoh: 5 Abstrak.tex:45: akhir ini adalah rancangan arsitektur yang memetakan pembagian tanggung jawab
  Contoh: Bab II - Studi.tex:71: \textit{Non-Intrusive Inspection} (NII) merupakan konsep pemeriksaan kargo yang memungkinkan pemeriksaan tanpa perlu membuka kontainer. Teknologi NII mencakup pendekatan pencitraan yang dapat memetakan struktur dan isi kontainer secara nondestruktif. Konsep dasar NII didasarkan pada prinsip fisika yang memungkinkan penetrasi material untuk menghasilkan representasi visual dari interior objek tanpa intervensi fisik langsung \autocite{wco2020}.
  Contoh: Bab IV - Perancangan.tex:582: Desain arsitektur sistem inspeksi kargo digital secara eksplisit mempertimbangkan atribut kualitas yang didefinisikan dalam standar ISO/IEC 25010. Tabel~\ref{tbl:iso25010_mapping} memetakan komponen utama arsitektur terhadap atribut kualitas yang didukungnya.

- `memfasilitasi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:275: World Customs Organization SAFE \textit{Framework of Standards} merupakan kerangka kerja internasional untuk mengamankan dan memfasilitasi perdagangan global \autocite{wco2025}. Kerangka ini menyediakan prinsip-prinsip untuk inspeksi kargo berbasis risiko dan pertukaran informasi elektronik antara otoritas kepabeanan.
  Contoh: Bab II - Studi.tex:317: asal-usul informasi dan memfasilitasi audit terhadap proses pengambilan
  Contoh: Bab III - Analisis.tex:58: Tidak ada komponen yang memfasilitasi standardisasi proses, pencatatan digital

- `memvalidasi` - muncul 3 kali
  Contoh: 5 Abstrak.tex:47: inspeksi, dan memvalidasi kesesuaian rancangan terhadap realisasi sistem.
  Contoh: Bab III - Analisis.tex:46: Ketiadaan standar formal untuk penilaian kerusakan maupun dokumentasi digital yang terintegrasi dengan alur informasi pelabuhan mengakibatkan fragmentasi proses dan inkonsistensi keluaran. Setiap tahapan dilakukan secara manual tanpa dukungan sistem yang memvalidasi kelengkapan atau kebenaran data.
  Contoh: Bab III - Analisis.tex:152: & Sistem memvalidasi kelengkapan data sebelum keputusan operasional diambil & Tinggi \\

- `mendeteksi` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:33: Beberapa pendekatan teknologi sebenarnya sudah mulai diterapkan di industri global. Salah satunya adalah penggunaan kamera termal atau \textit{infrared thermography} yang dapat mendeteksi perbedaan suhu pada permukaan kontainer untuk mengidentifikasi adanya anomali seperti lubang, retakan, atau kebocoran. Metode ini tergolong cepat, tidak merusak objek yang diperiksa, dan cocok untuk \textit{screening} awal. Meski demikian, efektivitas metode ini sangat bergantung pada kondisi lingkungan dan jenis kerusakan. Penyok, korosi awal, atau kerusakan struktural ringan yang tidak memengaruhi suhu sering kali tidak terdeteksi, sehingga hasil inspeksi kurang dapat diandalkan. Selain itu, hasil dari inspeksi termal biasanya belum terintegrasi dengan sistem pelaporan digital yang dapat dilacak secara menyeluruh \autocite{kim2022}.
  Contoh: Bab I - Pendahuluan.tex:35: Di sisi lain, sejumlah operator pelabuhan internasional telah mengembangkan sistem pemindaian otomatis berbasis 3D yang ditempatkan di pintu masuk pelabuhan. Teknologi ini memungkinkan pemetaan bentuk kontainer secara waktu nyata untuk mendeteksi penyok atau kerusakan struktural lain tanpa perlu pemeriksaan manual. Sistem seperti TMEIC DMG 3D, Camco Argus ADI, dan Visy ADDS merupakan beberapa contoh teknologi yang digunakan untuk keperluan ini. Untuk bagian dalam kontainer, teknologi X-ray seperti Leidos VACIS dimanfaatkan untuk memindai isi tanpa perlu membuka kontainer, sehingga anomali isi atau barang ilegal dapat lebih cepat dikenali \autocite{lim2021}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.

- `mengimplementasikan` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:281: aplikasi web. \textbf{\textit{Application Layer}} mengimplementasikan logika bisnis
  Contoh: Bab IV - Perancangan.tex:361: Sebagai bagian dari penempatan lokal, sistem mengimplementasikan arsitektur \textit{edge} yang berfokus pada akuisisi aliran video dan pemrosesan responsif di lapangan.
  Contoh: Bab IV - Perancangan.tex:478: Untuk mengisolasi logika bisnis dari detail implementasi integrasi, rancangan sistem menggunakan \textbf{pola \textit{adapter}}. Setiap sistem eksternal direncanakan memiliki \textit{adapter} khusus yang mengimplementasikan antarmuka standar, sehingga penambahan atau penggantian sistem eksternal dapat dilakukan tanpa mengubah kode aplikasi inti.

- `mengintegrasikan` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:68: yang efektif perlu mampu mengintegrasikan pengambilan data di lapangan,
  Contoh: Bab I - Pendahuluan.tex:85: \item Bagaimana merancang arsitektur sistem yang mampu mengintegrasikan
  Contoh: Bab II - Studi.tex:233: terkait secara menyeluruh, serta mengintegrasikan tata kelola TI dengan tata

- `mengisolasi` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:478: Untuk mengisolasi logika bisnis dari detail implementasi integrasi, rancangan sistem menggunakan \textbf{pola \textit{adapter}}. Setiap sistem eksternal direncanakan memiliki \textit{adapter} khusus yang mengimplementasikan antarmuka standar, sehingga penambahan atau penggantian sistem eksternal dapat dilakukan tanpa mengubah kode aplikasi inti.
  Contoh: Bab IV - Perancangan.tex:569: untuk mengisolasi sistem dari ancaman eksternal, keamanan aplikasi melalui
  Contoh: Bab IV - Perancangan.tex:644: pemeliharaan dengan mengisolasi perubahan pada satu lapisan tanpa memengaruhi

- `merealisasikan` - muncul 3 kali
  Contoh: Bab V - Implementasi.tex:25: Artefak sistem yang digunakan untuk merealisasikan rancangan terdiri atas beberapa komponen utama yang
  Contoh: Bab V - Implementasi.tex:146: Selain jalur data terstruktur, sistem juga merealisasikan jalur video langsung
  Contoh: Bab V - Implementasi.tex:174: berhasil merealisasikan kebutuhan integrasi data lintas modul yang sebelumnya

- `merespons` - muncul 3 kali
  Contoh: Bab II - Studi.tex:197: Arsitektur berbasis kejadian merupakan pola desain yang membuat komponen sistem berinteraksi melalui notifikasi perubahan status, memungkinkan independensi temporal dan fungsional antara komponen \autocite{hohpe2003}. Dalam pendekatan ini, komponen yang menghasilkan informasi tidak perlu mengetahui komponen mana yang akan merespons informasi tersebut, dan sebaliknya. Konsep ini menciptakan sistem yang lebih fleksibel karena komponen baru dapat ditambahkan untuk merespons kejadian yang sudah ada tanpa mengubah komponen penghasil kejadian. Pendekatan berbasis kejadian ini selaras dengan kebutuhan inspeksi kargo yang memerlukan penelusuran perubahan status kontainer sepanjang alur pemeriksaan secara transparan.
  Contoh: Bab II - Studi.tex:197: Arsitektur berbasis kejadian merupakan pola desain yang membuat komponen sistem berinteraksi melalui notifikasi perubahan status, memungkinkan independensi temporal dan fungsional antara komponen \autocite{hohpe2003}. Dalam pendekatan ini, komponen yang menghasilkan informasi tidak perlu mengetahui komponen mana yang akan merespons informasi tersebut, dan sebaliknya. Konsep ini menciptakan sistem yang lebih fleksibel karena komponen baru dapat ditambahkan untuk merespons kejadian yang sudah ada tanpa mengubah komponen penghasil kejadian. Pendekatan berbasis kejadian ini selaras dengan kebutuhan inspeksi kargo yang memerlukan penelusuran perubahan status kontainer sepanjang alur pemeriksaan secara transparan.
  Contoh: Bab II - Studi.tex:245: operasi untuk merespons permintaan dan menciptakan nilai, \textit{Guiding

- `meskipun` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:42: perlu membuka segelnya. Meskipun teknologi ini meningkatkan efisiensi dan
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:79: Meskipun efektif sebagai \textit{screening} awal ketika terdapat perbedaan temperatur signifikan, IRT memiliki keterbatasan teoretis: kerusakan nontermal sering kali tidak terdeteksi karena tidak menghasilkan kontras temperatur yang memadai. Emisivitas permukaan, jarak pemindaian, dan kondisi lingkungan dapat memengaruhi akurasi hasil secara signifikan sehingga metode ini umumnya digunakan sebagai pelengkap metode inspeksi lainnya.

- `modularitas` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:284: jelas, mengikuti prinsip modularitas dan \textit{loose coupling}
  Contoh: Bab III - Analisis.tex:308: dependensinya. Jika disiplin arsitektural melemah, modularitas dapat berubah
  Contoh: Bab III - Analisis.tex:399: Modularitas Komponen & Kemudahan untuk melakukan pemeliharaan, pembaruan, dan evolusi sistem melalui pemisahan tanggung jawab antarkomponen yang jelas. \\

- `objective` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:183: \node[box, below=of problem] (objective) {Penetapan tujuan perancangan arsitektur sistem};
  Contoh: Bab I - Pendahuluan.tex:190: \draw[line] (problem) -- (objective);
  Contoh: Bab I - Pendahuluan.tex:191: \draw[line] (objective) -- (literature);

- `observasi` - muncul 3 kali
  Contoh: Lampiran-B.tex:72: Berdasarkan observasi lapangan pada kedua lokasi tersebut, diperoleh beberapa
  Contoh: Lampiran-B.tex:88: Hasil observasi pada kunjungan ke terminal menunjukkan bahwa alur masuk
  Contoh: Lampiran-B.tex:106: Observasi lapangan juga menunjukkan bahwa pemeriksaan fisik bagian luar

- `optimalisasi` - muncul 3 kali
  Contoh: 1 Halaman Judul.tex:7: {\Large\bfseries PERANCANGAN ARSITEKTUR SISTEM INSPEKSI KARGO DIGITAL TERINTEGRASI UNTUK OPTIMALISASI PROSES PEMERIKSAAN KONTAINER DI PELABUHAN}\\
  Contoh: 2 Lembar Pengesahan.tex:8: {\large\bfseries PERANCANGAN ARSITEKTUR SISTEM INSPEKSI KARGO DIGITAL TERINTEGRASI UNTUK OPTIMALISASI PROSES PEMERIKSAAN KONTAINER DI PELABUHAN}\\
  Contoh: 6 Kata Pengantar.tex:7: untuk Optimalisasi Proses Pemeriksaan Kontainer di Pelabuhan''. Laporan ini disusun

- `organization` - muncul 3 kali
  Contoh: Bab II - Studi.tex:15: Inspeksi kargo merupakan elemen krusial dalam rantai logistik global yang menjamin keamanan, kepatuhan regulasi, dan integritas barang dalam perdagangan internasional. Menurut World Customs Organization (WCO), inspeksi kargo yang efektif mencegah penyalahgunaan perdagangan, melindungi keamanan publik, dan mendukung kelancaran alur barang di perbatasan \autocite{worldbank2023}. Dalam konteks Indonesia, proses inspeksi kontainer di pelabuhan masih menghadapi tantangan signifikan terkait efisiensi, akurasi, dan integrasi sistem \autocite{pwc2023, crifasia2023}.
  Contoh: Bab II - Studi.tex:23: World Customs Organization (WCO) mengklasifikasikan metode inspeksi kargo ke dalam beberapa kategori berdasarkan tingkat intrusivitas dan prinsip dasar teknologi yang digunakan \autocite{wco2020}. Klasifikasi ini penting untuk memahami dampak operasional, biaya, dan kelayakan pendekatan inspeksi dalam konteks pelabuhan.
  Contoh: Bab II - Studi.tex:45: World Customs Organization SAFE \textit{Framework} 2025 menganjurkan pendekatan

- `otoritas` - muncul 3 kali
  Contoh: Bab II - Studi.tex:275: World Customs Organization SAFE \textit{Framework of Standards} merupakan kerangka kerja internasional untuk mengamankan dan memfasilitasi perdagangan global \autocite{wco2025}. Kerangka ini menyediakan prinsip-prinsip untuk inspeksi kargo berbasis risiko dan pertukaran informasi elektronik antara otoritas kepabeanan.
  Contoh: Bab IV - Perancangan.tex:191: pengelola terminal, otoritas, dan sistem informasi lain di lingkungan
  Contoh: Bab IV - Perancangan.tex:219: inspeksi untuk mendukung keputusan operasional. Otoritas pemerintah

- `pacific` - muncul 3 kali
  Contoh: 6 Kata Pengantar.tex:21: Tanjung Priok serta pihak PT Salam Pacific Indonesia Lines (SPIL) yang telah
  Contoh: Lampiran-B.tex:15: Peti Kemas Tanjung Priok PT Salam Pacific Indonesia Lines (SPIL), yang
  Contoh: Lampiran-B.tex:201: \textbf{Lokasi} & Depo Peti Kemas Tanjung Priok PT Salam Pacific Indonesia Lines (SPIL) \\ \addlinespace

- `pelacakan` - muncul 3 kali
  Contoh: 13 Daftar Simbol.tex:19: $[\,]$ & Menunjukkan himpunan atau daftar elemen, misalnya kumpulan objek hasil pelacakan pada \textit{payload} data terstruktur. \\
  Contoh: Bab I - Pendahuluan.tex:62: digital, pelacakan inspeksi, dan standar operasional yang konsisten, potensi
  Contoh: Bab I - Pendahuluan.tex:89: kontainer agar pencatatan hasil inspeksi, pelacakan riwayat, dan penyediaan

- `pelaporan` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:33: Beberapa pendekatan teknologi sebenarnya sudah mulai diterapkan di industri global. Salah satunya adalah penggunaan kamera termal atau \textit{infrared thermography} yang dapat mendeteksi perbedaan suhu pada permukaan kontainer untuk mengidentifikasi adanya anomali seperti lubang, retakan, atau kebocoran. Metode ini tergolong cepat, tidak merusak objek yang diperiksa, dan cocok untuk \textit{screening} awal. Meski demikian, efektivitas metode ini sangat bergantung pada kondisi lingkungan dan jenis kerusakan. Penyok, korosi awal, atau kerusakan struktural ringan yang tidak memengaruhi suhu sering kali tidak terdeteksi, sehingga hasil inspeksi kurang dapat diandalkan. Selain itu, hasil dari inspeksi termal biasanya belum terintegrasi dengan sistem pelaporan digital yang dapat dilacak secara menyeluruh \autocite{kim2022}.
  Contoh: Bab I - Pendahuluan.tex:61: audit, pelaporan, maupun koordinasi antarinstansi. Tanpa dukungan pencatatan
  Contoh: Bab II - Studi.tex:291: informasi elektronik untuk pelaporan dan pemrosesan kapal dan barang,

- `pelindo` - muncul 3 kali
  Contoh: 6 Kata Pengantar.tex:20: direalisasikan dalam bentuk implementasi; pihak Terminal Pelindo Peti Kemas
  Contoh: Lampiran-B.tex:13: konteks tugas akhir. Lokasi pertama adalah Terminal Pelindo Peti Kemas Tanjung
  Contoh: Lampiran-B.tex:193: \textbf{Lokasi} & Terminal Pelindo Peti Kemas Tanjung Priok \\ \addlinespace

- `pemangku` - muncul 3 kali
  Contoh: Bab II - Studi.tex:232: kebutuhan pemangku kepentingan yang beragam, mencakup organisasi dan ekosistem
  Contoh: Bab II - Studi.tex:324: menjadi relevan khususnya dalam sistem yang melibatkan banyak pemangku
  Contoh: Bab II - Studi.tex:340: \textbf{Celah 4: Prinsip \textit{Audit Trail} Multi-Pemangku Kepentingan.} ISO 27037 menyediakan pedoman untuk penanganan bukti digital secara umum, tetapi belum diadaptasi untuk alur kerja inspeksi kargo yang melibatkan banyak pemangku kepentingan dengan kepentingan dan kewenangan yang berbeda. Belum ada kerangka konseptual untuk merancang \textit{audit trail} yang dapat memenuhi kebutuhan pelabuhan, bea cukai, pemilik barang, dan regulator secara simultan.

- `pemantauan` - muncul 3 kali
  Contoh: 5 Abstrak.tex:33: pemantauan hasil inspeksi. Pada aspek data, entitas kontainer ditempatkan
  Contoh: Bab II - Studi.tex:36: \textbf{\textit{Sensor-Based Inspection}} & Penggunaan sensor untuk deteksi anomali berbasis parameter fisik & Dapat memberikan pemantauan waktu nyata, tetapi sensitif terhadap kondisi lingkungan \\
  Contoh: Bab III - Analisis.tex:340: data sulit dijaga. Organisasi juga perlu menyiapkan mekanisme pemantauan untuk

- `pemindai` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:39: gamma, atau pemindai sejenis sebagaimana diatur dalam Peraturan Direktur
  Contoh: Bab I - Pendahuluan.tex:40: Jenderal Bea dan Cukai PER-1/BC/2023. Teknologi pemindai lain, seperti
  Contoh: Bab VI - Evaluasi.tex:286: Dokumen lapangan terkait assessment alat pemindai, pengaturan lalu lintas alat

- `pemrosesan` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:94: \item Bagaimana merancang pembagian fungsi antarkomponen agar pemrosesan
  Contoh: Bab II - Studi.tex:145: Konsep \textit{edge-cloud computing} mengacu pada model arsitektur komputasi yang membagi beban pemrosesan antara komponen di lokasi sumber data dan pusat pemrosesan terpusat \autocite{shi2016}. Shi dkk. mendefinisikan \textit{edge computing} sebagai paradigma yang menempatkan komputasi dan penyimpanan data di dekat sumber data untuk mengoptimalkan respons dan efisiensi sistem.
  Contoh: Bab II - Studi.tex:145: Konsep \textit{edge-cloud computing} mengacu pada model arsitektur komputasi yang membagi beban pemrosesan antara komponen di lokasi sumber data dan pusat pemrosesan terpusat \autocite{shi2016}. Shi dkk. mendefinisikan \textit{edge computing} sebagai paradigma yang menempatkan komputasi dan penyimpanan data di dekat sumber data untuk mengoptimalkan respons dan efisiensi sistem.

- `pencitraan` - muncul 3 kali
  Contoh: Bab II - Studi.tex:34: \textbf{\textit{Non-Intrusive Inspection} (NII)} & Penggunaan teknologi pencitraan tanpa membuka kontainer untuk memeriksa isi dan struktur & Efisien waktu, dapat diotomatisasi, tetapi memerlukan investasi infrastruktur besar \\
  Contoh: Bab II - Studi.tex:69: \subsection{Konsep \textit{Non-Intrusive Inspection} (NII) dan Pencitraan}
  Contoh: Bab II - Studi.tex:71: \textit{Non-Intrusive Inspection} (NII) merupakan konsep pemeriksaan kargo yang memungkinkan pemeriksaan tanpa perlu membuka kontainer. Teknologi NII mencakup pendekatan pencitraan yang dapat memetakan struktur dan isi kontainer secara nondestruktif. Konsep dasar NII didasarkan pada prinsip fisika yang memungkinkan penetrasi material untuk menghasilkan representasi visual dari interior objek tanpa intervensi fisik langsung \autocite{wco2020}.

- `pengoperasian` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:694: Pengoperasian sistem membutuhkan beberapa peran dengan kompetensi yang sesuai
  Contoh: Bab IV - Perancangan.tex:710: Operator Inspeksi & Pengoperasian perangkat inspeksi, inisiasi proses inspeksi, validasi hasil deteksi & Prosedur inspeksi, pengoperasian perangkat \\
  Contoh: Bab IV - Perancangan.tex:710: Operator Inspeksi & Pengoperasian perangkat inspeksi, inisiasi proses inspeksi, validasi hasil deteksi & Prosedur inspeksi, pengoperasian perangkat \\

- `penyajian` - muncul 3 kali
  Contoh: 5 Abstrak.tex:24: dan penyajian informasi secara terpadu.
  Contoh: 5 Abstrak.tex:41: lain, penyimpanan hasil inspeksi pada model data inti, dan penyajian hasil pada
  Contoh: Bab I - Pendahuluan.tex:69: analisis visual, penyimpanan hasil inspeksi, serta penyajian informasi kepada

- `penyiaran` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:285: awal, dan penyiaran video langsung. Diagram ini menggambarkan struktur
  Contoh: Bab IV - Perancangan.tex:345: ke aplikasi web, penyiaran video langsung dari \textit{edge} ke aplikasi web,
  Contoh: Bab IV - Perancangan.tex:441: Komunikasi antarkomponen menggunakan dua bentuk utama, yaitu pertukaran data terstruktur melalui HTTP dan penyiaran video langsung melalui \textit{WebSocket}. Setiap komunikasi membawa \textit{metadata} identifikasi, waktu, dan data yang relevan dengan proses inspeksi.

- `point` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab III - Analisis.tex:40: berdasarkan \textit{checklist} standar seperti CTPAT \textit{Seven Point

- `presentasi` - muncul 3 kali
  Contoh: 5 Abstrak.tex:29: disusun dengan pendekatan berlapis yang mencakup lapisan presentasi, aplikasi,
  Contoh: Bab IV - Perancangan.tex:641: \textit{Keputusan:} Sistem menggunakan arsitektur berlapis dengan pemisahan tanggung jawab yang jelas antara lapisan presentasi, aplikasi, data, dan akuisisi lokal.
  Contoh: Bab V - Implementasi.tex:82: lapisan presentasi dalam arsitektur sistem.

- `priok` - muncul 3 kali
  Contoh: 6 Kata Pengantar.tex:21: Tanjung Priok serta pihak PT Salam Pacific Indonesia Lines (SPIL) yang telah
  Contoh: Lampiran-B.tex:14: Priok, yang dikunjungi pada tanggal 3 Februari 2026. Lokasi kedua adalah Depo
  Contoh: Lampiran-B.tex:15: Peti Kemas Tanjung Priok PT Salam Pacific Indonesia Lines (SPIL), yang

- `quran` - muncul 3 kali
  Contoh: 1 Halaman Judul.tex:18: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 2 Lembar Pengesahan.tex:19: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 5 Abstrak.tex:10: Aththariq Lisan Quran Daulah Sentono\\

- `realisasinya` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:61: Kapabilitas di atas diturunkan dari analisis kebutuhan untuk mendukung \textbf{kemudahan pemeliharaan} melalui modularitas, \textbf{interoperabilitas} melalui kontrak layanan yang jelas, \textbf{auditabilitas} melalui ketertelusuran aktivitas, dan \textbf{keandalan operasi}. Pada realisasinya, kapabilitas tersebut diwujudkan melalui pemisahan komponen \textit{edge}, layanan API, aplikasi web, dan lapisan penyimpanan data, sedangkan interoperabilitas dengan sistem eksternal diposisikan sebagai kesiapan perluasan.
  Contoh: Bab V - Implementasi.tex:166: Pada realisasinya, ketika aliran OCR berhasil mendeteksi nomor kontainer,
  Contoh: Bab VI - Evaluasi.tex:37: realisasinya terhadap kebutuhan sistem. Artefak utama yang digunakan sebagai

- `regulasi` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab I - Pendahuluan.tex:70: operator dan sistem lain di lingkungan pelabuhan. Selain itu, regulasi seperti
  Contoh: Bab I - Pendahuluan.tex:112: kondisi lapangan, regulasi yang berlaku, dan kebutuhan integrasi data di

- `responsif` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:51: Penyajian Informasi & Kemampuan menyajikan informasi kepada pengguna melalui antarmuka yang intuitif dan responsif \\
  Contoh: Bab IV - Perancangan.tex:361: Sebagai bagian dari penempatan lokal, sistem mengimplementasikan arsitektur \textit{edge} yang berfokus pada akuisisi aliran video dan pemrosesan responsif di lapangan.
  Contoh: Bab IV - Perancangan.tex:633: Bab ini telah menyajikan desain arsitektur sistem inspeksi kargo digital terintegrasi yang dirancang untuk mengatasi permasalahan yang telah diidentifikasi di Bab III. Desain ini berfokus pada integrasi komponen, pemrosesan responsif, dan konsistensi alur data sebagai dasar realisasi sistem yang diimplementasikan.

- `safe` - muncul 3 kali
  Contoh: Bab II - Studi.tex:45: World Customs Organization SAFE \textit{Framework} 2025 menganjurkan pendekatan
  Contoh: Bab II - Studi.tex:275: World Customs Organization SAFE \textit{Framework of Standards} merupakan kerangka kerja internasional untuk mengamankan dan memfasilitasi perdagangan global \autocite{wco2025}. Kerangka ini menyediakan prinsip-prinsip untuk inspeksi kargo berbasis risiko dan pertukaran informasi elektronik antara otoritas kepabeanan.
  Contoh: Bab II - Studi.tex:277: Pilar utama WCO SAFE \textit{Framework} mencakup pertukaran informasi intelijen dan

- `sentono` - muncul 3 kali
  Contoh: 1 Halaman Judul.tex:18: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 2 Lembar Pengesahan.tex:19: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 5 Abstrak.tex:10: Aththariq Lisan Quran Daulah Sentono\\

- `skalabilitas` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:333: tertentu tanpa keterikatan kuat pada modul internal, sehingga skalabilitas dan
  Contoh: Bab IV - Perancangan.tex:15: arsitektur yang mengedepankan modularitas, skalabilitas, dan keamanan.
  Contoh: Bab IV - Perancangan.tex:105: skalabilitas.

- `space` - muncul 3 kali
  Contoh: TA.tex:283: labelsep=space,
  Contoh: TA.tex:291: labelsep=space,
  Contoh: TA.tex:301: labelsep=space,

- `spil` - muncul 3 kali
  Contoh: 6 Kata Pengantar.tex:21: Tanjung Priok serta pihak PT Salam Pacific Indonesia Lines (SPIL) yang telah
  Contoh: Lampiran-B.tex:15: Peti Kemas Tanjung Priok PT Salam Pacific Indonesia Lines (SPIL), yang
  Contoh: Lampiran-B.tex:201: \textbf{Lokasi} & Depo Peti Kemas Tanjung Priok PT Salam Pacific Indonesia Lines (SPIL) \\ \addlinespace

- `terdefinisi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:94: menekan ketergantungan antarkomponen melalui antarmuka yang terdefinisi dengan
  Contoh: Bab II - Studi.tex:168: \textit{contract-based communication}, yaitu antarmuka yang terdefinisi secara
  Contoh: Bab III - Analisis.tex:290: terdefinisi dan kontrak antardomain yang terdokumentasi.

- `terdokumentasi` - muncul 3 kali
  Contoh: 5 Abstrak.tex:43: mendukung proses pemeriksaan kontainer yang lebih terstruktur, terdokumentasi,
  Contoh: Bab III - Analisis.tex:143: & Sistem mencatat hasil inspeksi berdasarkan standar formal yang terdokumentasi & Tinggi \\
  Contoh: Bab III - Analisis.tex:221: dengan aturan transisi status dan definisi peran aktor yang terdokumentasi.

- `terkonsolidasi` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:332: volume operasi, data terkonsolidasi dapat disimpan secara berkelanjutan,
  Contoh: Bab VI - Evaluasi.tex:367: \textit{manual review}, dan lampiran bukti visual memang terkonsolidasi pada
  Contoh: Lampiran-B.tex:293: terkonsolidasi pada satu entitas kontainer. Demi menjaga kerahasiaan, sebagian

- `terorkestrasi` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:261: Keunggulan pendekatan integrasi terorkestrasi terletak pada kemampuannya
  Contoh: Bab III - Analisis.tex:424: 2. Integrasi Terorkestrasi & 3 & 4 & 3 & 3 & 3 & 16 \\
  Contoh: Bab III - Analisis.tex:436: Hasil evaluasi menunjukkan bahwa \textbf{Alternatif 3: Arsitektur Modular Berbasis Domain} memperoleh skor total tertinggi (17) karena memberikan keseimbangan optimal antara keselarasan proses, modularitas komponen, dan keberlanjutan operasional. Alternatif integrasi terorkestrasi (skor 16) unggul pada interoperabilitas tetapi memerlukan tata kelola integrasi yang lebih kompleks. Alternatif tata kelola data terpadu (skor 15) memiliki keunggulan pada aspek \textit{governance} tetapi kurang fleksibel dalam modularitas komponen. Dua alternatif lainnya cenderung fokus pada satu aspek tertentu sehingga kontribusinya terhadap kriteria lain lebih terbatas. Hasil ini mengindikasikan bahwa solusi terpilih harus mampu menggabungkan struktur proses yang konsisten dengan komposisi komponen yang modular agar integrasi dan tata kelola data dapat berkembang secara berkelanjutan.

- `transaksional` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:48: Penyimpanan Data Terstruktur & Kemampuan menyimpan data transaksional dan master dengan menjaga konsistensi dan integritas informasi \\
  Contoh: Bab IV - Perancangan.tex:259: transaksional dan data master, sedangkan \textit{file storage} digunakan untuk
  Contoh: Bab IV - Perancangan.tex:300: Digunakan untuk komunikasi yang memerlukan respons langsung dan bersifat transaksional. Pola ini mendukung operasi yang memerlukan konfirmasi segera dan menjaga konsistensi transaksi antarkomponen.

- `true` - muncul 3 kali
  Contoh: TA.tex:148: colorlinks=true,
  Contoh: TA.tex:242: breaklines=true,
  Contoh: TA.tex:244: keepspaces=true,

- `ucirc` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab II - Studi.tex:271: Institute of International Container Lessors (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC) menetapkan pedoman klasifikasi kerusakan dan dokumentasi yang menjadi dasar konsistensi penilaian kontainer \autocite{iicl2016, icswsc2023}. Standar ini mendefinisikan pola penilaian kerusakan yang konsisten, kategori kerusakan berdasarkan jenis dan tingkat keparahan, serta pentingnya dokumentasi yang mengikuti standar untuk keperluan audit dan klaim.

- `validasi` - muncul 3 kali
  Contoh: 5 Abstrak.tex:20: tersebut menyebabkan proses verifikasi kontainer, validasi manifes, dan
  Contoh: Bab I - Pendahuluan.tex:141: terhadap sistem yang direalisasikan dan pada validasi integrasi
  Contoh: Bab II - Studi.tex:33: \textbf{\textit{Intrusive Inspection}} & Pemeriksaan manual langsung pada isi kontainer dengan membuka segel dan memeriksa dokumen & Akurasi tinggi untuk validasi barang, tetapi memerlukan waktu signifikan dan tenaga kerja intensif \\

- `world` - muncul 3 kali
  Contoh: Bab II - Studi.tex:15: Inspeksi kargo merupakan elemen krusial dalam rantai logistik global yang menjamin keamanan, kepatuhan regulasi, dan integritas barang dalam perdagangan internasional. Menurut World Customs Organization (WCO), inspeksi kargo yang efektif mencegah penyalahgunaan perdagangan, melindungi keamanan publik, dan mendukung kelancaran alur barang di perbatasan \autocite{worldbank2023}. Dalam konteks Indonesia, proses inspeksi kontainer di pelabuhan masih menghadapi tantangan signifikan terkait efisiensi, akurasi, dan integrasi sistem \autocite{pwc2023, crifasia2023}.
  Contoh: Bab II - Studi.tex:23: World Customs Organization (WCO) mengklasifikasikan metode inspeksi kargo ke dalam beberapa kategori berdasarkan tingkat intrusivitas dan prinsip dasar teknologi yang digunakan \autocite{wco2020}. Klasifikasi ini penting untuk memahami dampak operasional, biaya, dan kelayakan pendekatan inspeksi dalam konteks pelabuhan.
  Contoh: Bab II - Studi.tex:45: World Customs Organization SAFE \textit{Framework} 2025 menganjurkan pendekatan

- `akuntabilitas` - muncul 2 kali
  Contoh: Bab II - Studi.tex:323: inspeksi dan mendukung akuntabilitas dalam proses kepabeanan. Prinsip ini
  Contoh: Bab IV - Perancangan.tex:96: Tidak ada pencatatan sistematis untuk melacak siapa yang melakukan inspeksi, kapan, dan perubahan apa yang dilakukan pada data. Hal ini mengakibatkan kesulitan dalam investigasi klaim, penyelesaian sengketa, dan kepatuhan audit. Transparansi dan akuntabilitas proses inspeksi sangat rendah.

- `antarinstansi` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:61: audit, pelaporan, maupun koordinasi antarinstansi. Tanpa dukungan pencatatan
  Contoh: Bab I - Pendahuluan.tex:73: antarinstansi dan keamanan sistem informasi \autocite{kemenhub2022}.

- `antarproses` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:267: mengelola beban kerja antarproses secara lebih adaptif.
  Contoh: Lampiran-B.tex:78: antarproses belum sepenuhnya berjalan secara terpadu. Ketiga, kebutuhan akan

- `antarsistem` - muncul 2 kali
  Contoh: Lampiran-B.tex:172: data dan \textit{audit trail}, integrasi antarsistem, masalah utama dalam
  Contoh: Lampiran-B.tex:188: pengelolaan data dan \textit{audit trail}, integrasi antarsistem, serta harapan

- `bass` - muncul 2 kali
  Contoh: Bab II - Studi.tex:87: telah dipaparkan oleh Bass, Clements, dan Kazman \autocite{bass2022}. Dalam
  Contoh: Bab II - Studi.tex:211: \autocite{bass2022}. Bass dkk. menekankan bahwa standardisasi antarmuka

- `berevolusi` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:472: \autocite{newman2015}. Setiap domain dapat berevolusi dengan siklus
  Contoh: Bab IV - Perancangan.tex:20: agar setiap komponen memiliki tanggung jawab tunggal dan dapat berevolusi

- `communication` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:188: \node[box, below=of evaluation] (communication) {Penyusunan laporan tugas akhir};
  Contoh: Bab I - Pendahuluan.tex:195: \draw[line] (evaluation) -- (communication);

- `dianotasi` - muncul 2 kali
  Contoh: Bab V - Implementasi.tex:60: sudah dianotasi kepada aplikasi web.
  Contoh: Bab V - Implementasi.tex:148: menyajikan \textit{frame} yang telah dianotasi secara waktu nyata. Pemisahan

- `didefinisikan` - muncul 2 kali
  Contoh: Bab IV - Perancangan.tex:582: Desain arsitektur sistem inspeksi kargo digital secara eksplisit mempertimbangkan atribut kualitas yang didefinisikan dalam standar ISO/IEC 25010. Tabel~\ref{tbl:iso25010_mapping} memetakan komponen utama arsitektur terhadap atribut kualitas yang didukungnya.
  Contoh: Bab V - Implementasi.tex:175: didefinisikan sebagai salah satu kapabilitas arsitektur inti.

- `dideteksi` - muncul 2 kali
  Contoh: Bab VI - Evaluasi.tex:210: menyebarkan nomor kontainer yang berhasil dideteksi ke aliran lain yang sedang
  Contoh: Bab VI - Evaluasi.tex:280: dideteksi pada aliran OCR, sedangkan Gambar~\ref{fig:evidence_container_detail}

- `dimodifikasi` - muncul 2 kali
  Contoh: Bab II - Studi.tex:173: Pendekatan ini memungkinkan sistem untuk berkembang secara evolusioner karena komponen dapat dimodifikasi atau diganti tanpa memerlukan perubahan menyeluruh pada sistem. Prinsip ini digunakan dalam literatur untuk menjelaskan pola adaptasi arsitektur terhadap perubahan regulasi dan kebutuhan operasional.
  Contoh: Bab II - Studi.tex:259: \textit{integrity verification} untuk memastikan data tidak dimodifikasi secara

- `dioperasikan` - muncul 2 kali
  Contoh: Bab II - Studi.tex:119: \textbf{\textit{Usability}} & \textit{Operability}, \textit{learnability} & Antarmuka dan alur informasi harus mudah dioperasikan oleh pengguna operasional tanpa menambah kompleksitas pemeriksaan \\
  Contoh: Bab VII - Penutup.tex:42: ketahanan sistem ketika dioperasikan pada beban yang lebih tinggi.

- `dipropagasikan` - muncul 2 kali
  Contoh: Bab V - Implementasi.tex:167: nomor tersebut secara otomatis dipropagasikan ke aliran lain yang sedang aktif.
  Contoh: Bab VI - Evaluasi.tex:87: aliran OCR dapat dipropagasikan ke aliran lain, seperti aliran pemindaian

- `direpresentasikan` - muncul 2 kali
  Contoh: Bab II - Studi.tex:305: yang tercatat dengan kondisi aktual yang direpresentasikan.
  Contoh: Bab III - Analisis.tex:317: analisis temuan, hingga otorisasi, direpresentasikan sebagai \textit{event}

- `divalidasi` - muncul 2 kali
  Contoh: Bab IV - Perancangan.tex:111: Modul analisis visual melakukan deteksi otomatis terhadap berbagai jenis kerusakan berdasarkan model analisis yang dilatih. Setiap deteksi disertai dengan tingkat keyakinan dan tingkat keparahan. Hasil deteksi dapat divalidasi oleh petugas untuk perbaikan berkelanjutan melalui umpan balik.
  Contoh: Bab VII - Penutup.tex:45: perlu dilakukan agar rancangan arsitektur dapat divalidasi terhadap kondisi

- `edition` - muncul 2 kali
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: TA.tex:130: edition      = {edisi},

- `ekspektasi` - muncul 2 kali
  Contoh: Bab IV - Perancangan.tex:739: Penting untuk menegaskan batasan ruang lingkup desain sistem ini agar ekspektasi
  Contoh: Bab IV - Perancangan.tex:756: Desain arsitektur ini menetapkan kerangka yang memandu realisasi sistem berdasarkan karakteristik operasi pelabuhan dan kebutuhan pemangku kepentingan. Kebutuhan operasional memastikan sistem dapat dijalankan secara berkelanjutan, sedangkan batasan ruang lingkup menjaga fokus desain dan ekspektasi yang realistis terhadap kapabilitas sistem.

- `harmonisasi` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:224: dan \textit{template} inspeksi baku, sehingga harmonisasi proses dan data
  Contoh: Bab III - Analisis.tex:242: adalah harmonisasi internal. Konsolidasi lintas pelabuhan juga belum otomatis

- `implementabel` - muncul 2 kali
  Contoh: Bab VI - Evaluasi.tex:173: memang implementabel dan mendukung tujuan yang telah ditetapkan.
  Contoh: Bab VI - Evaluasi.tex:397: Komponen sistem memiliki tanggung jawab berbeda dan harus tetap dapat berkembang tanpa saling membebani & Komponen \textit{edge}, API, web, dan penyimpanan dipisahkan menurut peran & Skenario integrasi menunjukkan komponen saling terhubung melalui kontrak layanan yang berbeda sesuai tanggung jawabnya & Pembagian lapisan arsitektur terbukti implementabel pada ruang lingkup tugas akhir ini \\

- `information` - muncul 2 kali
  Contoh: Bab II - Studi.tex:229: COBIT (Control Objectives for Information and Related Technologies) merupakan kerangka kerja tata kelola dan manajemen teknologi informasi yang dikembangkan oleh ISACA \autocite{isaca2019}. COBIT 2019 menyediakan prinsip-prinsip untuk menyelaraskan TI dengan tujuan bisnis organisasi dan memastikan penggunaan teknologi yang efektif dan bertanggung jawab.
  Contoh: Bab II - Studi.tex:242: ITIL (Information Technology Infrastructure Library) merupakan kerangka kerja praktik terbaik untuk manajemen layanan TI yang dikembangkan oleh AXELOS \autocite{axelos2019}. ITIL 4 memperkenalkan konsep \textit{Service Value System} yang menekankan penciptaan nilai melalui layanan TI.

- `inner` - muncul 2 kali
  Contoh: TA.tex:219: inner=4cm,
  Contoh: TA.tex:351: inner=4cm,

- `institute` - muncul 2 kali
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:271: Institute of International Container Lessors (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC) menetapkan pedoman klasifikasi kerusakan dan dokumentasi yang menjadi dasar konsistensi penilaian kontainer \autocite{iicl2016, icswsc2023}. Standar ini mendefinisikan pola penilaian kerusakan yang konsisten, kategori kerusakan berdasarkan jenis dan tingkat keparahan, serta pentingnya dokumentasi yang mengikuti standar untuk keperluan audit dan klaim.

- `insw` - muncul 2 kali
  Contoh: 14 Daftar Singkatan.tex:19: INSW & \textit{Indonesia National Single Window} \\
  Contoh: Bab IV - Perancangan.tex:679: PCS, dan INSW memiliki antarmuka yang heterogen, sehingga \textit{adapter}

- `interior` - muncul 2 kali
  Contoh: Bab II - Studi.tex:71: \textit{Non-Intrusive Inspection} (NII) merupakan konsep pemeriksaan kargo yang memungkinkan pemeriksaan tanpa perlu membuka kontainer. Teknologi NII mencakup pendekatan pencitraan yang dapat memetakan struktur dan isi kontainer secara nondestruktif. Konsep dasar NII didasarkan pada prinsip fisika yang memungkinkan penetrasi material untuk menghasilkan representasi visual dari interior objek tanpa intervensi fisik langsung \autocite{wco2020}.
  Contoh: Bab IV - Perancangan.tex:747: Sebaliknya, desain ini tidak mencakup inspeksi interior kontainer, proses

- `international` - muncul 2 kali
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:271: Institute of International Container Lessors (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC) menetapkan pedoman klasifikasi kerusakan dan dokumentasi yang menjadi dasar konsistensi penilaian kontainer \autocite{iicl2016, icswsc2023}. Standar ini mendefinisikan pola penilaian kerusakan yang konsisten, kategori kerusakan berdasarkan jenis dan tingkat keparahan, serta pentingnya dokumentasi yang mengikuti standar untuk keperluan audit dan klaim.

- `keterhubungan` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:78: proses, dan keterhubungan dengan ekosistem digital pelabuhan Indonesia.
  Contoh: Bab V - Implementasi.tex:276: utama bab ini bukan pada rincian kode, melainkan pada keterhubungan antara

- `keterlacakan` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:64: Dimensi \textit{data} menunjukkan keterbatasan kualitas dan keterlacakan
  Contoh: Bab III - Analisis.tex:357: kode, dan \textit{lineage} data, sehingga keterlacakan dapat dijaga dari

- `ketidaksesuaian` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:306: ketidaksesuaian antarbagian sistem. Pendekatan ini juga menuntut dokumentasi
  Contoh: Bab III - Analisis.tex:341: memastikan tidak ada peristiwa yang hilang atau tertunda. Ketidaksesuaian

- `klaim` - muncul 2 kali
  Contoh: Bab II - Studi.tex:271: Institute of International Container Lessors (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC) menetapkan pedoman klasifikasi kerusakan dan dokumentasi yang menjadi dasar konsistensi penilaian kontainer \autocite{iicl2016, icswsc2023}. Standar ini mendefinisikan pola penilaian kerusakan yang konsisten, kategori kerusakan berdasarkan jenis dan tingkat keparahan, serta pentingnya dokumentasi yang mengikuti standar untuk keperluan audit dan klaim.
  Contoh: Bab IV - Perancangan.tex:96: Tidak ada pencatatan sistematis untuk melacak siapa yang melakukan inspeksi, kapan, dan perubahan apa yang dilakukan pada data. Hal ini mengakibatkan kesulitan dalam investigasi klaim, penyelesaian sengketa, dan kepatuhan audit. Transparansi dan akuntabilitas proses inspeksi sangat rendah.

- `krusial` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:23: satu aspek krusial yang perlu diperhatikan adalah pemeriksaan peti kemas.
  Contoh: Bab II - Studi.tex:15: Inspeksi kargo merupakan elemen krusial dalam rantai logistik global yang menjamin keamanan, kepatuhan regulasi, dan integritas barang dalam perdagangan internasional. Menurut World Customs Organization (WCO), inspeksi kargo yang efektif mencegah penyalahgunaan perdagangan, melindungi keamanan publik, dan mendukung kelancaran alur barang di perbatasan \autocite{worldbank2023}. Dalam konteks Indonesia, proses inspeksi kontainer di pelabuhan masih menghadapi tantangan signifikan terkait efisiensi, akurasi, dan integrasi sistem \autocite{pwc2023, crifasia2023}.

- `kueri` - muncul 2 kali
  Contoh: Bab V - Implementasi.tex:236: Bab IV. Data terstruktur membutuhkan dukungan kueri, pembaruan status, dan
  Contoh: Bab VI - Evaluasi.tex:246: untuk mendukung kueri dan pembaruan status, sedangkan artefak visual disimpan

- `language` - muncul 2 kali
  Contoh: TA.tex:115: language=english,
  Contoh: TA.tex:251: language=Python

- `lessors` - muncul 2 kali
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:271: Institute of International Container Lessors (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC) menetapkan pedoman klasifikasi kerusakan dan dokumentasi yang menjadi dasar konsistensi penilaian kontainer \autocite{iicl2016, icswsc2023}. Standar ini mendefinisikan pola penilaian kerusakan yang konsisten, kategori kerusakan berdasarkan jenis dan tingkat keparahan, serta pentingnya dokumentasi yang mengikuti standar untuk keperluan audit dan klaim.

- `management` - muncul 2 kali
  Contoh: Bab II - Studi.tex:281: Management}, serta penggunaan teknologi modern untuk inspeksi dan verifikasi
  Contoh: Lampiran-B.tex:202: \textbf{Narasumber} & Sudarmaji Aji (Improvement \& Operational Excellence Project Management, PT Salam Pacific Indonesia Lines) \\ \addlinespace

- `memverifikasi` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:92: komponen sistem yang memverifikasi kelengkapan atau kebenaran data inspeksi
  Contoh: Bab IV - Perancangan.tex:217: berbeda. Petugas inspeksi lapangan membutuhkan sarana untuk memverifikasi hasil

- `mereduksi` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:229: Pendekatan ini unggul dalam konteks standardisasi karena dapat mereduksi variasi
  Contoh: Bab III - Analisis.tex:262: mereduksi fragmentasi informasi melalui kontrak formal antarlayanan. Titik

- `merepresentasikan` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:204: Atribut kualitas tersebut dipilih karena merepresentasikan faktor kritis keberhasilan sistem inspeksi digital dan selaras dengan prinsip arsitektur sistem terdistribusi yang telah dipaparkan dalam Bab II.
  Contoh: Bab III - Analisis.tex:412: Evaluasi dilakukan dengan penilaian kualitatif yang diterjemahkan menjadi skala numerik 1 hingga 4, merepresentasikan tingkat kesesuaian alternatif dengan setiap kriteria: 1 (sangat rendah), 2 (rendah), 3 (sedang), 4 (tinggi). Tabel~\ref{tbl:evaluasi_alternatif} merangkum hasil evaluasi terhadap kelima alternatif solusi.

- `node` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:178: node distance=0.8cm,
  Contoh: Bab V - Implementasi.tex:65: Node.js dan Express. Komponen ini berperan sebagai pusat orkestrasi data

- `nugraha` - muncul 2 kali
  Contoh: 2 Lembar Pengesahan.tex:38: Ir. I Gusti Bagus Baskara Nugraha, S.T., M.T., Ph.D  \\[0.2cm]
  Contoh: 6 Kata Pengantar.tex:16: Ir. I Gusti Bagus Baskara Nugraha, S.T., M.T., Ph.D selaku dosen pembimbing

- `orisinalitas` - muncul 2 kali
  Contoh: 3 Pernyataan Orisinalitas.tex:1: \chapter*{PERNYATAAN ORISINALITAS}
  Contoh: 3 Pernyataan Orisinalitas.tex:2: \addcontentsline{toc}{chapter}{PERNYATAAN ORISINALITAS}

- `otomasi` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:77: otomasi pemeriksaan, tetapi juga mendukung integrasi data, ketertelusuran
  Contoh: Bab III - Analisis.tex:225: dilakukan terlebih dahulu sebelum integrasi atau otomasi lanjutan dirancang.

- `outer` - muncul 2 kali
  Contoh: TA.tex:220: outer=3cm,
  Contoh: TA.tex:352: outer=3cm,

- `penggabungan` - muncul 2 kali
  Contoh: Bab II - Studi.tex:185: Literatur membedakan pendekatan deteksi berdasarkan organisasi proses analisis visual, yang dapat dilakukan secara bertahap dengan pemisahan tahap analisis awal dari tahap identifikasi objek, atau secara terintegrasi dengan penggabungan kedua proses. Literatur menyoroti adanya pertimbangan antara kedalaman analisis dan efisiensi proses dalam pemilihan pendekatan deteksi visual.
  Contoh: Lampiran-B.tex:347: memungkinkan penggabungan konteks OCR, kerusakan, barang berisiko, klasifikasi

- `penggantian` - muncul 2 kali
  Contoh: Bab IV - Perancangan.tex:478: Untuk mengisolasi logika bisnis dari detail implementasi integrasi, rancangan sistem menggunakan \textbf{pola \textit{adapter}}. Setiap sistem eksternal direncanakan memiliki \textit{adapter} khusus yang mengimplementasikan antarmuka standar, sehingga penambahan atau penggantian sistem eksternal dapat dilakukan tanpa mengubah kode aplikasi inti.
  Contoh: Bab IV - Perancangan.tex:615: lain. Penggunaan antarmuka standar juga memungkinkan penggantian

- `peninjauan` - muncul 2 kali
  Contoh: Bab IV - Perancangan.tex:420: kepemilikan atau peninjauan data inspeksi.
  Contoh: Bab V - Implementasi.tex:215: mendukung autentikasi, otorisasi, dan peninjauan hasil inspeksi melalui aplikasi

- `penyunting` - muncul 2 kali
  Contoh: TA.tex:124: editor       = {penyunting},
  Contoh: TA.tex:125: editors      = {penyunting},

- `perekaman` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:254: seperti perekaman data, penilaian, pelaporan, dan koordinasi eksternal, yang
  Contoh: Bab III - Analisis.tex:319: konsumen \textit{event}; misalnya, modul perekaman data menghasilkan

- `persisten` - muncul 2 kali
  Contoh: Bab V - Implementasi.tex:137: data operasional yang bersifat persisten tetap melalui layanan API sehingga
  Contoh: Bab VI - Evaluasi.tex:314: bersifat persisten dan data yang bersifat temporer.

- `premis` - muncul 2 kali
  Contoh: Bab VI - Evaluasi.tex:175: Pertama, terdapat premis kebutuhan operasional dan prinsip arsitektur yang
  Contoh: Bab VI - Evaluasi.tex:346: Berdasarkan premis tersebut, rancangan menetapkan empat keputusan utama.

- `python` - muncul 2 kali
  Contoh: Bab V - Implementasi.tex:54: Komponen \textit{edge} direalisasikan sebagai layanan berbasis Python dan
  Contoh: TA.tex:251: language=Python

- `repositori` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:356: dibangun di atas repositori referensi yang menyimpan definisi istilah, kamus
  Contoh: Bab IV - Perancangan.tex:408: Sistem mengelola data menggunakan repositori terstruktur untuk informasi

- `rest` - muncul 2 kali
  Contoh: Bab VI - Evaluasi.tex:163: Pembacaan hasil oleh aplikasi web & \textit{Endpoint} REST pada layanan API dan tampilan inspeksi pada aplikasi web & Data hasil inspeksi dapat dibaca dan ditampilkan kembali kepada operator & Menunjukkan bahwa integrasi antarlapisan berakhir pada interaksi pengguna yang utuh \\
  Contoh: Bab VI - Evaluasi.tex:190: REST.

- `scan` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:41: Hi-Co Scan, mulai diperkenalkan karena mampu menampilkan isi kontainer tanpa
  Contoh: Lampiran-B.tex:226: Hico Scan menunjukkan bahwa layanan alat pemindai telah ditempatkan dalam

- `standards` - muncul 2 kali
  Contoh: Bab II - Studi.tex:216: standards} yang menjaga konsistensi interpretasi data; \textit{protocol
  Contoh: Bab II - Studi.tex:217: standards} yang memastikan keselarasan mekanisme pertukaran informasi; serta

- `style` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:179: box/.style={rectangle, rounded corners, draw=black, align=center, minimum width=0.78\textwidth, minimum height=0.95cm},
  Contoh: Bab I - Pendahuluan.tex:180: line/.style={-{Latex[length=2mm]}, thick}

- `subjektivitas` - muncul 2 kali
  Contoh: Bab II - Studi.tex:35: \textbf{\textit{Visual-Mechanical Inspection}} & Pemeriksaan struktur kontainer menggunakan panduan standar industri & Relatif cepat dan murah, tetapi bergantung pada subjektivitas dan pengalaman petugas \\
  Contoh: Bab III - Analisis.tex:69: hasil inspeksi bergantung pada subjektivitas petugas individual dan sulit

- `supervisor` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:24: regulasi kepabeanan dan keamanan. Supervisor operasional mengawasi proses
  Contoh: Bab III - Analisis.tex:42: pada formulir kertas atau \textit{spreadsheet} lokal, ditinjau oleh supervisor,

- `teridentifikasi` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:12: Analisis sistem saat ini dilakukan untuk mengidentifikasi keterbatasan mendasar yang menjadi akar permasalahan arsitektural, sehingga kebutuhan sistem yang dirumuskan kemudian benar-benar merespons celah yang teridentifikasi.
  Contoh: Bab III - Analisis.tex:83: Analisis terhadap model konseptual sistem saat ini menghasilkan identifikasi tiga kategori masalah arsitektural. Kategorisasi ini disusun berdasarkan pengelompokan tematik terhadap keterbatasan yang teridentifikasi pada dimensi \textit{people}, \textit{process}, \textit{technology}, dan \textit{data}. Setiap kategori masalah mencerminkan celah arsitektural yang menghambat pencapaian standardisasi, integrasi, dan keandalan operasional.

- `terisolasi` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:68: masih terisolasi dari sistem TOS, PCS, atau Inaportnet. Akibatnya, interpretasi
  Contoh: Bab III - Analisis.tex:459: \textit{maintainability}, modul yang terisolasi mempermudah perbaikan dan

- `terlindungi` - muncul 2 kali
  Contoh: Bab II - Studi.tex:120: \textbf{\textit{Security}} & \textit{Integrity}, \textit{authenticity} & Data hasil inspeksi, bukti visual, dan keputusan pemeriksaan harus terlindungi dari perubahan tidak sah dan memiliki asal data yang jelas \\
  Contoh: Bab IV - Perancangan.tex:30: memastikan data inspeksi, status layanan, dan artefak visual tetap terlindungi

- `transkrip` - muncul 2 kali
  Contoh: Lampiran-B.tex:154: transkrip lengkap, penyajian pada lampiran ini disusun sebagai ringkasan
  Contoh: Lampiran-B.tex:178: Jawaban atas pokok pertanyaan tersebut tidak direkam dalam bentuk transkrip

- `transparansi` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:330: logika penanganan \textit{event} tanpa mengganggu modul lain. Transparansi juga
  Contoh: Bab IV - Perancangan.tex:96: Tidak ada pencatatan sistematis untuk melacak siapa yang melakukan inspeksi, kapan, dan perubahan apa yang dilakukan pada data. Hal ini mengakibatkan kesulitan dalam investigasi klaim, penyelesaian sengketa, dan kepatuhan audit. Transparansi dan akuntabilitas proses inspeksi sangat rendah.

- `tren` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:72: Ketiadaan \textit{metadata} dan mekanisme ketertelusuran membuat data inspeksi sulit dimanfaatkan untuk analisis tren ataupun audit kepatuhan. Model interaksi antaraktor dan titik masalah utama pada sistem manual diringkas pada Gambar~\ref{fig:model_konseptual_saat_ini}.
  Contoh: Bab IV - Perancangan.tex:86: kesulitan dalam analisis historis dan pelacakan tren. Dokumentasi media

- `user` - muncul 2 kali
  Contoh: Bab IV - Perancangan.tex:419: Sementara itu, entitas USER berfungsi sebagai konteks autentikasi dan
  Contoh: Bab IV - Perancangan.tex:434: dengan USER sebagai konteks autentikasi dan pengelolaan akses. Dengan demikian,

- `validitas` - muncul 2 kali
  Contoh: Bab II - Studi.tex:322: \textit{traceability} memungkinkan verifikasi terhadap validitas hasil
  Contoh: Bab V - Implementasi.tex:266: informasi. Pola realisasi ini memperkuat validitas keputusan arsitektural

- `variabilitas` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:30: Ketergantungan penuh pada interpretasi manual menyebabkan variabilitas hasil
  Contoh: Bab IV - Perancangan.tex:81: Petugas inspeksi melakukan pemeriksaan visual berdasarkan panduan inspeksi standar. Namun, penerapan panduan ini sangat bergantung pada interpretasi subjektif setiap petugas, menghasilkan variabilitas tinggi dalam hasil inspeksi. Tidak ada mekanisme validasi konsistensi antarpetugas.

- `adapter` - muncul 1 kali
  Contoh: Bab IV - Perancangan.tex:598: Pola Adapter Integrasi & \textit{Compatibility} - \textit{Interoperability} & Abstraksi sistem eksternal memudahkan pertukaran informasi ketika integrasi diperluas \\

- `adds` - muncul 1 kali
  Contoh: Bab I - Pendahuluan.tex:35: Di sisi lain, sejumlah operator pelabuhan internasional telah mengembangkan sistem pemindaian otomatis berbasis 3D yang ditempatkan di pintu masuk pelabuhan. Teknologi ini memungkinkan pemetaan bentuk kontainer secara waktu nyata untuk mendeteksi penyok atau kerusakan struktural lain tanpa perlu pemeriksaan manual. Sistem seperti TMEIC DMG 3D, Camco Argus ADI, dan Visy ADDS merupakan beberapa contoh teknologi yang digunakan untuk keperluan ini. Untuk bagian dalam kontainer, teknologi X-ray seperti Leidos VACIS dimanfaatkan untuk memindai isi tanpa perlu membuka kontainer, sehingga anomali isi atau barang ilegal dapat lebih cepat dikenali \autocite{lim2021}.

- `align` - muncul 1 kali
  Contoh: Bab I - Pendahuluan.tex:179: box/.style={rectangle, rounded corners, draw=black, align=center, minimum width=0.78\textwidth, minimum height=0.95cm},

- `andothers` - muncul 1 kali
  Contoh: TA.tex:123: andothers    = {dkk.},

- `antaratribut` - muncul 1 kali
  Contoh: Bab II - Studi.tex:354: antaratribut dapat dijelaskan secara relevan terhadap operasi pelabuhan.

- `antarbagian` - muncul 1 kali
  Contoh: Bab III - Analisis.tex:306: ketidaksesuaian antarbagian sistem. Pendekatan ini juga menuntut dokumentasi

- `antarentitas` - muncul 1 kali
  Contoh: Bab IV - Perancangan.tex:256: antarentitas utama seperti kontainer, manifes, dan hasil pemindaian.

- `antarhasil` - muncul 1 kali
  Contoh: Bab IV - Perancangan.tex:411: antarhasil inspeksi. Model ini diturunkan dari kebutuhan integrasi hasil OCR,

- `antarlokasi` - muncul 1 kali
  Contoh: Bab III - Analisis.tex:397: Keselarasan Proses & Kemampuan untuk menyediakan standardisasi proses inspeksi dan konsistensi hasil antarpetugas serta antarlokasi. \\

- `antarmodul` - muncul 1 kali
  Contoh: Bab III - Analisis.tex:305: Setiap perubahan pada kontrak antarmodul harus dikendalikan agar tidak memicu

- `antarotoritas` - muncul 1 kali
  Contoh: Bab II - Studi.tex:278: risiko antarotoritas kepabeanan melalui \textit{Customs-to-Customs Network},

- `antarpelaku` - muncul 1 kali
  Contoh: Bab III - Analisis.tex:230: interpretasi antarpelaku. Seluruh aktor bekerja mengikuti model proses yang

- `antarpersonel` - muncul 1 kali
  Contoh: Bab III - Analisis.tex:31: inspeksi antarpersonel yang signifikan. Tidak adanya mekanisme standardisasi

- `antarunit` - muncul 1 kali
  Contoh: Lampiran-B.tex:204: \textbf{Ringkasan Temuan} & Kegiatan operasional di depo memperlihatkan pentingnya keselarasan informasi kondisi kontainer, status proses, dan bukti visual agar koordinasi antarunit kerja dapat berjalan lebih efisien. \\

- `argus` - muncul 1 kali
  Contoh: Bab I - Pendahuluan.tex:35: Di sisi lain, sejumlah operator pelabuhan internasional telah mengembangkan sistem pemindaian otomatis berbasis 3D yang ditempatkan di pintu masuk pelabuhan. Teknologi ini memungkinkan pemetaan bentuk kontainer secara waktu nyata untuk mendeteksi penyok atau kerusakan struktural lain tanpa perlu pemeriksaan manual. Sistem seperti TMEIC DMG 3D, Camco Argus ADI, dan Visy ADDS merupakan beberapa contoh teknologi yang digunakan untuk keperluan ini. Untuk bagian dalam kontainer, teknologi X-ray seperti Leidos VACIS dimanfaatkan untuk memindai isi tanpa perlu membuka kontainer, sehingga anomali isi atau barang ilegal dapat lebih cepat dikenali \autocite{lim2021}.

- `assessment` - muncul 1 kali
  Contoh: Bab VI - Evaluasi.tex:286: Dokumen lapangan terkait assessment alat pemindai, pengaturan lalu lintas alat

- `ataupun` - muncul 1 kali
  Contoh: Bab III - Analisis.tex:72: Ketiadaan \textit{metadata} dan mekanisme ketertelusuran membuat data inspeksi sulit dimanfaatkan untuk analisis tren ataupun audit kepatuhan. Model interaksi antaraktor dan titik masalah utama pada sistem manual diringkas pada Gambar~\ref{fig:model_konseptual_saat_ini}.

- `authordate` - muncul 1 kali
  Contoh: TA.tex:114: authordate,

- `autolang` - muncul 1 kali
  Contoh: TA.tex:116: autolang=other

- `axelos` - muncul 1 kali
  Contoh: Bab II - Studi.tex:242: ITIL (Information Technology Infrastructure Library) merupakan kerangka kerja praktik terbaik untuk manajemen layanan TI yang dikembangkan oleh AXELOS \autocite{axelos2019}. ITIL 4 memperkenalkan konsep \textit{Service Value System} yang menekankan penciptaan nilai melalui layanan TI.

- `backend` - muncul 1 kali
  Contoh: TA.tex:113: backend=biber,
