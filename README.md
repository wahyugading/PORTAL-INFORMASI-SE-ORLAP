# Portal Informasi Sensus Ekonomi 2026 (SE2026)

Selamat datang di repositori **Portal Informasi Sensus Ekonomi 2026**. Aplikasi web ini dibangun untuk memfasilitasi dan mempermudah petugas Sensus Ekonomi di lapangan dalam mengakses informasi penting, mencari solusi atas kendala pendataan, serta menghubungi koordinator dan layanan bantuan secara instan.

[![Live Demo](https://img.shields.io/badge/Live_Demo-Vercel-black?style=for-the-badge&logo=vercel)](https://portal-informasi-se2026.vercel.app/)

---

## 🎯 Fitur Utama

- **Beranda & Navigasi Cepat:** Antarmuka responsif yang ramah seluler (*mobile-first*) dengan *Bottom Navigation Bar* khas aplikasi *mobile*.
- **Informasi & Pengumuman:** Menampilkan pembaruan (update) terbaru terkait instruksi teknis, metodologi, maupun logistik secara *real-time*.
- **QnA & FAQ Cerdas (Fuzzy Search):** Daftar tanya-jawab kendala lapangan (kasus batas, aplikasi FASIH, KBLI, Prelisting) yang dirangkum menjadi intisari ringkas. Dilengkapi dengan fitur pencarian canggih dan *tag filter* untuk mempermudah pencarian.
- **Pusat Solusi Lapangan (Triage System):**
  - **Kendala Lapangan:** Form pelaporan kendala teknis dan pencarian nomor kontak Koordinator Wilayah (Korwil).
  - **Layanan Kelelahan Mental & Stres:** Integrasi akses konseling bagi petugas lapangan, baik melalui Unit Pelayanan Kesehatan (UPK) Kampus maupun Konselor Sebaya BEM, dilengkapi tampilan poster interaktif.
  - **Darurat (Emergency):** Akses cepat (satu klik) ke Koordinator Utama atau Koordinator Magang Dosen saat kondisi darurat (konflik, penolakan keras, dll).
- **Dukungan PWA (Progressive Web App):** Dilengkapi dengan `manifest.json` yang memungkinkan pengguna untuk menginstal portal ini sebagai aplikasi di layar beranda (Homescreen) *smartphone* mereka.

## 🛠 Tech Stack

Aplikasi ini dibangun menggunakan arsitektur *Static Site* demi performa pemuatan (loading) yang super cepat, ringan, dan tidak membutuhkan koneksi database yang kompleks.

- **HTML5:** Struktur semantik utama.
- **CSS3 (Vanilla):** Sistem desain khusus (Custom Design System) dengan pendekatan *High Contrast Light* dan *Glassmorphism* (backdrop-filter).
- **Vanilla JavaScript:** Manipulasi DOM untuk logika pencarian, sistem *tab triage*, dan filter kategori.
- **Python (Utility):** Digunakan *script* tambahan (`summarize_qna_data_new.py`) untuk mengonversi data kompleks dari JSON menjadi elemen UI langsung ke dalam HTML.

## 🚀 Instalasi & Deployment

Portal ini tidak memerlukan *build tools* (seperti Webpack atau Vite) dan tidak menggunakan backend server seperti Node.js atau PHP.

### Menjalankan Secara Lokal (Local Development)
1. *Clone* repositori ini:
   ```bash
   git clone https://github.com/wahyugading/PORTAL-INFORMASI-SE-ORLAP.git
   ```
2. Buka folder repositori di editor teks Anda (VS Code, Cursor, dll).
3. Buka file `index.html` menggunakan fitur **Live Server** di editor Anda.
4. Anda juga bisa sekadar mengklik ganda file `.html` mana saja untuk menjalankannya langsung di browser.

### Deployment (Live Server)
Saat ini proyek ter-*deploy* secara mulus via **Vercel**. Karena berformat *static files*, aplikasi ini juga bisa di-*hosting* di platform manapun yang mendukung *static hosting* seperti:
- GitHub Pages
- Cloudflare Pages
- Nginx / Apache Server biasa (Kampus IT Server)

## 📁 Struktur Direktori

```text
├── assets/                  # Kumpulan gambar, poster, dan logo pendukung.
├── index.html               # Halaman Beranda.
├── bantuan.html             # Halaman Pusat Solusi & Triage Bantuan.
├── informasi.html           # Halaman Papan Pengumuman.
├── qna.html                 # Halaman FAQ interaktif dengan fuzzy search.
├── struktur.html            # Halaman Struktur Organisasi Lapangan.
├── manifest.json            # Konfigurasi PWA (Progressive Web App).
├── summarize_qna_data_new.py # Script Python pembantu manajemen data FAQ.
└── README.md                # Dokumentasi proyek.
```

## 📝 Catatan Penting
- **Pembaruan Data QnA:** Jika terdapat set data FAQ baru, Anda bisa memperbarui *array dictionary* pada `summarize_qna_data_new.py` kemudian mengeksekusi script tersebut untuk otomatis menyuntikkan (inject) rangkuman ke file `qna.html`.
- **Nomor Kontak:** Pastikan seluruh kontak Korwil, WA darurat, dan *link* Google Form yang tertaut (*hardcoded*) dijaga kerahasiaannya untuk lingkup petugas yang berkepentingan saja.

---
*Dibuat untuk kelancaran Sensus Ekonomi 2026.* 
**#MencatatEkonomiIndonesia**
