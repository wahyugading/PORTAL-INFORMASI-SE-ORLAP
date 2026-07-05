import json
import re

old_qna_text = '''
Q: PPL UB hanya mendata UB yang ada di prelist. Lalu PPL Door To Door mendata UB yang tidak ada di prelist (Sesuai alokasinya). Bagaimana cara Door To Door mengetahui jika UB tersebut sudah di data oleh PPL UB melalui FASIH ?
Saat Pelatihan terdapat di PPT bahwa PPL Door To Door jika menemukan UB hanya geotagging dan submit, berarti tidak dilanjutkan pendataan ya ? Apakah ini
masih sama ?
A: Jika PPL door to door menemukan usaha besar baik yang ada di daftar assigment maupun di menu lookup di wilayah SLS nya ada, maka PPL door to door cukup melakukan geotagging dan menempelkan sticker kemudian submit. Untuk pendataan lengkap usaha/perusahaan tersebut akan dilakukan oleh PPL-UB.
===TOPIC_END===
Q: Pak Barkah mengusahakan padi dan jagung selama 2025 secara berselang-seling, di P akan menjawab Ya pada tanaman pangan. Akan terbentuk rooster
Barkah-Tanaman Pangan. Saat di rincian 13a penentuan KBLI dari nilai produksi terbesar antara padi dan jagung; misal yg terbesar adalah Padi. Pertanyaannya, pengeluaran dan pendapatan usaha pertanian pak barkah hanya berisi pengeluaran dan pendapatan untuk padi saja sesuai KBLI usaha atau termasuk
pengeluaran dan pendapatan padi dan jagung?
A: Seluruh pendapatan dan pengeluaran padi dan jagung
Nilai Produksi dari seluruh hasil panen padi dan  jagung dicatat pada Rincaian 27 a Nilai produksi/penjualan/pendapatan barang dan jasa
Pengeluaran yang dicatat adalah seluruh pengeluaran pada kegiatan penanaman padi dan jagung pada rincian 26 b  Biaya produksi
===TOPIC_END===
Q: Rekomendasi untuk semua survei/sensus yang memanfaatkan FASIH dashboard. Bisa tidak ya dimulai dari SE ini, ada fitur di dashboard untuk melihat rekap per petugas? mengingat, kadang terjadi di survei lain, contohnya GC PBI, rekap petugas itu baru ada setelah ada banyak request dari daerah untuk dimunculkan di dashboard. Sebaiknya, itu jadi standar untuk kegiatan survei/sensus bahwa dashboard itu memfasilitasi untuk bisa melihat rekap per petugas.
A: Noted. Rekap per petugas akan dijadikan standar.
===TOPIC_END===
Q: Untuk jumlah hewan ternak terutama ayam ini apa tidak ada batasannya?karena kalau di desa ini setiap rumah pasti melihara ayam tapi hanya dipelihara untuk jaga-jaga kalau butuh telur atau daging untuk dikonsumsi sendiri tidak sampai dijual
Ini serius kalau ayam misalnya cuma satu dan dia mau mengusahakan dimasukan
?
A: untuk yang memelihara hewan ternak dengan tujuan konsumsi sendiri maka
tidak disebut sebagai usaha peternakan.
Identifikasi awal usaha peternakan yaitu ternak yang masih ada dipelihara pada saat pencacahan, kecuali pada unggas pedaging (ayam kampung pedaging, ayam ras pedaging, itik pedaging, puyuh pedaging) tetap tercakup walaupun pada saat pencacahan sedang tidak ada unggasnya (pengosongan kandang) asalkan masih berencana akan melanjutkan usaha unggas pedagingnya.
===TAGS===#Prosedur Prelisting,#Metodologi
Q: saat ini di salah satu kabupaten/Kota yaitu di Kota Bitung masih belum ada pengesahan Ketua SLS, jadi belum ada ketua SLS yang disahkan untuk satu wilayah Kota Bitungsampe sekarang, pada tahap pengenalan dan Penelusuran Wilayahnya, serta identifikasi SLS seperti apa?, apakah tidak perlu melapor ke ketua SLS nya (kareta tidak ada ketua sls definite) atau dikonfirmasi ke ketua SLS periode sebelumnya atau ke aparat kelurahan saja?, informasinya saat ini belum ada pengurus Untuk semua Tingkatan SLS dibawah Kelurahan, baik itu Lingkungan (RW) maupun sls terkecil (RT)
A: Melapor ke ketua SLS penting dilakukan untuk mengenalkan petugas, sekaligus meminta ijin untuk melakukan pendataan di wilayah (SLS) tersebut, hal ini untuk menghindari terjadinya persepsi negatif dari masyarakat. Jika suatu SLS belum ada Ketua SLSnya (belum ditetapkan), pendekatan yang dilakukan adalah melapor ke SLS di atasnya misal ke Ketua RW/Kampung, dan menanyakan pengurus/pengelola SLS/tokoh masyarakat lainnya yang diberi kewenangan (berpengaruh) untuk ditemui dan meminta ijin melakukan pendataan SE2026.
===TOPIC_END===
Q: Sewaktu NGIBAR, bagaimana menentukan Usaha Menengah (UM)?
tersebut hanya ada di Bangunan Khusus Usaha (BKU), contoh PTSP kebanyakan datanya adalah UMKM dan nama pada list data yang diberikan adalah nama pemiliknya meski sudah ada badan hukum. Tapi jika di probing atau pengecekan baru ketahuan jika dia ada yang tinggal di bangunan tersebut. Mohon konfirmasinya
A: - skala usaha berdasarkan prelist.
===TAGS===#Aplikasi FASIH,#Sistem
Q: dari penjelasan bu Puji menyebutkan bahwa anak sementara sekolah namun tidak tinggal bersama dengan keluarga dipilih kode 3 tidak tinggal bersama, misal anak ituk tinggal bersama dengan neneknya untuk bersekolah di dekat rumah nenek, masih berumur 10 tahun, anak masih masuk di kk orang tuannya, berarti saat pendataan di rumah neneknya sang anak tetep dianggap keluarga sendiri ( ada 2 keluarga keluarga nenek dan keluarga anak (hanya berisi anak)? meskipun belum cukup umur untuk menjadi responden? atau malah digabung
sebagai anggota keluarga Nenek meski sebenernya berbeda KK dengan neneknya, apakah ada batasan usia agar bisa/eligible untuk memberikan jawaban/menjadi
responden
A: 1. Dirumah nenek, anak ditambahkan menjadi assignment sendiri (keluarga tersendiri, berbeda dengan nenek). Anak sebagai kepala keluarga yang anggota keluarganya hanya ia sendiri. Keterangan perumahan mengikuti rumah nenek.
2. info mengenai anak ketika tinggal dirumah nenek, dapat ditanyakan ke nenek sebagai responden
===TOPIC_END===
Q: Pertanyaan Untuk rincian Kepemilikan Fasilitas BAB  jika seorang keluarga anak menumpang BAB di rumah orang taunya (keluarga anak dan keluarga orang tua tinggal berbeda rumah), jadi yang memiliki FAsilitas BAB/WC keluarga orang tuanya kan untuk keluarga orang tuanya status kepemilikan fasilitas BAB terisi kode 2, ada digunakan bersama oleh anggota keluarga dari beberapa rumah; nah untuk keluarga anaknya, status kepemilikan fasilitas BAB nya dipilih kode berapa? apakah kode 2 juga atau kode 4?
jika ternyata dipilih kode 2, kan sebenernya sang anak itu kondisinya tidak memiliki fasilitas BAB ya?, jadi kapan Pilihan kode 4 tidak ada fasilitas BAB nya
terpilih
A: Keluarga anak dan orang tua sama-sama terisi kode 2. Ada, digunakan bersama oleh anggota keluarga dari beberapa rumah
===TOPIC_END===
Q: Untuk usaha industri kue basah, industri tempe, industri makanan dalam kemasan, buat di rumah dan seluruhnya dijual di pasar.
artinya ada 2 usaha? di rumah sebagai industri, di pasar usaha perdagangan?.
- usaha d rumah 13b 1 'Ya', kategori industri, jaringan usaha pabrik.
- untuk usaha di pasar rincian 13b1 (apakah memproduksi barang di lokasi ini) akan tercatat 'Tidak'. kategori perdagangan, R14 jaringan usahanya adalah unit penunjang.
benarkah demikian?
tapi yang di pasar itu kan tidak ada mengambil selisih harga dari yang di rumah.
A: jaringan pabrik hanya untuk unit kegiatan usaha yang hanya memproses produksi, tidak ada aktivitas lainnya, seperti aktivitas  administrasi dan pemasaran. sementara rumah yang digunakan sebagai tempat produksi juga ada aktivitas adminstrasi dan pemasaran dianggap sebagai usaha tunggal.
Jadi usaha produksi kue basah, tempe yang dibuat di rumah, jaringan usahanya adalah usaha tunggal industri pengolahan, sementara unit penjualan di pasar sebagai usaha tunggal perdagangan (bukan unit penunjang)
===TOPIC_END===
Q: Adakah minimum jumlah tanaman pangan atau luas tanam minimumnya yang dianggap sebagai usaha pertanian tanaman pangan ? Karena ada cukup banyak masyarakat di DKI Jakarta yang memanfaatkan tanah yang kosong untuk menanam tanaman pangan seperti ubi kayu dan jumlah pohonnya sangat sedikit (dapat dihitung dengan jari). karena secara konsep tanaman pangan yang dikonsumsi sendiri termasuk usaha. apakah hanya menanam 1 pohon ubi kayu itu
sudah dianggap ada usaha pertanian tanaman pangan?
A: berapa jarak tanam normal tanaman pangan atau per komoditasnya? adakah info tersebut di slide?
===TOPIC_END===
Q: Mengacu ke pertanyaan no 238, untuk kantor perwakilan karena kegiatan mengawasi dan mengkoordinir urusan kantor area, apakah KBLI nya bisa kategori N 70 pak? walaupun bukan kantor pusat ataukah mengikuti KBLI pegadaian (kategori L)?
Izin melanjutkan Pak, Kanwil berfungsi sebagai pengawas dan pengelola operasional untuk wilayah geografis tertentu - tidak ada kegiatan gadai dengan nasabah, apakah kanwil tetap KBLI Pegadaian, atau KBLI Kantor Pusat mengingat kegiatannya?
A: Untuk Kantor Perwakilan atau Kanwil yang kegiatannya mengawasi dan mengkoordinir dan tidak ada kegiatan layanan gadai dengan nasabah, mengikuti KBLI Kantor Pusat (N 70100).
===TOPIC_END===
Q: Kenapa hanya ada beberapa KBLI khusus yang kegiatan utamanya dilihat dari naturenya?
Usaha karaoke secara nature adalah karaoke, tp kalo lihat pendapatannya, margin perdagangan makan minum / usaha PMMnya bisa jadi lebih besar. Apakah pada kasus seperti ini, keg utamanya bukan karaoke, tapi jadi perdagangan/usaha PMM?
A: untuk saat ini, yang sudah disepakati, usaha berdasarkan nature adalah
1. Usaha Bengkel yang juga menjual sparepart
2. Usaha Salon yang juga menjual alat kosmetik
3. Usaha Fotocopy yang juga menjual ATK
4. Usaha minimarket yang juga menjual minuman (kopi)
5. usaha Karaoke
6. klinik kecantikan
===TOPIC_END===
Q: Untuk keluarga yang tinggal di kepulauan, biasanya mereka punya rumah lain di darat/ibukota kabupaten. Alamat KK adalah di kepulauan, dan keluarga tidak menentu kapan menempati rumahnya di kepulauan (tergantung cuaca, tapi dalam setahun pasti ada pulang 2-3 kali).
1. Keberadaan anggota keluarga berpatokan pada rumah yang mana?
2. Kondisi perumahan dan aset apakah mengikuti rumah sesuai KK (pulau) atau domisili setempat?
A: Misalkan saat pendataan: keluarga sedang tinggal di darat sedangkan prelist ada di Kepulauan, maka:
1. Keluarga di prelist Kepulauan, petugas mencari tahu keberadaan keluarga tersebut dari tetangga-tetangganya, berstatus Tidak ditemukan (kode 0) jika tidak bisa diperoleh apa pun mengenai keluarga tsb atau tidak dapat ditemui hingga akhir pendataan (kode 5) jika diketahui keluarga tsb masih tinggal di rumah itu. Selanjutnya akan ada assignment baru untuk keluarga di alamat darat.
2. Kondisi perumahan dan aset mengikuti kondisi rumah keluarga di darat (yang
ditinggali). Untuk rumah di kepulauan, akan dicatat di Aset Lainnya
===TAGS===#KBLI & Klasifikasi,#Metodologi
Q: Sweet Bakery yang berlokasi di Jalan Cendana memproduksi roti sebanyak 1.000 pcs dengan harga jual Rp20.000,00 per pcs.
Dalam proses produksinya, Sweet Bakery mengeluarkan biaya sebagai berikut: Biaya produksi: Rp10.000.000, Biaya operasional (listrik, internet, transportasi, dll.): Rp1.000.000, Upah pegawai: Rp3.000.000.
Dari total 1.000 pcs roti yang diproduksi: Sebanyak 600 pcs dijual di outlet Sweet Bakery Jalan Cendana, Sebanyak 400 pcs disalurkan ke outlet Sweet Bakery Jalan Rinjani.
Adapun biaya operasional di outlet Jalan Rinjani adalah: Sewa ruko: Rp1.000.000, Upah pegawai: Rp1.500.000.
Selain menjual produk sendiri, Sweet Bakery juga menerima titipan penjualan kerupuk dari usaha lain sebanyak 100 pcs dengan harga Rp10.000 per pcs, dengan rincian: 50 pcs dijual di outlet Jalan Cendana dan 50 pcs dijual di outlet Jalan Rinjani.
Bagaimana cara pengisian jaringan usaha, pendapatan, dan pengeluaran untuk Sweet Bakery di Jl Cendana dan Jl. Rinjani?
A: Sweet Bakery Cendana: Kantor Pusat Pengeluaran
a. Upah: Rp3.000.000
b. Biaya Produksi: Rp10.000.000
c. pembelian barang yg terjual: 0
d. Biaya operasional: Rp1.000.000
e. Biaya non operasional: 0
Pendapatan
a. pendapatan: (1.000 x Rp20.000) + komisi penjualan 50 kerupuk
b. pendapatan lainnya: 0
Sweet Bakery Rinjani: Kantor Cabang
a. Upah: Rp1.500.000
b. Biaya Produksi: 0
c. pembelian barang yg terjual: 400 x Rp20.000 = Rp8.000.000
d. Biaya operasional: Rp1.000.000
e. Biaya non operasional: 0
Pendapatan
a. pendapatan: (400 x Rp20.000) + komisi penjualan 50 kerupuk
b. pendapatan lainnya: 0
===TOPIC_END===
Q: Pada flowchart penentuan jumlah usaha pada slide 10, penentuan jumlah usaha ketika misalnya punya lebih dari satu usaha dengan laporan keuangan tidak terpisah maka usaha yang tercatat ditentukan berdasarkan nilai omzet yang paling besar sedangkan pada slide 14 dan 15 jenis aktivitas usaha ditentukan berdasarkan nature usaha/izin usaha/pengakuan responden atau nilai penjualan/produksi/pendapatan. Jadi sebenarnya layer penentuan jumlah usaha berdasarkan omzet terbesar atau nature/izin/pengakuan responden? mohon
penjelasannya
A: - identifikasi esstablishment: pemilik, lokasi, laporan keuangan
- jika tidak bisa dibedakan laporan keuangannya, maka dianggap 1 usaha dengan melihat usaha dengan omset terbesar
- terdapat 4 jenis usaha yang harus dilihat naturenya : bengkel, fotokopi, salon, minimarket/swalayan
===TOPIC_END===
Q: tolong berikan penjelasan lebih detail terkait identifikasi establishment pada usaha mikro. seperti apa yang dicatat 1 dan seperti apa yang dicatat lebih dari 1. karna garis batasnya dari contoh yang disebutkan pada slide kurang begitu jelas. apakah dari pemilik, tempat usaha, atau pengelolaannya?
1. di contoh usaha online dan pemilik kontakan dicatat 2 usaha karena berbeda naturenya. jika demikian contoh yang nasi uduk dan warung kopi kan bisa juga naturenya dianggap berbeda.
2. bagaimana dengan usaha warung sembako, yang juga menjual pulsa, gas,
bensin eceran?
A: - Identifikasi establishment menggunakan 3 pendekatan :pemilik, lokasi usaha, dan pendekatan laporan keuangan (tidak ada pengecualian usaha mikro)
1. untuk usaha kopi dan warung nasi uduk bisa dipastikan dulu laporan keuangannya terpisah atau tidak. usaha online dan kontrakan juga bisa dipastikan terlebih dahulu laporan keuangannya terpisah atau tidak.
2.  dilihat dulu lokasi bangunan usaha nya. jika 2 lokasi maka bisa dipisahkan, jika 1 lokasi maka dilihat laporan keuangan terpisah atau tidak. jika tidak terpisah maka dianggap 1 usaha dengan omset terbesar
===TOPIC_END===
Q: Terkait pekerja konstruksi  jika dia menawarkan jasa sendiri  kemudian kerjanya dibayar harian, bekerja dan diberi upah oleh orang lain apakah tetap dianggap bukan usaha? bisakah diperjelas apa yang menjadi kata kunci/yang membedakan ketika usaha kosntruksi/bangunan harian, bekerja dan diberi upah oleh orang lain dianggap bukan usaha, namun untuk ART Yang tidak menginap dan memiliki majikan lebih dari satu dianggap usaha dan kuli pekerja lepas (dia dibayar harian
oleh banyak orang) pun dianggap usaha.
A: Konsep menanggung risiko, menanggung input, memperjualkan barang/jasa dan memasarkan barang/jasa
===TOPIC_END===
Q: Bagaimana usaha pertanian dengan sistem bagi hasil?
1. jika 1 orang sebagai pemilik lahan, 1 orang penggarap. modal beli bibit , pupuk dll dari penggarap. pemilik lahan hanya memperoleh bagi hasil dari hasil penjualan. apakah kedua orang itu usaha? pemilik lahan usaha penyewaan lahan dan penggarap usaha pertanian?
2. jika 1 orang pemilik lahan, 1 orang penggarap. modal dari pemilik lahan. tp hasil bagi 3 misal (pemilik 2 bagian, penggarap 1 bagian). bagaimana
pencatatannya.
A: 1. Penggarap sebagai usaha pertanian, pemilik lahan bukan usaha pertanian.
2. Jika seluruh modal usaha berasal dari pemilk lahan, maka pemilik lahan dianggap sebagai pengelola usaha pertanian karena bila terjadi gagal panen, maka menjadi tanggungan pemilik lahan (modal), sedangkan penggarap dalam hal ini dianggap sebagai buruh yang dibayar dengan 1 bagian bagi hasil.
===TOPIC_END===
Q: Untuk penggunaan air gunung/ air sumber/ mata air yang bebas pakai apakah di inputasi? Karena tadi sempat disinggung penggunaan lahan bebas sewa tidak diinputasi
Begitu juga dengan penjual pisang goreng yang pisangnya ambil dari budidaya sendiri dan ambil dari hutan (tidak dibudidayakan) apakah harus diimputasi semua nilainya berdasar harga pasar atau ada perbedaan?
Sama halnya dengan nelayan yang mengambil ikan di laut, apakah juga harus diimputasi biaya ikannya sesuai harga pasar atau dari cara mendapatkan ikannya?
A: Diimputasi sesuai harga pasar. Bila harga pasar air gunung/mata air di wilayah tersebut o, maka nilai imputas untuk air = 0
===TOPIC_END===
Q: Pada pelatihan kelas C kemarin, dicontohkan:
usaha klinik dan apotek, punya dua izin (izin klinik dan izin apotik), 1 pemilik, di tempat yang sama, pemilik sama, laporan keuangan 1.
maka dicatat sebagai 1 usaha. meskipun izinnya 2. apakah masih sesuai?
- Jika tercatat 1 usaha, kenapa pada slide metodologi (identifikasi establisment), contoh toko kelontong dan BRI Link dicatat sebagai 2 usaha karena nature kegiatan usahanya berbeda?
A: umumnya kedua jenis kegiatan ini walaupun dimiliki oleh 1 pemilik, laporan keuangannya terpisah, sesuai perizinannya sehingga dihitung 2 establishmen. bila ternyata laporan keuangannya jadi 1 (misal berbentuk CV dengan satu nama usaha, maka dianggap 1 usaha
===TAGS===#Pencatatan Pendapatan,#Teknis
Q: Melanjutkan pertanyaan no 5 diatas, berarti untuk usaha industri tempe di rumah dan menjual di pasar dimana unit di pasar adalah unit penunjang. Berarti untuk industri dirumah jaringan usahanya akan berstatus Kantor Pusat? Karena untuk unit penunjang di pasar membutuhkan isian kantor pusat di rincian 15. Kalau
seperti ini bukankah jadi akan banyak yang berstatus Kantor Pusat?
A: - Sudah diputuskan usaha perdagangan di mall/pasar pada tempat khusus usaha (BKU), diperlakukan sebagai usaha/establisment sendiri
- terdapat penegasan terbaru merujuk pada pertanyaan 4
===TOPIC_END===
Q: Bagaimana perlakuan bagi usaha yang pindah-pindah dari pasar/pekan ke pekan. Jika senin di pekan A, rabu di pekan B dan Sabtu di pekan C, bagaimana perlakukan usaha yang seperti ini, jika dia tidak punya tempat usaha tetap hanya beratapkan tenda, tapi tempat tetap hanya kar kaki per hari pekannya?
Bagaimana jika di setiap pekan, si pengusaha berpindah-pindah secara harian di kios masing-masing pasar di kios bangunan tetap. Usaha si pengusaha didata dimana?? apakah di setiap pasar didata?
A: - Untuk kasus disini, yang usahanya perpindah/pindah dari satu pasar ke pasar lain dengan menggunakan tenda (ka kaki) dan tempatnya tidak tetap, maka akan didata di rumah tangganya
- Usaha  di bangunan tetap (kios/BKU), hanya berbeda lokasi, maka akan di cacah di masing-masing kios (karena secara konsep usaha akan dicacah di BKU)
===TOPIC_END===
Q: Bagaimana pencatatan tenaga kerja musiman di usaha pertanian dan di industri? Apakah tenaga kerja yang bantuin selama musim panen dicatat sebagai tenaga kerja atau dicatat sebagai jasa pertanian (biaya produksi)?
Begitu juga dengan tenaga kerja yang dihire oleh industri kue selama menjelang lebaran bagaimana pencatatan tenaga kerjanya? Atau dicatat sebagai biaya
produksi karena tidak tetap?
A: pekerja musiman dicatat sebagai pekerja, yang dicatat sebagai biaya jasa apabila pembayarannya melalui usaha/perusahaan perantara penyalur tenaga kerja
===TOPIC_END===
Q: Hasil uji coba Internal Rollout Tahap II, ketika dalam 1 bangunan tempat tinggal terdapat 2 Keluarga, bagaimana pengisian keterangan untuk keluarga ke-2 tersebut, karena tidak muncul pilihan untuk pengisian keluarga ke-2 tersebut, apakah Keluarga ke-2 tersebut harus ditambahkan/merupakan assignment tersendiri untuk pengisian keterangan anggota keluarga, dan lain-lainnya?
A: Ya ditambahkan assignment tersendiri
===TOPIC_END===
Q: utk anak di bawah 17 tahun yang tinggal bersama neneknya di kab A krn sekolah, sdgkan orangtua nya tinggal di kab B. utk anak tsb ketika petugas dtg di rumah orangtua di kab B maka anaknya berkode 3 tidak tinggal dgn keluarga. Kemudian ketika rumah neneknya didatangi petugas apakah anak tsb apakah hrs ditambahkan assigment baru?
A: Betul. Anak dianggap sebagai keluarga sendiri di rumah nenek (karena berbeda KK). Anak menjadi kepala keluarga.
===TAGS===#Identifikasi Tempat Usaha & Bisnis Keluarga,#Identifikasi
Q: Hasil percobaan roll out tahap 2:
1. Setelah Rincian 13 c seharusnya langsung 13 f, tapi ini masih diminta mengisi 13e
2. Setelah Rincian 13 b4 terisi Ya seharusnya langsung 13 f, tapi ini masih diminta mengisi 13d dan 13 e
3. Keterangan contoh untuk rincian 13 d dan 13 e masih dijelaskan bibit dan pakan (kategori pertanian), padahal berdasarkan penjelasan tadi pagi, jika dia termasuk kategori A maka setelah 13 b4 langsung ke 13 f (produk utama), jadi contoh untuk rincian 13 d dan 13 e tidak termasuk usaha pertanian
4. Rincian 24 pekerja ketika dicoba jumlah pekerja =0 bisa (tidak ada warning), tetapi ketika jumlah pekerja = 1 kenapa ada warning: "Jika total pekerja=1, maka banyaknya pekerja tidak dibayar adalah 1 atau 0"? Jika pekerja tersebut bukan keluarga dan dibayar apakah tidak boleh total pekerja=1?
A: - Aturan validasi aplikasi fasih akan di perbaiki sesuai arahan tim fasih, pada tahap ini masih proses penyusunan dan belum final.
- pada rincian 24 Pekerja (total), total pekerja minimal 1, jika pekerja tsb adalah pemilik /pengelola yang diupah dan bukan sebagai pekerja tetap di usaha tsb maka bisa diklasifikasikan sebagai pekerja lainnya dan Pekerja tersebut dibayar
===TOPIC_END===
Q: Untuk kasus unit usaha di pasar, yang tidak punya kios tapi hanya menyewa "lapak" saja, masuk kemana? (rincian 13 b 2 kah "di tempat tidak tetap/keliling? atau rincian 13 b 1 "di bangunan khusus usaha)
A: Untuk unit usaha di pasar, yang tidak punya kios/los tapi hanya menyewa "lapak" saja merupakan usaha tidak menempati bangunan (kaki lima / usaha keliling).
===TOPIC_END===
Q: Ada beberapa yayasan yang di satu kompleks, terdiri dari TK, SD, SMP, SMA. Apakah di prelist tersendiri setiap sekolah?
A: Untuk kasus yayasan yang mengelola sekolah/lembaga pendidikan (dalam satu kompleks), akan di cacah sendiri-sendiri per jenjang pendidikan dan akan tercatat berstatus unit penunjang. sedangkan yayasannya akan tercatat berstatus kantor pusat.
===TOPIC_END===
Q: 1. Jika anak belum berumur 17 tahun dan sudah bekerja untuk membantu orang tuanya tanpa di bayar, bagaimana perlakuan pendataanya ?
2.  jika anak belum berumur 17 tahun dan punya  usaha sendiri  , bagaimana  perlakuan pendataanya?
A: 1. Jika anak (dibawah 17th) membantu usaha orangtua dan  tidak di bayar, maka dicatat sebagai pekerja yang tidak di bayar
2.  Jika anak tersebut memiliki usaha sendiri maka akan tercatat sebagai usaha sendiri dan si anak tersebut  menjadi pemilik usaha tersebut. (namun ini sangat kecil kemungkinan terjadi)
===TOPIC_END===
Q: Terkait usaha penginapan seperti kos-kosan jika jumlah kamarnya >=10 dan rumah kontrakan jumlah pintunya >=10 maka di kenali sebagai usaha. Pertanyaan nya, apakah ada batasan kamar yang terisi? jika tidak dan misalkan ada kamar 15 tetapi yang terisi hanya 5  berarti ini kan memenuhi syarat di kenali sebagai usaha kos2an , tp secara income mungkin hanya sedikit apakah ttp dikenali sebagai usaha
A: Pada SE 2026, batasan usaha penyediaan akomodasi (kos/kontrakan) didasarkan pada jumlah kamar/pintu yang disewakan >=10, meskipun pada saat pendataan ada yang tidak terisi.
===TOPIC_END===
Q: apabila bangunan khusus usaha tersebut di kontrakkan, apakah si pemilik bangunan di data di BKU tersebut?
A: Yang di data adalah usaha yang menyewa bangunan tersebut, kecuali si pemilik bangunan tersebut menyewakan >= 10 unit bangunan/pintu maka si pemilik akan didata di rumahtangganya.
===TOPIC_END===
Q: Berlanjut dari pertanyaan diatas, apabila bku ini banyak tetapi yang menyewakan bku ini 1 orang/pemilik, dan dari 10 bku yang dimiliki disewakan/kontrakkan ada 2 bku dan 8 bku kosong.
apakah sipemilik bangunan ini didata di bku tersebut? atau karena menyewakan bangunan ini merupakan masuk ke usaha yg menempati bangunan tidak khusus/rumah tangga, sehingga didata dirutanya
A: Usaha sewa bangunan dicacah di lokasi bangunan jika bangunan tersebut adalah satu kesatuan (misal kos-kosan/kontrakan dalam 1 kompleks) dan >=10 pintu. jika terpencar, akan dicacah di rumahtangga. Jika ada bangunan kosong maka tidak dicatat sebagai usaha (tidak didata).
===TOPIC_END===
Q: Izin bertanya,  jika ada pemilik perusahaan yang menyerahkan pengelolaan usaha ke pihak lain dan pemilik tsbt tdak tau secara teknis dan juga omset usahanya. Yang hanya di ketahui pemilik tsb hanya laba bersihnya sj tiap bulannya. Untuk kasus ini bgaimana pengisian kuesionernya ? Khusus nya pngisan pendapatan/penjualan dsb .. karna pihak pengelola juga tidak mau memberi tau..
A: Responden utama dari SE 2026 adalah pengelola unit usaha. Jika pengelola tidak bersedia menjawab / memberikan informasi, dapat melakukan pendekatan kepada pihak-pihak terkait, jika masih tidak bersedia dapat di catat sebagai non respon.
===TOPIC_END===
'''

def get_short_title(q_text):
    # Take first sentence or first ~120 characters to act as title
    parts = q_text.split('?')
    if len(parts) > 1 and len(parts[0]) < 120:
        return parts[0].strip() + '?'
    parts = q_text.split('.')
    if len(parts) > 1 and len(parts[0]) < 120:
        return parts[0].strip() + '.'
    return q_text[:120].strip() + '...'

new_qnas = []
sections = old_qna_text.split('===TAGS===')
for section in sections:
    if not section.strip(): continue
    parts = section.split('\nQ:')
    tags = parts[0].strip().split(',') if ',' in parts[0] else []
    if tags:
        q_blocks = parts[1:]
    else:
        tags = ['#Prosedur Prelisting', '#Metodologi']
        q_blocks = section.split('Q:')[1:]
    
    for block in q_blocks:
        if '===TOPIC_END===' in block:
            block = block.split('===TOPIC_END===')[0]
        q_text = block.split('A:')[0].strip()
        a_text = block.split('A:')[1].strip()
        
        # Clean formatting
        q_clean = ' '.join(q_text.split('\\n'))
        a_clean = ' '.join(a_text.split('\\n'))
        
        new_qnas.append({
            'q_full': q_text,
            'a_full': a_text,
            'tags': tags
        })

# Parse OLD file to extract all OLD questions
with open('c:/BERKAS STIS/SENSUS EKONOMI/PORTAL INFORMASI SE ORLAP/berkas adm/top qna.txt', 'r', encoding='utf-8') as f:
    text = f.read()

topics = re.split(r'TOPIK: .*?\nKonteks: .*?\n.*?\n={10,}', text)[1:]
if not topics:
    # try old format
    topics = re.split(r'TOPIK \d+ .*?\n={10,}', text)[1:]

old_qna_data = []

topic_mapping = {
    0: ['#Prosedur Prelisting', '#Metodologi'],
    1: ['#Aplikasi FASIH', '#Sistem'],
    2: ['#KBLI & Klasifikasi', '#Metodologi'],
    3: ['#Pencatatan Pendapatan', '#Teknis'],
    4: ['#Identifikasi Tempat Usaha & Bisnis Keluarga', '#KasusBatas']
}

for i, content in enumerate(topics):
    tags = topic_mapping.get(i, ['#Metodologi'])
    qnas = re.split(r'-{10,}', content)
    for qna in qnas:
        qna = qna.strip()
        if not qna: continue
        q_match = re.search(r'Q:\s*(.*?)\nA:', qna, re.DOTALL)
        a_match = re.search(r'A:\s*(.*)', qna, re.DOTALL)
        if q_match and a_match:
            question = q_match.group(1).strip()
            answer = a_match.group(1).strip()
            question_cl = re.sub(r'^\d+\.\s*', '', question)
            old_qna_data.append({
                'q_full': question_cl,
                'a_full': answer,
                'tags': tags
            })

all_qnas = old_qna_data + new_qnas

# Now update qna.html
html_path = 'c:/BERKAS STIS/SENSUS EKONOMI/PORTAL INFORMASI SE ORLAP/qna.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace DATA_QNA
start_idx = html_content.find('const DATA_QNA = [')
end_idx = html_content.find('];', start_idx) + 2

js_qnas = []
for idx, item in enumerate(all_qnas):
    cat = 'Metodologi'
    if '#Aplikasi FASIH' in item['tags']: cat = 'Aplikasi FASIH'
    elif '#Prosedur Prelisting' in item['tags']: cat = 'Prosedur Prelisting'
    elif '#KBLI & Klasifikasi' in item['tags']: cat = 'KBLI & Klasifikasi'
    elif '#Pencatatan Pendapatan' in item['tags']: cat = 'Pencatatan Pendapatan'
    elif '#Identifikasi Tempat Usaha & Bisnis Keluarga' in item['tags']: cat = 'Identifikasi Tempat Usaha & Bisnis Keluarga'
    
    tags_str = ', '.join([f"'{t.replace('#','')}'" for t in item['tags']])
    
    # Generate Short Title
    q_short = get_short_title(' '.join(item['q_full'].split('\n')))
    q_short = q_short.replace('`', '\\`')
    
    # We replace newlines with <br/>\n to format nicely in HTML and keep JS lines short
    q_full_html = item['q_full'].replace('`', '\\`').replace('\n', '<br/>\n')
    a_full_html = item['a_full'].replace('`', '\\`').replace('\n', '<br/>\n')
    
    final_answer_html = f"""<div style="font-weight: 600; color: var(--clr-blue); margin-bottom: 8px;">Pertanyaan Lengkap:</div>
<div style="margin-bottom: 16px; line-height: 1.5;">{q_full_html}</div>
<div style="font-weight: 600; color: var(--clr-orange); margin-bottom: 8px;">Jawaban:</div>
<div style="line-height: 1.5;">{a_full_html}</div>"""
    
    js_obj = f"""      {{
        id: 'q{idx+1}', category: '{cat}', tags: [{tags_str}],
        question: `{q_short}`,
        answer: `{final_answer_html}`
      }}"""
    js_qnas.append(js_obj)

new_array = 'const DATA_QNA = [\n' + ',\n'.join(js_qnas) + '\n    ];'
new_html = html_content[:start_idx] + new_array + html_content[end_idx:]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f'Successfully updated qna.html with {len(all_qnas)} questions.')
