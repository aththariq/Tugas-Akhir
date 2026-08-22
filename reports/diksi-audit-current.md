# Audit Diksi dan Ejaan Rawan

Laporan ini dibuat otomatis dari sumber `.tex`. Setiap temuan adalah kandidat yang perlu dicek manual, bukan vonis final.

Total temuan pola rawan: 0
Total kandidat spellcheck Aspell: 470

## Pola Rawan

Tidak ada temuan dari daftar pola yang diperiksa.

## Kandidat Spellcheck Aspell

Bagian ini memakai kamus `aspell-id` dan allowlist teknis lokal. Kandidat nama diri atau istilah teknis dapat ditambahkan ke allowlist.

- `algoritma` - muncul 3 kali
  Contoh: 11 Daftar Algoritma.tex:6: \addcontentsline{toc}{chapter}{DAFTAR ALGORITMA}
  Contoh: 4 Pernyataan Penggunaan AI.tex:28: 8 & Penyusunan konsep desain atau algoritma & ChatGPT & Rendah & Penyusunan alternatif struktur penjelasan \\
  Contoh: Bab I - Pendahuluan.tex:133: arsitektur data, bukan pada implementasi detail algoritma deteksi, strategi

- `align` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:193: box/.style={rectangle, rounded corners, draw=black, align=center, minimum width=0.78\textwidth, minimum height=0.95cm},
  Contoh: Bab III - Analisis.tex:274: altbox/.style={rectangle, rounded corners, draw=black, align=center, minimum width=3.05cm, minimum height=1.05cm},
  Contoh: Bab III - Analisis.tex:275: chosen/.style={rectangle, rounded corners, draw=black, very thick, align=center, minimum width=3.05cm, minimum height=1.05cm},

- `analitik` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:182: \textbf{FR-09} & \makecell[l]{Integrasi\\Data} & Sistem menyajikan akses terstruktur untuk pelaporan dan analitik & Sedang \\
  Contoh: Bab III - Analisis.tex:431: analitik proses. Selain itu, pihak eksternal dapat berlangganan \textit{event}
  Contoh: Bab III - Analisis.tex:475: yang baik dengan sistem pelaporan dan analitik agar manfaat \textit{data

- `antaraktor` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:91: Ketiadaan \textit{metadata} dan mekanisme ketertelusuran membuat data inspeksi sulit dimanfaatkan untuk analisis tren ataupun audit kepatuhan. Model interaksi antaraktor dan titik masalah utama pada sistem manual diringkas pada Gambar~\ref{fig:model_konseptual_saat_ini}.
  Contoh: Bab III - Analisis.tex:441: \textit{event} dapat menimbulkan perbedaan status antaraktor, sehingga
  Contoh: Bab III - Analisis.tex:465: tanggung jawab antaraktor menjadi lebih jelas melalui kepemilikan data,

- `antardomain` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:389: terdefinisi dan kontrak antardomain yang terdokumentasi.
  Contoh: Bab III - Analisis.tex:403: Keterbatasannya terletak pada kebutuhan tata kelola antardomain yang konsisten.
  Contoh: Bab III - Analisis.tex:562: \textit{interoperability}, kontrak antardomain dapat dirancang sebagai

- `antarpemangku` - muncul 3 kali
  Contoh: 5 Abstrak.tex:17: di antaranya fragmentasi informasi antarpemangku kepentingan, pencatatan hasil
  Contoh: Bab II - Studi.tex:292: pertukaran data elektronik antarpemangku kepentingan melalui platform
  Contoh: Bab III - Analisis.tex:70: antarpemangku kepentingan tanpa mekanisme pelacakan formal.

- `antarpetugas` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:179: \textbf{FR-06} & \makecell[l]{Standardisasi\\Proses} & Sistem menjaga konsistensi interpretasi hasil antarpetugas & Tinggi \\
  Contoh: Bab III - Analisis.tex:496: Keselarasan Proses & Kemampuan untuk menyediakan standardisasi proses inspeksi dan konsistensi hasil antarpetugas serta antarlokasi. \\
  Contoh: Bab IV - Perancangan.tex:92: petugas dan belum didukung mekanisme validasi konsistensi antarpetugas.

- `antarsistem` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:251: Integrasi terorkestrasi & Pertukaran informasi antarsistem & Layanan tematik yang dikoordinasikan oleh lapisan orkestrasi & Kuat untuk interoperabilitas, tetapi membutuhkan tata kelola kontrak layanan yang ketat \\
  Contoh: Lampiran-B.tex:172: data dan \textit{audit trail}, integrasi antarsistem, masalah utama dalam
  Contoh: Lampiran-B.tex:188: pengelolaan data dan \textit{audit trail}, integrasi antarsistem, serta harapan

- `application` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:355: \node[layerbox] (application) at (0,-1.45) {\textbf{Lapisan Aplikasi}\\Layanan Inspeksi, Analisis, dan Integrasi};
  Contoh: Bab IV - Perancangan.tex:359: \draw[line] ([xshift=-1.25cm]application.north) -- ([xshift=-1.25cm]presentation.south);
  Contoh: Bab IV - Perancangan.tex:361: \draw[line] ([xshift=1.35cm]application.south) -- ([xshift=1.35cm]data.north);

- `arsitektural` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:163: menyeluruh, melainkan untuk menjelaskan bagaimana keputusan arsitektural
  Contoh: Bab III - Analisis.tex:12: Analisis sistem saat ini dilakukan untuk mengidentifikasi keterbatasan mendasar yang menjadi akar permasalahan arsitektural, sehingga kebutuhan sistem yang dirumuskan kemudian benar-benar merespons celah yang teridentifikasi.
  Contoh: Bab III - Analisis.tex:102: Analisis terhadap model konseptual sistem saat ini menghasilkan identifikasi tiga kategori masalah arsitektural. Kategorisasi ini disusun berdasarkan pengelompokan tematik terhadap keterbatasan yang teridentifikasi pada dimensi \textit{people}, \textit{process}, \textit{technology}, dan \textit{data}. Setiap kategori masalah mencerminkan celah arsitektural yang menghambat pencapaian standardisasi, integrasi, dan keandalan operasional.

- `aththariq` - muncul 3 kali
  Contoh: 1 Halaman Judul.tex:18: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 2 Lembar Pengesahan.tex:18: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 5 Abstrak.tex:10: Aththariq Lisan Quran Daulah Sentono\\

- `berfokus` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:132: \item Tugas akhir ini berfokus pada perancangan arsitektur sistem dan
  Contoh: Bab IV - Perancangan.tex:140: realisasi integrasi masih berfokus pada alur internal proyek, sedangkan
  Contoh: Bab IV - Perancangan.tex:246: integrasi aktual masih berfokus pada interaksi internal antara komponen

- `berinteraksi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:197: Arsitektur berbasis kejadian merupakan pola desain yang membuat komponen sistem berinteraksi melalui notifikasi perubahan status, memungkinkan independensi temporal dan fungsional antara komponen \autocite{hohpe2003}. Dalam pendekatan ini, komponen yang menghasilkan informasi tidak perlu mengetahui komponen mana yang akan merespons informasi tersebut, dan sebaliknya. Konsep ini menciptakan sistem yang lebih fleksibel karena komponen baru dapat ditambahkan untuk merespons kejadian yang sudah ada tanpa mengubah komponen penghasil kejadian. Pendekatan berbasis kejadian ini selaras dengan kebutuhan inspeksi kargo yang memerlukan penelusuran perubahan status kontainer sepanjang alur pemeriksaan secara transparan.
  Contoh: Bab III - Analisis.tex:31: berinteraksi dengan \textit{Terminal Operating System}.
  Contoh: Bab III - Analisis.tex:497: Interoperabilitas & Kemampuan untuk berinteraksi dengan berbagai sistem pelabuhan (TOS, PCS, Inaportnet) tanpa modifikasi signifikan pada sistem eksternal. \\

- `berisiko` - muncul 3 kali
  Contoh: Bab II - Studi.tex:53: berisiko sedang sehingga proses dapat dipercepat tanpa pembongkaran fisik.
  Contoh: Bab II - Studi.tex:56: berisiko tinggi, \textit{physical inspection} tetap diperlukan sebagai validasi
  Contoh: Bab III - Analisis.tex:375: perubahan yang terstruktur, lapisan orkestrasi justru berisiko menjadi hambatan

- `berkomunikasi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:210: memungkinkan komponen heterogen untuk berkomunikasi secara efektif
  Contoh: Bab III - Analisis.tex:354: berkomunikasi melalui kontrak pertukaran informasi standar. Alur informasi
  Contoh: Bab VI - Evaluasi.tex:23: penyimpanan dapat berkomunikasi sesuai dengan rancangan arsitektur?

- `black` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:193: box/.style={rectangle, rounded corners, draw=black, align=center, minimum width=0.78\textwidth, minimum height=0.95cm},
  Contoh: Bab III - Analisis.tex:274: altbox/.style={rectangle, rounded corners, draw=black, align=center, minimum width=3.05cm, minimum height=1.05cm},
  Contoh: Bab III - Analisis.tex:275: chosen/.style={rectangle, rounded corners, draw=black, very thick, align=center, minimum width=3.05cm, minimum height=1.05cm},

- `bottom` - muncul 3 kali
  Contoh: TA.tex:221: bottom=3cm
  Contoh: TA.tex:286: capposition=bottom
  Contoh: TA.tex:354: bottom=3cm

- `camera` - muncul 3 kali
  Contoh: 13 Daftar Simbol.tex:17: \{camera\_id\} & Menunjukkan parameter identitas kamera pada jalur layanan atau aliran video langsung. \\
  Contoh: Bab V - Implementasi.tex:250: \node[block] (camera) at (0,2.2) {Kamera\\\textit{RTSP}};
  Contoh: Bab V - Implementasi.tex:257: \draw[arrow] (camera) -- (tepi);

- `capposition` - muncul 3 kali
  Contoh: TA.tex:286: capposition=bottom
  Contoh: TA.tex:294: capposition=top,
  Contoh: TA.tex:306: capposition=top

- `center` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:193: box/.style={rectangle, rounded corners, draw=black, align=center, minimum width=0.78\textwidth, minimum height=0.95cm},
  Contoh: Bab III - Analisis.tex:274: altbox/.style={rectangle, rounded corners, draw=black, align=center, minimum width=3.05cm, minimum height=1.05cm},
  Contoh: Bab III - Analisis.tex:275: chosen/.style={rectangle, rounded corners, draw=black, very thick, align=center, minimum width=3.05cm, minimum height=1.05cm},

- `chapter` - muncul 3 kali
  Contoh: 10 Daftar Persamaan.tex:6: \addcontentsline{toc}{chapter}{DAFTAR PERSAMAAN}
  Contoh: 11 Daftar Algoritma.tex:6: \addcontentsline{toc}{chapter}{DAFTAR ALGORITMA}
  Contoh: 12 Daftar Listing.tex:4: \addcontentsline{toc}{chapter}{DAFTAR \textit{LISTING}}

- `chatgpt` - muncul 3 kali
  Contoh: 4 Pernyataan Penggunaan AI.tex:14: 1 & Pemeriksaan ejaan dan tata bahasa & ChatGPT & Rendah & Semua bab \\
  Contoh: 4 Pernyataan Penggunaan AI.tex:16: 2 & Pembuatan teks & ChatGPT & Rendah & Bab I--Bab VII \\
  Contoh: 4 Pernyataan Penggunaan AI.tex:20: 4 & Pencarian informasi atau referensi & ChatGPT & Rendah & Studi literatur dan perumusan draf \\

- `cloud` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:701: \node[group] (cloud) at (0,0) {\textbf{Cloud / Layanan Terpusat}\\Layanan API, MongoDB, R2, dan Aplikasi Web};
  Contoh: Bab IV - Perancangan.tex:708: \draw[line] (network.north) -- (cloud.south);
  Contoh: Bab IV - Perancangan.tex:709: \draw[line, dashed] (network.east) -- ++(1.45,0) \|- (cloud.east);

- `cobit` - muncul 3 kali
  Contoh: 14 Daftar Singkatan.tex:24: COBIT & \textit{Control Objectives for Information and Related Technologies} \\
  Contoh: Bab II - Studi.tex:229: COBIT (Control Objectives for Information and Related Technologies) merupakan kerangka kerja tata kelola dan manajemen teknologi informasi yang dikembangkan oleh ISACA \autocite{isaca2019}. COBIT 2019 menyediakan prinsip-prinsip untuk menyelaraskan TI dengan tujuan bisnis organisasi dan memastikan penggunaan teknologi yang efektif dan bertanggung jawab.
  Contoh: Bab II - Studi.tex:229: COBIT (Control Objectives for Information and Related Technologies) merupakan kerangka kerja tata kelola dan manajemen teknologi informasi yang dikembangkan oleh ISACA \autocite{isaca2019}. COBIT 2019 menyediakan prinsip-prinsip untuk menyelaraskan TI dengan tujuan bisnis organisasi dan memastikan penggunaan teknologi yang efektif dan bertanggung jawab.

- `container` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.

- `corners` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:193: box/.style={rectangle, rounded corners, draw=black, align=center, minimum width=0.78\textwidth, minimum height=0.95cm},
  Contoh: Bab III - Analisis.tex:274: altbox/.style={rectangle, rounded corners, draw=black, align=center, minimum width=3.05cm, minimum height=1.05cm},
  Contoh: Bab III - Analisis.tex:275: chosen/.style={rectangle, rounded corners, draw=black, very thick, align=center, minimum width=3.05cm, minimum height=1.05cm},

- `ctpat` - muncul 3 kali
  Contoh: 14 Daftar Singkatan.tex:25: CTPAT & \textit{Customs-Trade Partnership Against Terrorism} \\
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.

- `customs` - muncul 3 kali
  Contoh: Bab II - Studi.tex:15: Inspeksi kargo merupakan elemen krusial dalam rantai logistik global yang menjamin keamanan, kepatuhan regulasi, dan integritas barang dalam perdagangan internasional. Menurut World Customs Organization (WCO), inspeksi kargo yang efektif mencegah penyalahgunaan perdagangan, melindungi keamanan publik, dan mendukung kelancaran alur barang di perbatasan \autocite{worldbank2023}. Dalam konteks Indonesia, proses inspeksi kontainer di pelabuhan masih menghadapi tantangan signifikan terkait efisiensi, akurasi, dan integrasi sistem \autocite{pwc2023, crifasia2023}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:23: World Customs Organization (WCO) mengklasifikasikan metode inspeksi kargo ke dalam beberapa kategori berdasarkan tingkat intrusivitas dan prinsip dasar teknologi yang digunakan \autocite{wco2020}. Klasifikasi ini penting untuk memahami dampak operasional, biaya, dan kelayakan pendekatan inspeksi dalam konteks pelabuhan.

- `daulah` - muncul 3 kali
  Contoh: 1 Halaman Judul.tex:18: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 2 Lembar Pengesahan.tex:18: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 5 Abstrak.tex:10: Aththariq Lisan Quran Daulah Sentono\\

- `depo` - muncul 3 kali
  Contoh: Lampiran-B.tex:14: Priok, yang dikunjungi pada tanggal 3 Februari 2026. Lokasi kedua adalah Depo
  Contoh: Lampiran-B.tex:153: pelabuhan dan depo peti kemas. Karena wawancara tidak direkam dalam bentuk
  Contoh: Lampiran-B.tex:201: \textbf{Lokasi} & Depo Peti Kemas Tanjung Priok PT Salam Pacific Indonesia Lines (SPIL) \\ \addlinespace

- `design` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:198: \node[box, below=of objective] (design) {Perancangan dan pengembangan artefak arsitektur sistem};
  Contoh: Bab I - Pendahuluan.tex:204: \draw[line] (objective) -- (design);
  Contoh: Bab I - Pendahuluan.tex:205: \draw[line] (design) -- (demo);

- `diakses` - muncul 3 kali
  Contoh: Bab II - Studi.tex:262: dicatat, serta \textit{accessibility} agar jejak audit dapat diakses untuk
  Contoh: Bab III - Analisis.tex:124: \item Data inspeksi belum dapat diakses secara waktu nyata oleh sistem TOS,
  Contoh: Bab IV - Perancangan.tex:134: otomatis dalam waktu singkat setelah proses inspeksi dimulai, dapat diakses

- `diaudit` - muncul 3 kali
  Contoh: Bab II - Studi.tex:48: yang terstruktur dan dapat diaudit. Tahap awalnya adalah \textit{targeting},
  Contoh: Bab II - Studi.tex:59: digital dan dokumentasi yang dapat diaudit.
  Contoh: Bab III - Analisis.tex:253: Alur kerja berbasis peristiwa & Perubahan status sebagai pemicu proses & Produsen dan konsumen \textit{event} dengan \textit{payload} yang mengikuti standar & Responsif dan mudah diaudit, tetapi kompleksitas skema \textit{event} harus dijaga \\

- `difokuskan` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:79: Dalam tugas akhir ini, istilah inspeksi kargo difokuskan pada proses
  Contoh: Bab I - Pendahuluan.tex:141: \item Evaluasi tugas akhir ini difokuskan pada kesesuaian rancangan arsitektur
  Contoh: Bab II - Studi.tex:104: Dalam tugas akhir ini, atribut kualitas yang digunakan difokuskan pada

- `diimplementasikan` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:719: yang diimplementasikan di lokasi inspeksi. Pada realisasi saat ini, sumber data
  Contoh: Bab IV - Perancangan.tex:796: Bab ini telah menyajikan desain arsitektur sistem inspeksi kargo digital terintegrasi yang dirancang untuk mengatasi permasalahan yang telah diidentifikasi di Bab III. Desain ini berfokus pada integrasi komponen, pemrosesan responsif, dan konsistensi alur data sebagai dasar realisasi sistem yang diimplementasikan.
  Contoh: Bab V - Implementasi.tex:143: dapat diimplementasikan.

- `diorganisasikan` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:352: lapisan orkestrasi. Komponen sistem diorganisasikan sebagai layanan tematik,
  Contoh: Bab III - Analisis.tex:452: jalur eskalasi yang terdokumentasi. Komponen sistem diorganisasikan mengikuti
  Contoh: Bab IV - Perancangan.tex:198: Sistem diorganisasikan dalam empat lapisan utama: (1) \textbf{\textit{Presentation Layer}} untuk interaksi pengguna melalui aplikasi web, (2) \textbf{\textit{Application Layer}} untuk logika proses inspeksi, autentikasi, dan orkestrasi data melalui layanan API, (3) \textbf{\textit{Data Layer}} untuk penyimpanan data terstruktur dan artefak visual, dan (4) \textbf{\textit{Edge Layer}} untuk akuisisi aliran video, inferensi, dan pengiriman hasil inspeksi dari lapangan.

- `diposisikan` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:61: Kapabilitas di atas diturunkan dari analisis kebutuhan untuk mendukung \textbf{kemudahan pemeliharaan} melalui modularitas, \textbf{interoperabilitas} melalui kontrak layanan yang jelas, \textbf{auditabilitas} melalui ketertelusuran aktivitas, dan \textbf{keandalan operasi}. Pada realisasinya, kapabilitas tersebut diwujudkan melalui pemisahan komponen \textit{edge}, layanan API, aplikasi web, dan lapisan penyimpanan data, sedangkan interoperabilitas dengan sistem eksternal diposisikan sebagai kesiapan perluasan.
  Contoh: Bab IV - Perancangan.tex:141: sinkronisasi ke sistem eksternal diposisikan sebagai arah pengembangan
  Contoh: Bab IV - Perancangan.tex:230: API Ditjen Hubla diposisikan sebagai sasaran integrasi eksternal yang

- `direalisasikan` - muncul 3 kali
  Contoh: 6 Kata Pengantar.tex:25: direalisasikan dalam bentuk implementasi.
  Contoh: Bab I - Pendahuluan.tex:103: memeriksa kesesuaian rancangan terhadap sistem yang direalisasikan sebagai
  Contoh: Bab I - Pendahuluan.tex:142: terhadap sistem yang direalisasikan dan pada validasi integrasi

- `divalidasi` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:129: keparahan agar dapat divalidasi oleh petugas.
  Contoh: Bab IV - Perancangan.tex:878: Pada ruang lingkup tugas akhir, pola ini divalidasi sebagai rancangan sasaran, bukan klaim integrasi eksternal penuh. \\
  Contoh: Bab V - Implementasi.tex:168: Data inspeksi masuk melalui jalur terstruktur dan dapat divalidasi sebelum disimpan. \\

- `draw` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:193: box/.style={rectangle, rounded corners, draw=black, align=center, minimum width=0.78\textwidth, minimum height=0.95cm},
  Contoh: Bab III - Analisis.tex:274: altbox/.style={rectangle, rounded corners, draw=black, align=center, minimum width=3.05cm, minimum height=1.05cm},
  Contoh: Bab III - Analisis.tex:275: chosen/.style={rectangle, rounded corners, draw=black, very thick, align=center, minimum width=3.05cm, minimum height=1.05cm},

- `east` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:364: \draw[line, dashed] (local.east) -- ++(1.1,0) \|- node[flowlabel, pos=0.74, right] {video langsung} (presentation.east);
  Contoh: Bab IV - Perancangan.tex:364: \draw[line, dashed] (local.east) -- ++(1.1,0) \|- node[flowlabel, pos=0.74, right] {video langsung} (presentation.east);
  Contoh: Bab IV - Perancangan.tex:709: \draw[line, dashed] (network.east) -- ++(1.45,0) \|- (cloud.east);

- `entitas` - muncul 3 kali
  Contoh: 13 Daftar Simbol.tex:16: \{id\} & Menunjukkan parameter identitas entitas pada jalur \textit{endpoint} layanan, misalnya identitas kontainer atau sumber daya tertentu. \\
  Contoh: 5 Abstrak.tex:33: pemantauan hasil inspeksi. Pada aspek data, entitas kontainer ditempatkan
  Contoh: 5 Abstrak.tex:40: entitas kontainer melalui OCR, propagasi nomor kontainer ke alur pemindaian

- `eskalasi` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:452: jalur eskalasi yang terdokumentasi. Komponen sistem diorganisasikan mengikuti
  Contoh: Bab IV - Perancangan.tex:946: Validator & Verifikasi hasil deteksi otomatis, penanganan kasus anomali, eskalasi keputusan & Pengetahuan kerusakan kontainer, prosedur penanganan \\
  Contoh: Bab IV - Perancangan.tex:964: sedangkan prosedur operasional mencakup SOP penggunaan sistem, eskalasi

- `evaluation` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:200: \node[box, below=of demo] (evaluation) {Evaluasi kesesuaian rancangan terhadap realisasi dan bukti integrasi};
  Contoh: Bab I - Pendahuluan.tex:206: \draw[line] (demo) -- (evaluation);
  Contoh: Bab I - Pendahuluan.tex:207: \draw[line] (evaluation) -- (communication);

- `false` - muncul 3 kali
  Contoh: TA.tex:240: breakatwhitespace=false,
  Contoh: TA.tex:246: showspaces=false,
  Contoh: TA.tex:247: showstringspaces=false,

- `fitur` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:168: Rincian implementasi model deteksi, pengembangan fitur aplikasi, strategi
  Contoh: Bab V - Implementasi.tex:129: Layer} direalisasikan oleh aplikasi web yang menyediakan fitur pemantauan,
  Contoh: Bab VI - Evaluasi.tex:67: arsitektural, bukan sebagai pengujian seluruh fitur aplikasi atau pengukuran

- `flowlabel` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:352: flowlabel/.style={fill=white, inner sep=1.5pt, font=\small}
  Contoh: Bab IV - Perancangan.tex:363: \draw[line] (local.west) -- ++(-0.85,0) \|- node[flowlabel, pos=0.62, left] {hasil inspeksi} (application.west);
  Contoh: Bab IV - Perancangan.tex:364: \draw[line, dashed] (local.east) -- ++(1.1,0) \|- node[flowlabel, pos=0.74, right] {video langsung} (presentation.east);

- `fondasi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:19: Transformasi menuju pendekatan digital menuntut pemahaman yang mendalam terhadap teori inspeksi kargo, prinsip-prinsip arsitektur sistem, dan kerangka tata kelola yang dapat mendukung operasi yang konsisten, terukur, dan berkelanjutan. Literatur yang ada menyediakan fondasi teoretis yang kuat untuk merancang sistem yang tidak hanya efisien secara teknis tetapi juga sesuai dengan kebutuhan operasional dan regulasi pelabuhan.
  Contoh: Bab II - Studi.tex:98: Prinsip-prinsip ini membentuk fondasi untuk merancang sistem yang tidak hanya efektif secara fungsional tetapi juga dapat dipelihara, dikembangkan, dan diadaptasi sesuai dengan perubahan kebutuhan operasional.
  Contoh: Bab III - Analisis.tex:8: Bab ini menyajikan analisis mendalam terhadap sistem inspeksi kontainer yang ada saat ini, identifikasi kebutuhan sistem, eksplorasi alternatif solusi konseptual, dan justifikasi pemilihan solusi berdasarkan kriteria objektif. Analisis ini menjadi fondasi untuk perancangan arsitektur konseptual yang dipaparkan pada Bab IV.

- `font` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:273: font=\scriptsize,
  Contoh: Bab IV - Perancangan.tex:349: font=\small,
  Contoh: Bab IV - Perancangan.tex:352: flowlabel/.style={fill=white, inner sep=1.5pt, font=\small}

- `height` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:193: box/.style={rectangle, rounded corners, draw=black, align=center, minimum width=0.78\textwidth, minimum height=0.95cm},
  Contoh: Bab III - Analisis.tex:274: altbox/.style={rectangle, rounded corners, draw=black, align=center, minimum width=3.05cm, minimum height=1.05cm},
  Contoh: Bab III - Analisis.tex:275: chosen/.style={rectangle, rounded corners, draw=black, very thick, align=center, minimum width=3.05cm, minimum height=1.05cm},

- `holistik` - muncul 3 kali
  Contoh: Bab II - Studi.tex:234: kelola organisasi. COBIT juga menekankan pendekatan holistik terhadap faktor
  Contoh: Bab II - Studi.tex:339: informasi yang holistik.
  Contoh: Bab III - Analisis.tex:16: Sistem inspeksi kontainer yang berlaku saat ini dapat dianalisis melalui kerangka \textit{People–Process–Technology–Data} untuk memahami komponen utama dan interaksinya. Kerangka ini memungkinkan identifikasi sistematis terhadap keterbatasan pada setiap dimensi, sehingga rancangan solusi dapat merespons seluruh aspek masalah secara holistik.

- `htbp` - muncul 3 kali
  Contoh: Bab II - Studi.tex:131: \begin{figure}[htbp]
  Contoh: Bab III - Analisis.tex:269: \begin{figure}[htbp]
  Contoh: Bab IV - Perancangan.tex:234: \begin{figure}[htbp]

- `http` - muncul 3 kali
  Contoh: 14 Daftar Singkatan.tex:28: HTTP & \textit{Hypertext Transfer Protocol} \\
  Contoh: Bab IV - Perancangan.tex:25: komunikasi diterapkan dengan menggunakan HTTP untuk data terstruktur dan
  Contoh: Bab IV - Perancangan.tex:381: dilakukan secara sinkron melalui HTTP untuk data terstruktur dan

- `iicl` - muncul 3 kali
  Contoh: 14 Daftar Singkatan.tex:30: IICL & \textit{Institute of International Container Lessors} \\
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.

- `implementasinya` - muncul 3 kali
  Contoh: Bab V - Implementasi.tex:194: menyediakan data operasional kepada pengguna. Pada implementasinya, komponen
  Contoh: Bab V - Implementasi.tex:225: Pada implementasinya, aplikasi web membuka koneksi \textit{WebSocket} langsung ke
  Contoh: Bab V - Implementasi.tex:324: muatan yang tercatat. Pada implementasinya, data manifes diisikan melalui

- `inaportnet` - muncul 3 kali
  Contoh: Bab II - Studi.tex:356: komunikasi yang menghubungkan sistem inspeksi dengan Inaportnet, TOS, dan PCS.
  Contoh: Bab III - Analisis.tex:86: \item Data inspeksi masih terisolasi dari sistem TOS, PCS, atau Inaportnet.
  Contoh: Bab III - Analisis.tex:209: & Arsitektur sistem menyediakan batas antarmuka dan pola pertukaran data yang memungkinkan integrasi bertahap dengan berbagai sistem pelabuhan (TOS, PCS, Inaportnet) tanpa mengubah logika inti sistem. \textit{Interface} integrasi dirancang mengikuti format data yang konsisten dan mudah dipetakan ke standar industri logistik. \\

- `independen` - muncul 3 kali
  Contoh: Bab II - Studi.tex:92: \textit{Modularity} mengarahkan sistem agar tersusun dari unit independen yang
  Contoh: Bab II - Studi.tex:151: independen ketika koneksi dengan pusat terganggu. \textit{Scalability}
  Contoh: Bab II - Studi.tex:163: terdekomposisi, \textit{loosely coupled}, dan dapat dikelola secara independen

- `informatika` - muncul 3 kali
  Contoh: 1 Halaman Judul.tex:35: {\large SEKOLAH TEKNIK ELEKTRO DAN INFORMATIKA}\\
  Contoh: 2 Lembar Pengesahan.tex:25: {\large Sekolah Teknik Elektro dan Informatika}\\
  Contoh: 6 Kata Pengantar.tex:9: Studi Sistem dan Teknologi Informasi, Sekolah Teknik Elektro dan Informatika,

- `inkonsistensi` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:58: Ketiadaan standar formal untuk penilaian kerusakan maupun dokumentasi digital yang terintegrasi dengan alur informasi pelabuhan mengakibatkan fragmentasi proses dan inkonsistensi keluaran. Setiap tahapan dilakukan secara manual tanpa dukungan sistem yang memvalidasi kelengkapan atau kebenaran data.
  Contoh: Bab III - Analisis.tex:127: sehingga risiko kesalahan dan inkonsistensi meningkat.
  Contoh: Bab III - Analisis.tex:397: penerapan kontrol akses dan menekan risiko inkonsistensi. Selain itu, strategi

- `inner` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:352: flowlabel/.style={fill=white, inner sep=1.5pt, font=\small}
  Contoh: Bab IV - Perancangan.tex:698: flowlabel/.style={fill=white, inner sep=1.5pt, font=\small}
  Contoh: TA.tex:218: inner=4cm,

- `inspection` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.

- `insw` - muncul 3 kali
  Contoh: 14 Daftar Singkatan.tex:31: INSW & \textit{Indonesia National Single Window} \\
  Contoh: Bab IV - Perancangan.tex:833: karakteristik ekosistem pelabuhan. Sistem eksternal seperti TOS, PCS, dan INSW
  Contoh: Bab V - Implementasi.tex:62: Integrasi operasional penuh dengan TOS, PCS, INSW, atau sistem eksternal pelabuhan lain. \\

- `investigasi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:263: keperluan investigasi atau kepatuhan.
  Contoh: Bab IV - Perancangan.tex:623: juga menekankan jejak audit untuk penelusuran dan investigasi, pemantauan
  Contoh: Bab IV - Perancangan.tex:786: setiap aktivitas dapat ditelusuri untuk keperluan investigasi, penyelesaian

- `justifikasi` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:8: Bab ini menyajikan analisis mendalam terhadap sistem inspeksi kontainer yang ada saat ini, identifikasi kebutuhan sistem, eksplorasi alternatif solusi konseptual, dan justifikasi pemilihan solusi berdasarkan kriteria objektif. Analisis ini menjadi fondasi untuk perancangan arsitektur konseptual yang dipaparkan pada Bab IV.
  Contoh: Bab III - Analisis.tex:539: Berdasarkan matriks evaluasi dan analisis terhadap karakteristik setiap alternatif, \textbf{Alternatif 3: Arsitektur Modular Berbasis Domain} dipilih sebagai solusi yang paling sesuai untuk mengatasi masalah sistem inspeksi kontainer di Indonesia. Justifikasi pemilihan disusun berdasarkan empat perspektif: kebutuhan operasional, atribut kualitas ISO/IEC 25010, prinsip arsitektur, dan kepatuhan terhadap standar dan regulasi.
  Contoh: Bab III - Analisis.tex:592: Berdasarkan justifikasi dari empat perspektif tersebut, arsitektur modular

- `kapabilitas` - muncul 3 kali
  Contoh: Bab II - Studi.tex:152: dipenuhi melalui pusat pemrosesan yang menyediakan kapabilitas elastis untuk
  Contoh: Bab III - Analisis.tex:142: \item Proses belum memiliki kapabilitas untuk menyesuaikan kapasitas
  Contoh: Bab III - Analisis.tex:155: Temuan pada sistem saat ini diterjemahkan menjadi kebutuhan sistem yang merespons celah arsitektural secara langsung. Analisis kebutuhan dibagi menjadi dua kategori: kebutuhan fungsional yang mendefinisikan kapabilitas sistem, dan kebutuhan nonfungsional yang menentukan atribut kualitas agar sistem dapat beroperasi secara andal dalam konteks pelabuhan Indonesia.

- `karakteristik` - muncul 3 kali
  Contoh: Bab II - Studi.tex:41: Tabel \ref{tbl:inspeksi_klasifikasi} menggambarkan empat pendekatan utama inspeksi kargo yang umum digunakan dalam industri logistik. Setiap pendekatan memiliki karakteristik dan aplikasi yang berbeda, dan pemilihan pendekatan yang tepat bergantung pada kebutuhan operasional, regulasi, dan konteks pelabuhan.
  Contoh: Bab II - Studi.tex:49: yaitu seleksi risiko berdasarkan profil data historis, karakteristik pengirim,
  Contoh: Bab II - Studi.tex:73: Pendekatan representasi visual digunakan untuk mengidentifikasi deformasi struktural pada permukaan kontainer melalui analisis pola. Literatur memaparkan konsep ini sebagai proses representasi visual yang digunakan untuk memahami pola dan karakteristik objek secara konsisten.

- `keberlangsungan` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:611: keberlangsungan pemantauan maupun pencatatan data sesuai kondisi layanan yang
  Contoh: Bab VI - Evaluasi.tex:390: pengaturan lalu lintas alat pemindai, keberlangsungan layanan, dan prosedur
  Contoh: Lampiran-B.tex:220: \textit{screening} kontainer, dokumen tingkat layanan dan keberlangsungan layanan alat

- `kepabeanan` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:55: terintegrasi dengan alur kerja pelabuhan dan sistem kepabeanan. Ketiadaan
  Contoh: Bab II - Studi.tex:58: \textit{compliance decision}, yaitu keputusan kepabeanan berdasarkan bukti
  Contoh: Bab II - Studi.tex:275: World Customs Organization SAFE \textit{Framework of Standards} merupakan kerangka kerja internasional untuk mengamankan dan memfasilitasi perdagangan global \autocite{wco2025}. Kerangka ini menyediakan prinsip-prinsip untuk inspeksi kargo berbasis risiko dan pertukaran informasi elektronik antara otoritas kepabeanan.

- `keparahan` - muncul 3 kali
  Contoh: Bab II - Studi.tex:271: Institute of International Container Lessors (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC) menetapkan pedoman klasifikasi kerusakan dan dokumentasi yang menjadi dasar konsistensi penilaian kontainer \autocite{iicl2016, icswsc2023}. Standar ini mendefinisikan pola penilaian kerusakan yang konsisten, kategori kerusakan berdasarkan jenis dan tingkat keparahan, serta pentingnya dokumentasi yang mengikuti standar untuk keperluan audit dan klaim.
  Contoh: Bab III - Analisis.tex:110: formal mengenai kategori kerusakan, tingkat keparahan, atau kriteria keputusan
  Contoh: Bab III - Analisis.tex:177: \textbf{FR-04} & \makecell[l]{Standardisasi\\Proses} & Sistem mendukung representasi hasil penilaian kerusakan berdasarkan kategori dan tingkat keparahan yang konsisten & Tinggi \\

- `keterlacakan` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:79: Dimensi data menunjukkan keterbatasan kualitas dan keterlacakan informasi
  Contoh: Bab III - Analisis.tex:456: kode, dan \textit{lineage} data, sehingga keterlacakan dapat dijaga dari
  Contoh: Bab IV - Perancangan.tex:844: diidentifikasi pada Bab III. Untuk menjaga keterlacakan antara masalah,

- `ketertelusuran` - muncul 3 kali
  Contoh: 5 Abstrak.tex:18: inspeksi yang belum terintegrasi, keterbatasan ketertelusuran bukti inspeksi,
  Contoh: 5 Abstrak.tex:49: Kata kunci: arsitektur sistem, inspeksi kargo digital, integrasi data, pelabuhan, ketertelusuran.
  Contoh: Bab I - Pendahuluan.tex:77: otomasi pemeriksaan, tetapi juga mendukung integrasi data, ketertelusuran

- `klaim` - muncul 3 kali
  Contoh: Bab II - Studi.tex:271: Institute of International Container Lessors (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC) menetapkan pedoman klasifikasi kerusakan dan dokumentasi yang menjadi dasar konsistensi penilaian kontainer \autocite{iicl2016, icswsc2023}. Standar ini mendefinisikan pola penilaian kerusakan yang konsisten, kategori kerusakan berdasarkan jenis dan tingkat keparahan, serta pentingnya dokumentasi yang mengikuti standar untuk keperluan audit dan klaim.
  Contoh: Bab IV - Perancangan.tex:552: sebagai rancangan kesiapan perluasan, bukan sebagai klaim realisasi integrasi
  Contoh: Bab IV - Perancangan.tex:878: Pada ruang lingkup tugas akhir, pola ini divalidasi sebagai rancangan sasaran, bukan klaim integrasi eksternal penuh. \\

- `kompleksitas` - muncul 3 kali
  Contoh: Bab II - Studi.tex:119: \textbf{\textit{Usability}} & \textit{Operability}, \textit{learnability} & Antarmuka dan alur informasi harus mudah dioperasikan oleh pengguna operasional tanpa menambah kompleksitas pemeriksaan \\
  Contoh: Bab III - Analisis.tex:253: Alur kerja berbasis peristiwa & Perubahan status sebagai pemicu proses & Produsen dan konsumen \textit{event} dengan \textit{payload} yang mengikuti standar & Responsif dan mudah diaudit, tetapi kompleksitas skema \textit{event} harus dijaga \\
  Contoh: Bab III - Analisis.tex:371: memelihara kontrak dan katalog pertukaran informasi. Kompleksitas koordinasi

- `komputasi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:145: Konsep \textit{edge-cloud computing} mengacu pada model arsitektur komputasi yang membagi beban pemrosesan antara komponen di lokasi sumber data dan pusat pemrosesan terpusat \autocite{shi2016}. Shi dkk. mendefinisikan \textit{edge computing} sebagai paradigma yang menempatkan komputasi dan penyimpanan data di dekat sumber data untuk mengoptimalkan respons dan efisiensi sistem.
  Contoh: Bab II - Studi.tex:145: Konsep \textit{edge-cloud computing} mengacu pada model arsitektur komputasi yang membagi beban pemrosesan antara komponen di lokasi sumber data dan pusat pemrosesan terpusat \autocite{shi2016}. Shi dkk. mendefinisikan \textit{edge computing} sebagai paradigma yang menempatkan komputasi dan penyimpanan data di dekat sumber data untuk mengoptimalkan respons dan efisiensi sistem.
  Contoh: Bab II - Studi.tex:179: \textit{Computer vision} merupakan bidang yang mempelajari bagaimana sistem komputasi dapat memperoleh pemahaman tingkat tinggi dari citra atau video digital \autocite{szeliski2022}. Prinsip dasar melibatkan transformasi informasi visual mentah menjadi representasi semantik yang dapat digunakan untuk pengambilan keputusan. Konsep ini dipaparkan dalam literatur sebagai pendekatan untuk memahami karakteristik interpretasi visual yang konsisten. Dalam konteks inspeksi kontainer, pendekatan ini relevan karena kerusakan struktural memiliki pola tepi, bentuk, dan tekstur yang dapat dipelajari model secara sistematis.

- `konektivitas` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:500: Keberlanjutan Operasional & Kemampuan untuk menjaga kontinuitas operasional meskipun terjadi gangguan infrastruktur atau konektivitas, serta adaptabilitas terhadap perubahan regulasi. \\
  Contoh: Bab IV - Perancangan.tex:150: melalui layanan API saat konektivitas tersedia.
  Contoh: Bab IV - Perancangan.tex:816: anomali kritis tanpa menunggu respons dari sistem terpusat. Konektivitas

- `labelsep` - muncul 3 kali
  Contoh: TA.tex:282: labelsep=space,
  Contoh: TA.tex:290: labelsep=space,
  Contoh: TA.tex:300: labelsep=space,

- `latensi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:149: mengoptimalkan penggunaan \textit{bandwidth} dan mengurangi latensi.
  Contoh: Bab IV - Perancangan.tex:27: tersebar digunakan untuk menempatkan fungsi yang sensitif terhadap latensi di
  Contoh: Bab IV - Perancangan.tex:678: Gambar \ref{fig:deployment_architecture} menunjukkan distribusi komponen sistem antara perangkat \textit{edge} dan layanan terpusat. Pada sisi \textit{edge}, sistem menjalankan layanan untuk akuisisi aliran video, inferensi, dan siaran video langsung. Pada sisi terpusat, layanan API menangani persistensi dan penyediaan data, MongoDB menyimpan data terstruktur, media penyimpanan objek menyimpan artefak visual, dan aplikasi web menyediakan antarmuka bagi pengguna. Arsitektur ini menempatkan pemrosesan yang sensitif terhadap latensi di dekat sumber data, sementara penyimpanan dan penyajian informasi dipusatkan untuk menjaga konsistensi.

- `latex` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:194: line/.style={-{Latex[length=2mm]}, thick}
  Contoh: Bab III - Analisis.tex:277: line/.style={-{Latex[length=1.8mm]}, thick}
  Contoh: Bab IV - Perancangan.tex:351: line/.style={-{Latex[length=2mm]}, thick},

- `left` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:363: \draw[line] (local.west) -- ++(-0.85,0) \|- node[flowlabel, pos=0.62, left] {hasil inspeksi} (application.west);
  Contoh: Bab V - Implementasi.tex:261: \draw[arrow] (web.north east) -- node[left,font=\scriptsize]{REST} (api.south west);
  Contoh: Bab V - Implementasi.tex:263: \draw[arrow] (tepi.south) -- node[left,font=\scriptsize]{\textit{WebSocket}} (web.north);

- `length` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:194: line/.style={-{Latex[length=2mm]}, thick}
  Contoh: Bab III - Analisis.tex:277: line/.style={-{Latex[length=1.8mm]}, thick}
  Contoh: Bab IV - Perancangan.tex:351: line/.style={-{Latex[length=2mm]}, thick},

- `line` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:194: line/.style={-{Latex[length=2mm]}, thick}
  Contoh: Bab III - Analisis.tex:277: line/.style={-{Latex[length=1.8mm]}, thick}
  Contoh: Bab IV - Perancangan.tex:351: line/.style={-{Latex[length=2mm]}, thick},

- `lines` - muncul 3 kali
  Contoh: 14 Daftar Singkatan.tex:49: SPIL & PT Salam Pacific Indonesia Lines \\
  Contoh: 6 Kata Pengantar.tex:27: Pacific Indonesia Lines (SPIL) yang telah memberikan kesempatan, dukungan,
  Contoh: Lampiran-B.tex:15: Peti Kemas Tanjung Priok PT Salam Pacific Indonesia Lines (SPIL), yang

- `listing` - muncul 3 kali
  Contoh: Bab VI - Evaluasi.tex:178: Struktur layanan API dan bukti data pada entitas kontainer di Listing~\ref{lst:container-entity-sample}. &
  Contoh: Bab VI - Evaluasi.tex:183: Gambar~\ref{fig:evidence_ocr_live} dan Listing~\ref{lst:container-entity-sample}. &
  Contoh: Bab VI - Evaluasi.tex:188: Gambar~\ref{fig:evidence_container_detail} dan struktur \texttt{defectScan}, \texttt{illegalScan}, serta \texttt{categoryScan} pada Listing~\ref{lst:container-entity-sample}. &

- `local` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:357: \node[layerbox] (local) at (0,-4.35) {\textbf{Lapisan \textit{Edge}}\\Akuisisi Video dan Inferensi Awal};
  Contoh: Bab IV - Perancangan.tex:363: \draw[line] (local.west) -- ++(-0.85,0) \|- node[flowlabel, pos=0.62, left] {hasil inspeksi} (application.west);
  Contoh: Bab IV - Perancangan.tex:364: \draw[line, dashed] (local.east) -- ++(1.1,0) \|- node[flowlabel, pos=0.74, right] {video langsung} (presentation.east);

- `manifest` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:450: pemindaian, keputusan sistem, dan lampiran bukti inspeksi. Entitas MANIFEST
  Contoh: Bab IV - Perancangan.tex:467: tugas akhir ini, pusat model data berada pada entitas KONTAINER dan MANIFEST,
  Contoh: Bab V - Implementasi.tex:309: menyimpan identitas kontainer, hasil OCR, ringkasan manifest, hasil pemindaian

- `memetakan` - muncul 3 kali
  Contoh: 5 Abstrak.tex:45: akhir ini adalah rancangan arsitektur yang memetakan pembagian tanggung jawab
  Contoh: Bab II - Studi.tex:71: \textit{Non-Intrusive Inspection} (NII) merupakan konsep pemeriksaan kargo yang memungkinkan pemeriksaan tanpa perlu membuka kontainer. Teknologi NII mencakup pendekatan pencitraan yang dapat memetakan struktur dan isi kontainer secara nondestruktif. Konsep dasar NII didasarkan pada prinsip fisika yang memungkinkan penetrasi material untuk menghasilkan representasi visual dari interior objek tanpa intervensi fisik langsung \autocite{wco2020}.
  Contoh: Bab IV - Perancangan.tex:745: Desain arsitektur sistem inspeksi kargo digital secara eksplisit mempertimbangkan atribut kualitas yang didefinisikan dalam standar ISO/IEC 25010. Tabel~\ref{tbl:iso25010_mapping} memetakan komponen utama arsitektur terhadap atribut kualitas yang didukungnya.

- `memfasilitasi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:275: World Customs Organization SAFE \textit{Framework of Standards} merupakan kerangka kerja internasional untuk mengamankan dan memfasilitasi perdagangan global \autocite{wco2025}. Kerangka ini menyediakan prinsip-prinsip untuk inspeksi kargo berbasis risiko dan pertukaran informasi elektronik antara otoritas kepabeanan.
  Contoh: Bab II - Studi.tex:317: asal-usul informasi dan memfasilitasi audit terhadap proses pengambilan
  Contoh: Bab III - Analisis.tex:73: Tidak ada komponen yang memfasilitasi standardisasi proses, pencatatan digital

- `memvalidasi` - muncul 3 kali
  Contoh: 5 Abstrak.tex:47: inspeksi, dan memvalidasi kesesuaian rancangan terhadap realisasi sistem.
  Contoh: Bab III - Analisis.tex:58: Ketiadaan standar formal untuk penilaian kerusakan maupun dokumentasi digital yang terintegrasi dengan alur informasi pelabuhan mengakibatkan fragmentasi proses dan inkonsistensi keluaran. Setiap tahapan dilakukan secara manual tanpa dukungan sistem yang memvalidasi kelengkapan atau kebenaran data.
  Contoh: Bab V - Implementasi.tex:204: layanan API. Selanjutnya, layanan API memvalidasi, menyimpan, dan memperbarui

- `mendeteksi` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:33: Beberapa pendekatan teknologi sebenarnya sudah mulai diterapkan di industri global. Salah satunya adalah penggunaan kamera termal atau \textit{infrared thermography} yang dapat mendeteksi perbedaan suhu pada permukaan kontainer untuk mengidentifikasi adanya anomali seperti lubang, retakan, atau kebocoran. Metode ini tergolong cepat, tidak merusak objek yang diperiksa, dan cocok untuk \textit{screening} awal. Meski demikian, efektivitas metode ini sangat bergantung pada kondisi lingkungan dan jenis kerusakan. Penyok, korosi awal, atau kerusakan struktural ringan yang tidak memengaruhi suhu sering kali tidak terdeteksi, sehingga hasil inspeksi kurang dapat diandalkan. Selain itu, hasil dari inspeksi termal biasanya belum terintegrasi dengan sistem pelaporan digital yang dapat dilacak secara menyeluruh \autocite{kim2022}.
  Contoh: Bab I - Pendahuluan.tex:35: Di sisi lain, sejumlah operator pelabuhan internasional telah mengembangkan sistem pemindaian otomatis berbasis 3D yang ditempatkan di pintu masuk pelabuhan. Teknologi ini memungkinkan pemetaan bentuk kontainer secara waktu nyata untuk mendeteksi penyok atau kerusakan struktural lain tanpa perlu pemeriksaan manual. Sistem seperti TMEIC DMG 3D, Camco Argus ADI, dan Visy ADDS merupakan beberapa contoh teknologi yang digunakan untuk keperluan ini. Untuk bagian dalam kontainer, teknologi X-ray seperti Leidos VACIS dimanfaatkan untuk memindai isi tanpa perlu membuka kontainer, sehingga anomali isi atau barang ilegal dapat lebih cepat dikenali \autocite{lim2021}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.

- `mengimplementasikan` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:375: aplikasi web. \textbf{\textit{Application Layer}} mengimplementasikan logika proses inspeksi
  Contoh: Bab IV - Perancangan.tex:518: Untuk mengisolasi logika aplikasi inti dari detail implementasi integrasi, rancangan sistem menggunakan \textbf{pola \textit{adapter}}. Setiap sistem eksternal direncanakan memiliki \textit{adapter} khusus yang mengimplementasikan antarmuka standar, sehingga penambahan atau penggantian sistem eksternal dapat dilakukan tanpa mengubah kode aplikasi inti.
  Contoh: Bab IV - Perancangan.tex:682: Sebagai bagian dari penempatan lokal, sistem mengimplementasikan arsitektur \textit{edge} yang berfokus pada akuisisi aliran video dan pemrosesan responsif di lapangan.

- `mengintegrasikan` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:68: yang efektif perlu mampu mengintegrasikan pengambilan data di lapangan,
  Contoh: Bab I - Pendahuluan.tex:87: \item Bagaimana merancang arsitektur sistem yang mampu mengintegrasikan
  Contoh: Bab II - Studi.tex:233: terkait secara menyeluruh, serta mengintegrasikan tata kelola TI dengan tata

- `mengisolasi` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:518: Untuk mengisolasi logika aplikasi inti dari detail implementasi integrasi, rancangan sistem menggunakan \textbf{pola \textit{adapter}}. Setiap sistem eksternal direncanakan memiliki \textit{adapter} khusus yang mengimplementasikan antarmuka standar, sehingga penambahan atau penggantian sistem eksternal dapat dilakukan tanpa mengubah kode aplikasi inti.
  Contoh: Bab IV - Perancangan.tex:619: untuk mengisolasi sistem dari ancaman eksternal, keamanan aplikasi melalui
  Contoh: Bab IV - Perancangan.tex:806: pemeliharaan dengan mengisolasi perubahan pada satu lapisan tanpa memengaruhi

- `merealisasikan` - muncul 3 kali
  Contoh: Bab V - Implementasi.tex:25: Artefak sistem yang digunakan untuk merealisasikan rancangan terdiri atas beberapa komponen utama yang
  Contoh: Bab V - Implementasi.tex:219: Selain jalur data terstruktur, sistem juga merealisasikan jalur video langsung
  Contoh: Bab VI - Evaluasi.tex:51: merealisasikan keputusan arsitektural yang telah dirumuskan pada tahap

- `merespons` - muncul 3 kali
  Contoh: Bab II - Studi.tex:197: Arsitektur berbasis kejadian merupakan pola desain yang membuat komponen sistem berinteraksi melalui notifikasi perubahan status, memungkinkan independensi temporal dan fungsional antara komponen \autocite{hohpe2003}. Dalam pendekatan ini, komponen yang menghasilkan informasi tidak perlu mengetahui komponen mana yang akan merespons informasi tersebut, dan sebaliknya. Konsep ini menciptakan sistem yang lebih fleksibel karena komponen baru dapat ditambahkan untuk merespons kejadian yang sudah ada tanpa mengubah komponen penghasil kejadian. Pendekatan berbasis kejadian ini selaras dengan kebutuhan inspeksi kargo yang memerlukan penelusuran perubahan status kontainer sepanjang alur pemeriksaan secara transparan.
  Contoh: Bab II - Studi.tex:197: Arsitektur berbasis kejadian merupakan pola desain yang membuat komponen sistem berinteraksi melalui notifikasi perubahan status, memungkinkan independensi temporal dan fungsional antara komponen \autocite{hohpe2003}. Dalam pendekatan ini, komponen yang menghasilkan informasi tidak perlu mengetahui komponen mana yang akan merespons informasi tersebut, dan sebaliknya. Konsep ini menciptakan sistem yang lebih fleksibel karena komponen baru dapat ditambahkan untuk merespons kejadian yang sudah ada tanpa mengubah komponen penghasil kejadian. Pendekatan berbasis kejadian ini selaras dengan kebutuhan inspeksi kargo yang memerlukan penelusuran perubahan status kontainer sepanjang alur pemeriksaan secara transparan.
  Contoh: Bab II - Studi.tex:245: operasi untuk merespons permintaan dan menciptakan nilai, \textit{Guiding

- `meskipun` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:42: perlu membuka segelnya. Meskipun teknologi ini meningkatkan efisiensi dan
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:79: Meskipun efektif sebagai \textit{screening} awal ketika terdapat perbedaan temperatur signifikan, IRT memiliki keterbatasan teoretis: kerusakan nontermal sering kali tidak terdeteksi karena tidak menghasilkan kontras temperatur yang memadai. Emisivitas permukaan, jarak pemindaian, dan kondisi lingkungan dapat memengaruhi akurasi hasil secara signifikan sehingga metode ini umumnya digunakan sebagai pelengkap metode inspeksi lainnya.

- `modularitas` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:252: Modular berbasis domain & Pemisahan tanggung jawab berdasarkan domain inspeksi & Modul akuisisi, analisis, otorisasi, pelaporan, dan integrasi dengan antarmuka jelas & Seimbang untuk modularitas, evolusi sistem, dan integrasi bertahap \\
  Contoh: Bab III - Analisis.tex:383: jelas, mengikuti prinsip modularitas dan \textit{loose coupling}
  Contoh: Bab III - Analisis.tex:407: dependensinya. Jika disiplin arsitektural melemah, modularitas dapat berubah

- `network` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:702: \node[group] (network) at (0,-1.45) {\textbf{Jaringan}\\HTTP untuk data terstruktur dan kanal video langsung};
  Contoh: Bab IV - Perancangan.tex:707: \draw[line] (local.north) -- (network.south);
  Contoh: Bab IV - Perancangan.tex:708: \draw[line] (network.north) -- (cloud.south);

- `node` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:192: node distance=0.8cm,
  Contoh: Bab IV - Perancangan.tex:363: \draw[line] (local.west) -- ++(-0.85,0) \|- node[flowlabel, pos=0.62, left] {hasil inspeksi} (application.west);
  Contoh: Bab IV - Perancangan.tex:364: \draw[line, dashed] (local.east) -- ++(1.1,0) \|- node[flowlabel, pos=0.74, right] {video langsung} (presentation.east);

- `north` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:359: \draw[line] ([xshift=-1.25cm]application.north) -- ([xshift=-1.25cm]presentation.south);
  Contoh: Bab IV - Perancangan.tex:361: \draw[line] ([xshift=1.35cm]application.south) -- ([xshift=1.35cm]data.north);
  Contoh: Bab IV - Perancangan.tex:706: \draw[line] (sensor.north) -- (local.south);

- `objective` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:197: \node[box, below=of problem] (objective) {Penetapan tujuan perancangan arsitektur sistem};
  Contoh: Bab I - Pendahuluan.tex:203: \draw[line] (problem) -- (objective);
  Contoh: Bab I - Pendahuluan.tex:204: \draw[line] (objective) -- (design);

- `observasi` - muncul 3 kali
  Contoh: Lampiran-B.tex:72: Berdasarkan observasi lapangan pada kedua lokasi tersebut, diperoleh beberapa
  Contoh: Lampiran-B.tex:88: Hasil observasi pada kunjungan ke terminal menunjukkan bahwa alur masuk
  Contoh: Lampiran-B.tex:106: Observasi lapangan juga menunjukkan bahwa pemeriksaan fisik bagian luar

- `optimalisasi` - muncul 3 kali
  Contoh: 1 Halaman Judul.tex:7: {\Large\bfseries PERANCANGAN ARSITEKTUR SISTEM INSPEKSI KARGO DIGITAL TERINTEGRASI UNTUK OPTIMALISASI PROSES PEMERIKSAAN KONTAINER DI PELABUHAN}\\
  Contoh: 2 Lembar Pengesahan.tex:7: {\large\bfseries PERANCANGAN ARSITEKTUR SISTEM INSPEKSI KARGO DIGITAL TERINTEGRASI UNTUK OPTIMALISASI PROSES PEMERIKSAAN KONTAINER DI PELABUHAN}\\
  Contoh: 6 Kata Pengantar.tex:7: untuk Optimalisasi Proses Pemeriksaan Kontainer di Pelabuhan''. Laporan ini disusun

- `organization` - muncul 3 kali
  Contoh: Bab II - Studi.tex:15: Inspeksi kargo merupakan elemen krusial dalam rantai logistik global yang menjamin keamanan, kepatuhan regulasi, dan integritas barang dalam perdagangan internasional. Menurut World Customs Organization (WCO), inspeksi kargo yang efektif mencegah penyalahgunaan perdagangan, melindungi keamanan publik, dan mendukung kelancaran alur barang di perbatasan \autocite{worldbank2023}. Dalam konteks Indonesia, proses inspeksi kontainer di pelabuhan masih menghadapi tantangan signifikan terkait efisiensi, akurasi, dan integrasi sistem \autocite{pwc2023, crifasia2023}.
  Contoh: Bab II - Studi.tex:23: World Customs Organization (WCO) mengklasifikasikan metode inspeksi kargo ke dalam beberapa kategori berdasarkan tingkat intrusivitas dan prinsip dasar teknologi yang digunakan \autocite{wco2020}. Klasifikasi ini penting untuk memahami dampak operasional, biaya, dan kelayakan pendekatan inspeksi dalam konteks pelabuhan.
  Contoh: Bab II - Studi.tex:45: World Customs Organization SAFE \textit{Framework} 2025 menganjurkan pendekatan

- `otoritas` - muncul 3 kali
  Contoh: Bab II - Studi.tex:275: World Customs Organization SAFE \textit{Framework of Standards} merupakan kerangka kerja internasional untuk mengamankan dan memfasilitasi perdagangan global \autocite{wco2025}. Kerangka ini menyediakan prinsip-prinsip untuk inspeksi kargo berbasis risiko dan pertukaran informasi elektronik antara otoritas kepabeanan.
  Contoh: Bab IV - Perancangan.tex:206: pengelola terminal, otoritas, dan sistem informasi lain di lingkungan
  Contoh: Bab IV - Perancangan.tex:255: inspeksi untuk mendukung keputusan operasional. Otoritas pemerintah

- `pacific` - muncul 3 kali
  Contoh: 14 Daftar Singkatan.tex:49: SPIL & PT Salam Pacific Indonesia Lines \\
  Contoh: 6 Kata Pengantar.tex:27: Pacific Indonesia Lines (SPIL) yang telah memberikan kesempatan, dukungan,
  Contoh: Lampiran-B.tex:15: Peti Kemas Tanjung Priok PT Salam Pacific Indonesia Lines (SPIL), yang

- `pelacakan` - muncul 3 kali
  Contoh: 13 Daftar Simbol.tex:19: $[\,]$ & Menunjukkan himpunan atau daftar elemen, misalnya kumpulan objek hasil pelacakan pada \textit{payload} data terstruktur. \\
  Contoh: Bab I - Pendahuluan.tex:62: digital, pelacakan inspeksi, dan standar operasional yang konsisten, potensi
  Contoh: Bab I - Pendahuluan.tex:91: hasil inspeksi, pelacakan riwayat, dan penyediaan bukti inspeksi dapat

- `pelaporan` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:33: Beberapa pendekatan teknologi sebenarnya sudah mulai diterapkan di industri global. Salah satunya adalah penggunaan kamera termal atau \textit{infrared thermography} yang dapat mendeteksi perbedaan suhu pada permukaan kontainer untuk mengidentifikasi adanya anomali seperti lubang, retakan, atau kebocoran. Metode ini tergolong cepat, tidak merusak objek yang diperiksa, dan cocok untuk \textit{screening} awal. Meski demikian, efektivitas metode ini sangat bergantung pada kondisi lingkungan dan jenis kerusakan. Penyok, korosi awal, atau kerusakan struktural ringan yang tidak memengaruhi suhu sering kali tidak terdeteksi, sehingga hasil inspeksi kurang dapat diandalkan. Selain itu, hasil dari inspeksi termal biasanya belum terintegrasi dengan sistem pelaporan digital yang dapat dilacak secara menyeluruh \autocite{kim2022}.
  Contoh: Bab I - Pendahuluan.tex:61: audit, pelaporan, maupun koordinasi antarinstansi. Tanpa dukungan pencatatan
  Contoh: Bab II - Studi.tex:291: informasi elektronik untuk pelaporan dan pemrosesan kapal dan barang,

- `pelindo` - muncul 3 kali
  Contoh: 6 Kata Pengantar.tex:26: \item Pihak Terminal Pelindo Peti Kemas Tanjung Priok serta pihak PT Salam
  Contoh: Lampiran-B.tex:13: konteks tugas akhir. Lokasi pertama adalah Terminal Pelindo Peti Kemas Tanjung
  Contoh: Lampiran-B.tex:193: \textbf{Lokasi} & Terminal Pelindo Peti Kemas Tanjung Priok \\ \addlinespace

- `pemangku` - muncul 3 kali
  Contoh: Bab II - Studi.tex:232: kebutuhan pemangku kepentingan yang beragam, mencakup organisasi dan ekosistem
  Contoh: Bab II - Studi.tex:324: menjadi relevan khususnya dalam sistem yang melibatkan banyak pemangku
  Contoh: Bab II - Studi.tex:375: melibatkan banyak pemangku kepentingan.

- `pemantauan` - muncul 3 kali
  Contoh: 5 Abstrak.tex:33: pemantauan hasil inspeksi. Pada aspek data, entitas kontainer ditempatkan
  Contoh: Bab II - Studi.tex:36: \textbf{\textit{Sensor-Based Inspection}} & Penggunaan sensor untuk deteksi anomali berbasis parameter fisik & Dapat memberikan pemantauan waktu nyata, tetapi sensitif terhadap kondisi lingkungan \\
  Contoh: Bab III - Analisis.tex:439: data sulit dijaga. Organisasi juga perlu menyiapkan mekanisme pemantauan untuk

- `pemindai` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:39: gamma, atau pemindai sejenis sebagaimana diatur dalam Peraturan Direktur
  Contoh: Bab I - Pendahuluan.tex:40: Jenderal Bea dan Cukai PER-1/BC/2023. Teknologi pemindai lain, seperti
  Contoh: Bab VI - Evaluasi.tex:389: lapangan yang nyata. Dokumen lapangan terkait assessment alat pemindai,

- `pemrosesan` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:96: \item Bagaimana merancang pembagian fungsi antarkomponen agar pemrosesan
  Contoh: Bab I - Pendahuluan.tex:122: \item Merancang pembagian fungsi antarkomponen agar pemrosesan lokal,
  Contoh: Bab II - Studi.tex:145: Konsep \textit{edge-cloud computing} mengacu pada model arsitektur komputasi yang membagi beban pemrosesan antara komponen di lokasi sumber data dan pusat pemrosesan terpusat \autocite{shi2016}. Shi dkk. mendefinisikan \textit{edge computing} sebagai paradigma yang menempatkan komputasi dan penyimpanan data di dekat sumber data untuk mengoptimalkan respons dan efisiensi sistem.

- `pencitraan` - muncul 3 kali
  Contoh: Bab II - Studi.tex:34: \textbf{\textit{Non-Intrusive Inspection} (NII)} & Penggunaan teknologi pencitraan tanpa membuka kontainer untuk memeriksa isi dan struktur & Efisien waktu, dapat diotomatisasi, tetapi memerlukan investasi infrastruktur besar \\
  Contoh: Bab II - Studi.tex:69: \subsection{Konsep \textit{Non-Intrusive Inspection} (NII) dan Pencitraan}
  Contoh: Bab II - Studi.tex:71: \textit{Non-Intrusive Inspection} (NII) merupakan konsep pemeriksaan kargo yang memungkinkan pemeriksaan tanpa perlu membuka kontainer. Teknologi NII mencakup pendekatan pencitraan yang dapat memetakan struktur dan isi kontainer secara nondestruktif. Konsep dasar NII didasarkan pada prinsip fisika yang memungkinkan penetrasi material untuk menghasilkan representasi visual dari interior objek tanpa intervensi fisik langsung \autocite{wco2020}.

- `pengoperasian` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:929: Pengoperasian sistem membutuhkan beberapa peran dengan kompetensi yang sesuai
  Contoh: Bab IV - Perancangan.tex:945: Operator Inspeksi & Pengoperasian perangkat inspeksi, inisiasi proses inspeksi, validasi hasil deteksi & Prosedur inspeksi, pengoperasian perangkat \\
  Contoh: Bab IV - Perancangan.tex:945: Operator Inspeksi & Pengoperasian perangkat inspeksi, inisiasi proses inspeksi, validasi hasil deteksi & Prosedur inspeksi, pengoperasian perangkat \\

- `peninjauan` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:454: kepemilikan atau peninjauan data inspeksi.
  Contoh: Bab V - Implementasi.tex:162: Aplikasi web untuk pemantauan, peninjauan hasil, dan pelaporan inspeksi &
  Contoh: Bab V - Implementasi.tex:331: mendukung autentikasi, otorisasi, dan peninjauan hasil inspeksi melalui aplikasi

- `penyajian` - muncul 3 kali
  Contoh: 5 Abstrak.tex:24: dan penyajian informasi secara terpadu.
  Contoh: 5 Abstrak.tex:41: lain, penyimpanan hasil inspeksi pada model data inti, dan penyajian hasil pada
  Contoh: Bab I - Pendahuluan.tex:69: analisis visual, penyimpanan hasil inspeksi, serta penyajian informasi kepada

- `penyiaran` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:379: awal, dan penyiaran video langsung. Diagram ini menggambarkan struktur
  Contoh: Bab IV - Perancangan.tex:475: Komunikasi antarkomponen menggunakan dua bentuk utama, yaitu pertukaran data terstruktur melalui HTTP dan penyiaran video langsung melalui \textit{WebSocket}. Setiap komunikasi membawa \textit{metadata} identifikasi, waktu, dan data yang relevan dengan proses inspeksi.
  Contoh: Bab IV - Perancangan.tex:481: penyiaran \textit{frame} beranotasi dari \textit{edge} ke aplikasi web untuk

- `persisten` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:416: tetapi juga menunjukkan alasan pemisahan jalur antara data persisten dan video
  Contoh: Bab IV - Perancangan.tex:906: Menyatukan video dan data persisten membuat layanan API menanggung beban yang tidak sesuai dengan fungsi utamanya &
  Contoh: Bab V - Implementasi.tex:210: data operasional yang bersifat persisten tetap melalui layanan API sehingga

- `presentasi` - muncul 3 kali
  Contoh: 5 Abstrak.tex:29: disusun dengan pendekatan berlapis yang mencakup lapisan presentasi, aplikasi,
  Contoh: Bab IV - Perancangan.tex:290: dikelompokkan sebagai lapisan presentasi. Kedua, kebutuhan koordinasi proses,
  Contoh: Bab IV - Perancangan.tex:804: pemisahan tanggung jawab yang jelas antara lapisan presentasi, aplikasi, data,

- `presentation` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:354: \node[layerbox] (presentation) at (0,0) {\textbf{Lapisan Presentasi}\\Aplikasi Web dan Antarmuka Pengguna};
  Contoh: Bab IV - Perancangan.tex:359: \draw[line] ([xshift=-1.25cm]application.north) -- ([xshift=-1.25cm]presentation.south);
  Contoh: Bab IV - Perancangan.tex:364: \draw[line, dashed] (local.east) -- ++(1.1,0) \|- node[flowlabel, pos=0.74, right] {video langsung} (presentation.east);

- `priok` - muncul 3 kali
  Contoh: 6 Kata Pengantar.tex:26: \item Pihak Terminal Pelindo Peti Kemas Tanjung Priok serta pihak PT Salam
  Contoh: Lampiran-B.tex:14: Priok, yang dikunjungi pada tanggal 3 Februari 2026. Lokasi kedua adalah Depo
  Contoh: Lampiran-B.tex:15: Peti Kemas Tanjung Priok PT Salam Pacific Indonesia Lines (SPIL), yang

- `quran` - muncul 3 kali
  Contoh: 1 Halaman Judul.tex:18: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 2 Lembar Pengesahan.tex:18: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 5 Abstrak.tex:10: Aththariq Lisan Quran Daulah Sentono\\

- `realisasinya` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:61: Kapabilitas di atas diturunkan dari analisis kebutuhan untuk mendukung \textbf{kemudahan pemeliharaan} melalui modularitas, \textbf{interoperabilitas} melalui kontrak layanan yang jelas, \textbf{auditabilitas} melalui ketertelusuran aktivitas, dan \textbf{keandalan operasi}. Pada realisasinya, kapabilitas tersebut diwujudkan melalui pemisahan komponen \textit{edge}, layanan API, aplikasi web, dan lapisan penyimpanan data, sedangkan interoperabilitas dengan sistem eksternal diposisikan sebagai kesiapan perluasan.
  Contoh: Bab V - Implementasi.tex:276: Pada realisasinya, ketika aliran OCR berhasil mendeteksi nomor kontainer,
  Contoh: Bab VI - Evaluasi.tex:41: realisasinya terhadap kebutuhan sistem. Artefak utama yang digunakan sebagai

- `rectangle` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:193: box/.style={rectangle, rounded corners, draw=black, align=center, minimum width=0.78\textwidth, minimum height=0.95cm},
  Contoh: Bab III - Analisis.tex:274: altbox/.style={rectangle, rounded corners, draw=black, align=center, minimum width=3.05cm, minimum height=1.05cm},
  Contoh: Bab III - Analisis.tex:275: chosen/.style={rectangle, rounded corners, draw=black, very thick, align=center, minimum width=3.05cm, minimum height=1.05cm},

- `regulasi` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab I - Pendahuluan.tex:70: operator dan sistem lain di lingkungan pelabuhan. Selain itu, regulasi seperti
  Contoh: Bab I - Pendahuluan.tex:222: untuk memperoleh landasan teoretis, standar industri, regulasi, dan kebutuhan

- `responsif` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:253: Alur kerja berbasis peristiwa & Perubahan status sebagai pemicu proses & Produsen dan konsumen \textit{event} dengan \textit{payload} yang mengikuti standar & Responsif dan mudah diaudit, tetapi kompleksitas skema \textit{event} harus dijaga \\
  Contoh: Bab IV - Perancangan.tex:51: Penyajian Informasi & Kemampuan menyajikan informasi kepada pengguna melalui antarmuka yang intuitif dan responsif \\
  Contoh: Bab IV - Perancangan.tex:682: Sebagai bagian dari penempatan lokal, sistem mengimplementasikan arsitektur \textit{edge} yang berfokus pada akuisisi aliran video dan pemrosesan responsif di lapangan.

- `rest` - muncul 3 kali
  Contoh: 14 Daftar Singkatan.tex:44: REST & \textit{Representational State Transfer} \\
  Contoh: Bab IV - Perancangan.tex:360: \node[flowlabel] at (-2.1,-0.72) {REST};
  Contoh: Bab V - Implementasi.tex:261: \draw[arrow] (web.north east) -- node[left,font=\scriptsize]{REST} (api.south west);

- `rounded` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:193: box/.style={rectangle, rounded corners, draw=black, align=center, minimum width=0.78\textwidth, minimum height=0.95cm},
  Contoh: Bab III - Analisis.tex:274: altbox/.style={rectangle, rounded corners, draw=black, align=center, minimum width=3.05cm, minimum height=1.05cm},
  Contoh: Bab III - Analisis.tex:275: chosen/.style={rectangle, rounded corners, draw=black, very thick, align=center, minimum width=3.05cm, minimum height=1.05cm},

- `safe` - muncul 3 kali
  Contoh: 14 Daftar Singkatan.tex:46: SAFE & \textit{Standards to Secure and Facilitate Global Trade} \\
  Contoh: Bab II - Studi.tex:45: World Customs Organization SAFE \textit{Framework} 2025 menganjurkan pendekatan
  Contoh: Bab II - Studi.tex:275: World Customs Organization SAFE \textit{Framework of Standards} merupakan kerangka kerja internasional untuk mengamankan dan memfasilitasi perdagangan global \autocite{wco2025}. Kerangka ini menyediakan prinsip-prinsip untuk inspeksi kargo berbasis risiko dan pertukaran informasi elektronik antara otoritas kepabeanan.

- `sentono` - muncul 3 kali
  Contoh: 1 Halaman Judul.tex:18: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 2 Lembar Pengesahan.tex:18: {\large Aththariq Lisan Quran Daulah Sentono}\\
  Contoh: 5 Abstrak.tex:10: Aththariq Lisan Quran Daulah Sentono\\

- `skalabilitas` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:432: tertentu tanpa keterikatan kuat pada modul internal, sehingga skalabilitas dan
  Contoh: Bab IV - Perancangan.tex:15: arsitektur yang mengedepankan modularitas, skalabilitas, dan keamanan.
  Contoh: Bab IV - Perancangan.tex:116: skalabilitas.

- `south` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:359: \draw[line] ([xshift=-1.25cm]application.north) -- ([xshift=-1.25cm]presentation.south);
  Contoh: Bab IV - Perancangan.tex:361: \draw[line] ([xshift=1.35cm]application.south) -- ([xshift=1.35cm]data.north);
  Contoh: Bab IV - Perancangan.tex:706: \draw[line] (sensor.north) -- (local.south);

- `space` - muncul 3 kali
  Contoh: TA.tex:282: labelsep=space,
  Contoh: TA.tex:290: labelsep=space,
  Contoh: TA.tex:300: labelsep=space,

- `spil` - muncul 3 kali
  Contoh: 14 Daftar Singkatan.tex:49: SPIL & PT Salam Pacific Indonesia Lines \\
  Contoh: 6 Kata Pengantar.tex:27: Pacific Indonesia Lines (SPIL) yang telah memberikan kesempatan, dukungan,
  Contoh: Lampiran-B.tex:15: Peti Kemas Tanjung Priok PT Salam Pacific Indonesia Lines (SPIL), yang

- `style` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:193: box/.style={rectangle, rounded corners, draw=black, align=center, minimum width=0.78\textwidth, minimum height=0.95cm},
  Contoh: Bab I - Pendahuluan.tex:194: line/.style={-{Latex[length=2mm]}, thick}
  Contoh: Bab III - Analisis.tex:274: altbox/.style={rectangle, rounded corners, draw=black, align=center, minimum width=3.05cm, minimum height=1.05cm},

- `subjektivitas` - muncul 3 kali
  Contoh: Bab II - Studi.tex:35: \textbf{\textit{Visual-Mechanical Inspection}} & Pemeriksaan struktur kontainer menggunakan panduan standar industri & Relatif cepat dan murah, tetapi bergantung pada subjektivitas dan pengalaman petugas \\
  Contoh: Bab III - Analisis.tex:87: \item Interpretasi hasil inspeksi bergantung pada subjektivitas petugas
  Contoh: Bab III - Analisis.tex:112: \item Subjektivitas hasil inspeksi tinggi karena penilaian masih bergantung

- `terdefinisi` - muncul 3 kali
  Contoh: Bab II - Studi.tex:94: menekan ketergantungan antarkomponen melalui antarmuka yang terdefinisi dengan
  Contoh: Bab II - Studi.tex:168: \textit{contract-based communication}, yaitu antarmuka yang terdefinisi secara
  Contoh: Bab II - Studi.tex:355: terdefinisi secara spesifik, terutama untuk standar antarmuka dan protokol

- `terdokumentasi` - muncul 3 kali
  Contoh: 5 Abstrak.tex:43: mendukung proses pemeriksaan kontainer yang lebih terstruktur, terdokumentasi,
  Contoh: Bab III - Analisis.tex:174: \textbf{FR-01} & \makecell[l]{Pencatatan\\Inspeksi} & Sistem mencatat hasil inspeksi berdasarkan standar formal yang terdokumentasi & Tinggi \\
  Contoh: Bab III - Analisis.tex:320: dengan aturan transisi status dan definisi peran aktor yang terdokumentasi.

- `terkonsolidasi` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:645: volume operasi, data terkonsolidasi dapat disimpan secara berkelanjutan,
  Contoh: Bab VI - Evaluasi.tex:476: \textit{manual review}, dan lampiran bukti visual memang terkonsolidasi pada
  Contoh: Lampiran-B.tex:293: terkonsolidasi pada satu entitas kontainer. Demi menjaga kerahasiaan, sebagian

- `terorkestrasi` - muncul 3 kali
  Contoh: Bab III - Analisis.tex:251: Integrasi terorkestrasi & Pertukaran informasi antarsistem & Layanan tematik yang dikoordinasikan oleh lapisan orkestrasi & Kuat untuk interoperabilitas, tetapi membutuhkan tata kelola kontrak layanan yang ketat \\
  Contoh: Bab III - Analisis.tex:360: Keunggulan pendekatan integrasi terorkestrasi terletak pada kemampuannya
  Contoh: Bab III - Analisis.tex:523: 2. Integrasi Terorkestrasi & 3 & 4 & 3 & 3 & 3 & 16 \\

- `thick` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:194: line/.style={-{Latex[length=2mm]}, thick}
  Contoh: Bab III - Analisis.tex:275: chosen/.style={rectangle, rounded corners, draw=black, very thick, align=center, minimum width=3.05cm, minimum height=1.05cm},
  Contoh: Bab III - Analisis.tex:277: line/.style={-{Latex[length=1.8mm]}, thick}

- `transaksional` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:48: Penyimpanan Data Terstruktur & Kemampuan menyimpan data transaksional dan master dengan menjaga konsistensi dan integritas informasi \\
  Contoh: Bab IV - Perancangan.tex:335: transaksional dan data master, sedangkan \textit{file storage} digunakan untuk
  Contoh: Bab IV - Perancangan.tex:397: respons langsung dan bersifat transaksional. Pola ini mendukung operasi yang

- `true` - muncul 3 kali
  Contoh: TA.tex:150: colorlinks=true,
  Contoh: TA.tex:241: breaklines=true,
  Contoh: TA.tex:243: keepspaces=true,

- `ucirc` - muncul 3 kali
  Contoh: 14 Daftar Singkatan.tex:53: UCIRC & \textit{Unified Container Inspection and Repair Criteria} \\
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.

- `validasi` - muncul 3 kali
  Contoh: 5 Abstrak.tex:20: tersebut menyebabkan proses verifikasi kontainer, validasi manifes, dan
  Contoh: Bab I - Pendahuluan.tex:142: terhadap sistem yang direalisasikan dan pada validasi integrasi
  Contoh: Bab I - Pendahuluan.tex:171: tersebut sebagai bahan demonstrasi dan validasi rancangan arsitektur. Dengan

- `west` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:363: \draw[line] (local.west) -- ++(-0.85,0) \|- node[flowlabel, pos=0.62, left] {hasil inspeksi} (application.west);
  Contoh: Bab IV - Perancangan.tex:363: \draw[line] (local.west) -- ++(-0.85,0) \|- node[flowlabel, pos=0.62, left] {hasil inspeksi} (application.west);
  Contoh: Bab V - Implementasi.tex:261: \draw[arrow] (web.north east) -- node[left,font=\scriptsize]{REST} (api.south west);

- `width` - muncul 3 kali
  Contoh: Bab I - Pendahuluan.tex:193: box/.style={rectangle, rounded corners, draw=black, align=center, minimum width=0.78\textwidth, minimum height=0.95cm},
  Contoh: Bab III - Analisis.tex:274: altbox/.style={rectangle, rounded corners, draw=black, align=center, minimum width=3.05cm, minimum height=1.05cm},
  Contoh: Bab III - Analisis.tex:275: chosen/.style={rectangle, rounded corners, draw=black, very thick, align=center, minimum width=3.05cm, minimum height=1.05cm},

- `world` - muncul 3 kali
  Contoh: Bab II - Studi.tex:15: Inspeksi kargo merupakan elemen krusial dalam rantai logistik global yang menjamin keamanan, kepatuhan regulasi, dan integritas barang dalam perdagangan internasional. Menurut World Customs Organization (WCO), inspeksi kargo yang efektif mencegah penyalahgunaan perdagangan, melindungi keamanan publik, dan mendukung kelancaran alur barang di perbatasan \autocite{worldbank2023}. Dalam konteks Indonesia, proses inspeksi kontainer di pelabuhan masih menghadapi tantangan signifikan terkait efisiensi, akurasi, dan integrasi sistem \autocite{pwc2023, crifasia2023}.
  Contoh: Bab II - Studi.tex:23: World Customs Organization (WCO) mengklasifikasikan metode inspeksi kargo ke dalam beberapa kategori berdasarkan tingkat intrusivitas dan prinsip dasar teknologi yang digunakan \autocite{wco2020}. Klasifikasi ini penting untuk memahami dampak operasional, biaya, dan kelayakan pendekatan inspeksi dalam konteks pelabuhan.
  Contoh: Bab II - Studi.tex:45: World Customs Organization SAFE \textit{Framework} 2025 menganjurkan pendekatan

- `xshift` - muncul 3 kali
  Contoh: Bab IV - Perancangan.tex:359: \draw[line] ([xshift=-1.25cm]application.north) -- ([xshift=-1.25cm]presentation.south);
  Contoh: Bab IV - Perancangan.tex:359: \draw[line] ([xshift=-1.25cm]application.north) -- ([xshift=-1.25cm]presentation.south);
  Contoh: Bab IV - Perancangan.tex:361: \draw[line] ([xshift=1.35cm]application.south) -- ([xshift=1.35cm]data.north);

- `antarbagian` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:405: ketidaksesuaian antarbagian sistem. Pendekatan ini juga menuntut dokumentasi
  Contoh: Bab IV - Perancangan.tex:873: Pemisahan tanggung jawab mengurangi ketergantungan langsung antarbagian sistem &

- `antarinstansi` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:61: audit, pelaporan, maupun koordinasi antarinstansi. Tanpa dukungan pencatatan
  Contoh: Bab I - Pendahuluan.tex:73: antarinstansi dan keamanan sistem informasi \autocite{kemenhub2022}.

- `antarproses` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:366: mengelola beban kerja antarproses secara lebih adaptif.
  Contoh: Lampiran-B.tex:78: antarproses belum sepenuhnya berjalan secara terpadu. Ketiga, kebutuhan akan

- `bass` - muncul 2 kali
  Contoh: Bab II - Studi.tex:87: telah dipaparkan oleh Bass, Clements, dan Kazman \autocite{bass2022}. Dalam
  Contoh: Bab II - Studi.tex:211: \autocite{bass2022}. Bass dkk. menekankan bahwa standardisasi antarmuka

- `berevolusi` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:571: \autocite{newman2015}. Setiap domain dapat berevolusi dengan siklus
  Contoh: Bab IV - Perancangan.tex:20: agar setiap komponen memiliki tanggung jawab tunggal dan dapat berevolusi

- `cargovision` - muncul 2 kali
  Contoh: 6 Kata Pengantar.tex:23: \item Rekan satu tim proyek Cargovision yang telah berkolaborasi dalam
  Contoh: Bab IV - Perancangan.tex:228: \item Menetapkan batas sistem dengan menempatkan Cargovision sebagai pusat

- `cctv` - muncul 2 kali
  Contoh: 14 Daftar Singkatan.tex:22: CCTV & \textit{Closed-Circuit Television} \\
  Contoh: Lampiran-B.tex:137: sistem operasional dan infrastruktur pemantauan seperti CCTV, tetapi pemanfaatan

- `communication` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:201: \node[box, below=of evaluation] (communication) {Penyusunan laporan tugas akhir};
  Contoh: Bab I - Pendahuluan.tex:207: \draw[line] (evaluation) -- (communication);

- `dianotasi` - muncul 2 kali
  Contoh: Bab V - Implementasi.tex:97: sudah dianotasi kepada aplikasi web.
  Contoh: Bab V - Implementasi.tex:221: menyajikan \textit{frame} yang telah dianotasi secara waktu nyata. Pemisahan

- `didefinisikan` - muncul 2 kali
  Contoh: Bab IV - Perancangan.tex:745: Desain arsitektur sistem inspeksi kargo digital secara eksplisit mempertimbangkan atribut kualitas yang didefinisikan dalam standar ISO/IEC 25010. Tabel~\ref{tbl:iso25010_mapping} memetakan komponen utama arsitektur terhadap atribut kualitas yang didukungnya.
  Contoh: Bab V - Implementasi.tex:290: lintas modul yang sebelumnya didefinisikan sebagai salah satu kapabilitas

- `dideteksi` - muncul 2 kali
  Contoh: Bab VI - Evaluasi.tex:309: menyebarkan nomor kontainer yang berhasil dideteksi ke aliran lain yang sedang
  Contoh: Bab VI - Evaluasi.tex:383: kontainer berhasil dideteksi pada aliran OCR, sedangkan

- `diintegrasikan` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:612: siap diintegrasikan.
  Contoh: Bab IV - Perancangan.tex:138: diintegrasikan dengan sistem operasional eksternal melalui antarmuka layanan

- `dimodifikasi` - muncul 2 kali
  Contoh: Bab II - Studi.tex:173: Pendekatan ini memungkinkan sistem untuk berkembang secara evolusioner karena komponen dapat dimodifikasi atau diganti tanpa memerlukan perubahan menyeluruh pada sistem. Prinsip ini digunakan dalam literatur untuk menjelaskan pola adaptasi arsitektur terhadap perubahan regulasi dan kebutuhan operasional.
  Contoh: Bab II - Studi.tex:259: \textit{integrity verification} untuk memastikan data tidak dimodifikasi secara

- `dioperasikan` - muncul 2 kali
  Contoh: Bab II - Studi.tex:119: \textbf{\textit{Usability}} & \textit{Operability}, \textit{learnability} & Antarmuka dan alur informasi harus mudah dioperasikan oleh pengguna operasional tanpa menambah kompleksitas pemeriksaan \\
  Contoh: Bab VII - Penutup.tex:53: menyeluruh, kapasitas pemrosesan, dan ketahanan sistem ketika dioperasikan

- `dipropagasikan` - muncul 2 kali
  Contoh: Bab V - Implementasi.tex:277: nomor tersebut secara otomatis dipropagasikan ke aliran lain yang sedang aktif.
  Contoh: Bab VI - Evaluasi.tex:93: deteksi nomor kontainer dari aliran OCR dapat dipropagasikan ke aliran lain,

- `direpresentasikan` - muncul 2 kali
  Contoh: Bab II - Studi.tex:305: yang tercatat dengan kondisi aktual yang direpresentasikan.
  Contoh: Bab III - Analisis.tex:416: analisis temuan, hingga otorisasi, direpresentasikan sebagai \textit{event}

- `edition` - muncul 2 kali
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: TA.tex:132: edition      = {edisi},

- `ekspektasi` - muncul 2 kali
  Contoh: Bab IV - Perancangan.tex:974: Penting untuk menegaskan batasan ruang lingkup desain sistem ini agar ekspektasi
  Contoh: Bab IV - Perancangan.tex:991: Desain arsitektur ini menetapkan kerangka yang memandu realisasi sistem berdasarkan karakteristik operasi pelabuhan dan kebutuhan pemangku kepentingan. Kebutuhan operasional memastikan sistem dapat dijalankan secara berkelanjutan, sedangkan batasan ruang lingkup menjaga fokus desain dan ekspektasi yang realistis terhadap kapabilitas sistem.

- `english` - muncul 2 kali
  Contoh: TA.tex:115: language=english,
  Contoh: TA.tex:118: \DeclareLanguageMapping{indonesian}{english}

- `fill` - muncul 2 kali
  Contoh: Bab IV - Perancangan.tex:352: flowlabel/.style={fill=white, inner sep=1.5pt, font=\small}
  Contoh: Bab IV - Perancangan.tex:698: flowlabel/.style={fill=white, inner sep=1.5pt, font=\small}

- `harmonisasi` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:323: dan \textit{template} inspeksi baku, sehingga harmonisasi proses dan data
  Contoh: Bab III - Analisis.tex:341: adalah harmonisasi internal. Konsolidasi lintas pelabuhan juga belum otomatis

- `implementabel` - muncul 2 kali
  Contoh: Bab VI - Evaluasi.tex:269: memang implementabel dan mendukung tujuan yang telah ditetapkan.
  Contoh: Bab VI - Evaluasi.tex:506: Komponen sistem memiliki tanggung jawab berbeda dan harus tetap dapat berkembang tanpa saling membebani & Komponen \textit{edge}, API, web, dan penyimpanan dipisahkan menurut peran & Skenario integrasi menunjukkan komponen saling terhubung melalui kontrak layanan yang berbeda sesuai tanggung jawabnya & Pembagian lapisan arsitektur terbukti implementabel pada ruang lingkup tugas akhir ini \\

- `implementabilitas` - muncul 2 kali
  Contoh: Bab V - Implementasi.tex:46: direalisasikan sebagai bukti implementabilitas rancangan dan bagian yang tetap
  Contoh: Bab VI - Evaluasi.tex:40: tugas akhir ini, yaitu menilai implementabilitas rancangan arsitektur dan kesesuaian

- `indikator` - muncul 2 kali
  Contoh: Bab VI - Evaluasi.tex:100: tersimpan pada entitas kontainer yang sesuai. Skenario ini menjadi indikator
  Contoh: Bab VI - Evaluasi.tex:160: dibandingkan dengan indikator keberhasilan pada Tabel~\ref{tbl:aspek-evaluasi}.

- `information` - muncul 2 kali
  Contoh: Bab II - Studi.tex:229: COBIT (Control Objectives for Information and Related Technologies) merupakan kerangka kerja tata kelola dan manajemen teknologi informasi yang dikembangkan oleh ISACA \autocite{isaca2019}. COBIT 2019 menyediakan prinsip-prinsip untuk menyelaraskan TI dengan tujuan bisnis organisasi dan memastikan penggunaan teknologi yang efektif dan bertanggung jawab.
  Contoh: Bab II - Studi.tex:242: ITIL (Information Technology Infrastructure Library) merupakan kerangka kerja praktik terbaik untuk manajemen layanan TI yang dikembangkan oleh AXELOS \autocite{axelos2019}. ITIL 4 memperkenalkan konsep \textit{Service Value System} yang menekankan penciptaan nilai melalui layanan TI.

- `institute` - muncul 2 kali
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:271: Institute of International Container Lessors (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC) menetapkan pedoman klasifikasi kerusakan dan dokumentasi yang menjadi dasar konsistensi penilaian kontainer \autocite{iicl2016, icswsc2023}. Standar ini mendefinisikan pola penilaian kerusakan yang konsisten, kategori kerusakan berdasarkan jenis dan tingkat keparahan, serta pentingnya dokumentasi yang mengikuti standar untuk keperluan audit dan klaim.

- `interior` - muncul 2 kali
  Contoh: Bab II - Studi.tex:71: \textit{Non-Intrusive Inspection} (NII) merupakan konsep pemeriksaan kargo yang memungkinkan pemeriksaan tanpa perlu membuka kontainer. Teknologi NII mencakup pendekatan pencitraan yang dapat memetakan struktur dan isi kontainer secara nondestruktif. Konsep dasar NII didasarkan pada prinsip fisika yang memungkinkan penetrasi material untuk menghasilkan representasi visual dari interior objek tanpa intervensi fisik langsung \autocite{wco2020}.
  Contoh: Bab IV - Perancangan.tex:982: Sebaliknya, desain ini tidak mencakup inspeksi interior kontainer, proses

- `international` - muncul 2 kali
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:271: Institute of International Container Lessors (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC) menetapkan pedoman klasifikasi kerusakan dan dokumentasi yang menjadi dasar konsistensi penilaian kontainer \autocite{iicl2016, icswsc2023}. Standar ini mendefinisikan pola penilaian kerusakan yang konsisten, kategori kerusakan berdasarkan jenis dan tingkat keparahan, serta pentingnya dokumentasi yang mengikuti standar untuk keperluan audit dan klaim.

- `json` - muncul 2 kali
  Contoh: 13 Daftar Simbol.tex:20: : & Menunjukkan pemisah antara nama atribut dan nilai pada representasi data terstruktur seperti JSON. \\
  Contoh: 14 Daftar Singkatan.tex:36: JSON & \textit{JavaScript Object Notation} \\

- `keterhubungan` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:78: proses, dan keterhubungan dengan ekosistem digital pelabuhan Indonesia.
  Contoh: Bab V - Implementasi.tex:392: utama bab ini bukan pada rincian kode, melainkan pada keterhubungan antara

- `ketidaksesuaian` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:405: ketidaksesuaian antarbagian sistem. Pendekatan ini juga menuntut dokumentasi
  Contoh: Bab III - Analisis.tex:440: memastikan tidak ada peristiwa yang hilang atau tertunda. Ketidaksesuaian

- `krusial` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:23: satu aspek krusial yang perlu diperhatikan adalah pemeriksaan peti kemas.
  Contoh: Bab II - Studi.tex:15: Inspeksi kargo merupakan elemen krusial dalam rantai logistik global yang menjamin keamanan, kepatuhan regulasi, dan integritas barang dalam perdagangan internasional. Menurut World Customs Organization (WCO), inspeksi kargo yang efektif mencegah penyalahgunaan perdagangan, melindungi keamanan publik, dan mendukung kelancaran alur barang di perbatasan \autocite{worldbank2023}. Dalam konteks Indonesia, proses inspeksi kontainer di pelabuhan masih menghadapi tantangan signifikan terkait efisiensi, akurasi, dan integrasi sistem \autocite{pwc2023, crifasia2023}.

- `kueri` - muncul 2 kali
  Contoh: Bab V - Implementasi.tex:352: Bab IV. Data terstruktur membutuhkan dukungan kueri, pembaruan status, dan
  Contoh: Bab VI - Evaluasi.tex:350: untuk mendukung kueri dan pembaruan status, sedangkan artefak visual disimpan

- `language` - muncul 2 kali
  Contoh: TA.tex:115: language=english,
  Contoh: TA.tex:250: language=Python

- `lessors` - muncul 2 kali
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.
  Contoh: Bab II - Studi.tex:271: Institute of International Container Lessors (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC) menetapkan pedoman klasifikasi kerusakan dan dokumentasi yang menjadi dasar konsistensi penilaian kontainer \autocite{iicl2016, icswsc2023}. Standar ini mendefinisikan pola penilaian kerusakan yang konsisten, kategori kerusakan berdasarkan jenis dan tingkat keparahan, serta pentingnya dokumentasi yang mengikuti standar untuk keperluan audit dan klaim.

- `management` - muncul 2 kali
  Contoh: Bab II - Studi.tex:281: Management}, serta penggunaan teknologi modern untuk inspeksi dan verifikasi
  Contoh: Lampiran-B.tex:202: \textbf{Narasumber} & Sudarmaji Aji (Improvement \& Operational Excellence Project Management, PT Salam Pacific Indonesia Lines) \\ \addlinespace

- `memverifikasi` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:114: \item Belum terdapat komponen sistem yang memverifikasi kelengkapan atau
  Contoh: Bab IV - Perancangan.tex:253: berbeda. Petugas inspeksi lapangan membutuhkan sarana untuk memverifikasi hasil

- `mereduksi` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:328: Pendekatan ini unggul dalam konteks standardisasi karena dapat mereduksi variasi
  Contoh: Bab III - Analisis.tex:361: mereduksi fragmentasi informasi melalui kontrak formal antarlayanan. Titik

- `merepresentasikan` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:222: Atribut kualitas tersebut dipilih karena merepresentasikan faktor kritis keberhasilan sistem inspeksi digital dan selaras dengan prinsip arsitektur sistem terdistribusi yang telah dipaparkan dalam Bab II.
  Contoh: Bab III - Analisis.tex:511: Evaluasi dilakukan dengan penilaian kualitatif yang diterjemahkan menjadi skala numerik 1 hingga 4, merepresentasikan tingkat kesesuaian alternatif dengan setiap kriteria: 1 (sangat rendah), 2 (rendah), 3 (sedang), 4 (tinggi). Tabel~\ref{tbl:evaluasi_alternatif} merangkum hasil evaluasi terhadap kelima alternatif solusi.

- `ncip` - muncul 2 kali
  Contoh: 14 Daftar Singkatan.tex:37: NCIP & \textit{National Container Inspection Program} \\
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.

- `nugraha` - muncul 2 kali
  Contoh: 2 Lembar Pengesahan.tex:37: Ir. I Gusti Bagus Baskara Nugraha, S.T., M.T., Ph.D  \\[0.2cm]
  Contoh: 6 Kata Pengantar.tex:20: \item Ir. I Gusti Bagus Baskara Nugraha, S.T., M.T., Ph.D selaku dosen

- `orisinalitas` - muncul 2 kali
  Contoh: 3 Pernyataan Orisinalitas.tex:1: \chapter*{PERNYATAAN ORISINALITAS}
  Contoh: 3 Pernyataan Orisinalitas.tex:2: \addcontentsline{toc}{chapter}{PERNYATAAN ORISINALITAS}

- `otomasi` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:77: otomasi pemeriksaan, tetapi juga mendukung integrasi data, ketertelusuran
  Contoh: Bab III - Analisis.tex:324: dilakukan terlebih dahulu sebelum integrasi atau otomasi lanjutan dirancang.

- `outer` - muncul 2 kali
  Contoh: TA.tex:219: outer=3cm,
  Contoh: TA.tex:352: outer=3cm,

- `pemicu` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:253: Alur kerja berbasis peristiwa & Perubahan status sebagai pemicu proses & Produsen dan konsumen \textit{event} dengan \textit{payload} yang mengikuti standar & Responsif dan mudah diaudit, tetapi kompleksitas skema \textit{event} harus dijaga \\
  Contoh: Bab IV - Perancangan.tex:217: Bab III, yaitu permohonan atau pemicu pemeriksaan, akuisisi data lapangan,

- `penggabungan` - muncul 2 kali
  Contoh: Bab II - Studi.tex:185: Literatur membedakan pendekatan deteksi berdasarkan organisasi proses analisis visual, yang dapat dilakukan secara bertahap dengan pemisahan tahap analisis awal dari tahap identifikasi objek, atau secara terintegrasi dengan penggabungan kedua proses. Literatur menyoroti adanya pertimbangan antara kedalaman analisis dan efisiensi proses dalam pemilihan pendekatan deteksi visual.
  Contoh: Lampiran-B.tex:347: memungkinkan penggabungan konteks OCR, kerusakan, barang berisiko, klasifikasi

- `penggantian` - muncul 2 kali
  Contoh: Bab IV - Perancangan.tex:518: Untuk mengisolasi logika aplikasi inti dari detail implementasi integrasi, rancangan sistem menggunakan \textbf{pola \textit{adapter}}. Setiap sistem eksternal direncanakan memiliki \textit{adapter} khusus yang mengimplementasikan antarmuka standar, sehingga penambahan atau penggantian sistem eksternal dapat dilakukan tanpa mengubah kode aplikasi inti.
  Contoh: Bab IV - Perancangan.tex:778: lain. Penggunaan antarmuka standar juga memungkinkan penggantian

- `penyunting` - muncul 2 kali
  Contoh: TA.tex:126: editor       = {penyunting},
  Contoh: TA.tex:127: editors      = {penyunting},

- `perekaman` - muncul 2 kali
  Contoh: Bab III - Analisis.tex:353: seperti perekaman data, penilaian, pelaporan, dan koordinasi eksternal, yang
  Contoh: Bab III - Analisis.tex:418: konsumen \textit{event}; misalnya, modul perekaman data menghasilkan

- `point` - muncul 2 kali
  Contoh: Bab I - Pendahuluan.tex:51: Walaupun teknologi-teknologi tersebut telah banyak digunakan secara global, sebagian besar pelabuhan di Indonesia masih bergantung pada metode manual. Petugas biasanya melakukan pemeriksaan berdasarkan \textit{checklist} standar seperti CTPAT 7-Point Container Inspection atau panduan inspeksi dari IICL dan UCIRC. Di tingkat internasional, program inspeksi kontainer yang komprehensif seperti \textit{National Container Inspection Program} (NCIP) milik U.S. Coast Guard mengharuskan inspektur memiliki pengetahuan tentang berbagai kriteria inspeksi dan perbaikan yang banyak digunakan, termasuk panduan dari \textit{Institute of International Container Lessors} (IICL) dan \textit{Unified Container Inspection and Repair Criteria} (UCIRC), untuk memastikan kontainer memenuhi standar keselamatan struktural dan regulasi pengangkutan bahan berbahaya \autocite{uscg2019}.
  Contoh: Bab II - Studi.tex:17: Secara tradisional, inspeksi kontainer dilakukan melalui pemeriksaan manual oleh petugas, menggunakan panduan standar seperti CTPAT 7-Point Container Inspection Checklist dari U.S. Customs and Border Protection \autocite{cbp2022} dan Guide for Container Equipment Inspection 6th Edition dari Institute of International Container Lessors \autocite{iicl2016}. Meskipun metode ini efektif dalam mendeteksi kerusakan visual dan anomali tertentu, pendekatan manual memiliki keterbatasan inheren: konsistensi rendah, tingginya tingkat \textit{human error}, durasi waktu inspeksi yang lama, dan sulit untuk menghasilkan dokumentasi yang mengikuti standar dan dapat dilacak sepenuhnya \autocite{meola2004, crifasia2023}.

- `premis` - muncul 2 kali
  Contoh: Bab VI - Evaluasi.tex:273: \item Premis kebutuhan operasional dan prinsip arsitektur yang menjadi dasar
  Contoh: Bab VI - Evaluasi.tex:451: Berdasarkan premis tersebut, rancangan menetapkan empat keputusan utama:
