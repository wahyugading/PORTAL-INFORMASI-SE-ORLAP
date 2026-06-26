---
{
  "id": "file_pi45qfx8",
  "filetype": "document",
  "filename": "Dokumen Spesifikasi Teknis PR-SE2026",
  "created_at": "2026-06-25T17:29:23.539Z",
  "updated_at": "2026-06-25T17:29:23.539Z",
  "meta": {
    "location": "/",
    "tags": [],
    "categories": [],
    "description": "",
    "source": "markdown"
  }
}
---
# **DOKUMEN ACUAN TEKNIS & PEDOMAN PENGEMBANGAN PORTAL**

## **Portal Repository & Pusat Bantuan Lapangan Sensus Ekonomi 2026 (PR-SE2026)**

### **DAFTAR ISI**

1. Pendahuluan & Spesifikasi Teknologi (Tech Stack)  
2. Matriks Identifikasi Risiko, Urgensi, & Solusi Teknis  
3. Cetak Biru Implementasi Kode (Code Blueprints)  
   * 3.1. Fitur Offline (PWA & Service Worker)  
   * 3.2. Fitur Keamanan Ganda (NextAuth & Obfuscator Kontak)  
   * 3.3. Fitur Kecepatan UX (Fuzzy Live Search & Chips)  
   * 3.4. Fitur Triage Call Center (Sistem Penyaringan Darurat)  
4. Spesifikasi Desain & Panduan Aksesibilitas (WCAG)  
5. Alur Validasi Rilis (Checklist Staging)

### **1\. PENDAHULUAN & SPESIFIKASI TEKNOLOGI (TECH STACK)**

Dokumen ini berfungsi sebagai acuan teknis utama dalam pengembangan portal **PR-SE2026**. Portal ini dirancang untuk memfasilitasi mahasiswa tingkat 2 Polstat STIS yang bertugas sebagai petugas lapangan agar dapat mengakses surat legalitas, mencari solusi kasus metodologi, serta melaporkan kendala darurat secara instan di bawah kendala jaringan internet.

Untuk memenuhi kebutuhan sistem yang dinamis namun tetap mempertahankan biaya operasional **nol rupiah (100% Free Tier)**, berikut adalah spesifikasi teknologi yang wajib diimplementasikan:

| Komponen | Teknologi | Deskripsi |
| :---- | :---- | :---- |
| **Framework Utama** | Next.js 14/15 (App Router) | Pilihan terbaik untuk performa tinggi, struktur rute yang rapi, dan kemampuan Serverless/Edge gratis di Vercel. |
| **UI/UX Styling** | Tailwind CSS | Utility-first CSS untuk mempercepat proses pembuatan komponen responsif (*mobile-first*). |
| **PWA Engine** | @ducanh2912/next-pwa | Library modern untuk mengotomatisasi kompilasi Service Worker dan manajemen *cache* lokal. |
| **Authentication Gate** | NextAuth.js (v4/v5) \+ Google Provider | Membatasi akses masuk portal hanya bagi mahasiswa dengan akun email institusi. |
| **Data Submission** | Google Forms API Integration | Penanganan pelaporan kendala tanpa database internal (data otomatis masuk ke Google Sheets). |
| **Hosting Platform** | Vercel (Hobby/Free Tier) | Deployment otomatis terintegrasi ke repositori GitHub dengan dukungan global CDN. |

### **2\. MATRIKS IDENTIFIKASI RISIKO, URGENSI, & SOLUSI TEKNIS**

| No | Risiko & Masalah Lapangan | Tingkat Urgensi | Analisis Dampak / Alasan | Solusi Teknis & Desain |
| :---- | :---- | :---- | :---- | :---- |
| **1** | **Blank Spot & Kehilangan Sinyal** Petugas tidak bisa me-load web/surat tugas saat berada di area tanpa sinyal internet (pasar, gang, *basement*). | **KRITIS (HIGHLY URGENT)** | Jika surat legalitas gagal dibuka di depan responden, petugas akan dicurigai, ditolak, atau bahkan diusir dari lokasi. | Konfigurasi **PWA (Progressive Web App)** dengan *aggressive caching*. Dokumen Surat Tugas disimpan lokal di direktori /public dan dibaca via tag \<img\> (bukan \<iframe\> dari Drive). |
| **2** | **Kebocoran Kontak WA Internal** Nomor WA BPH, Korwil, UPK, dan Bu Risni rentan di-*scraping* oleh bot penipuan jika ditaruh di web publik. | **KRITIS (HIGHLY URGENT)** | Mengganggu fokus kerja panitia akibat serangan spam otomatis dan melanggar hukum privasi data personal (*cybersecurity*). | Terapkan **NextAuth Domain Gate** khusus domain @stis.ac.id ditambah enkripsi **Base64 Obfuscation** pada string nomor telepon di level kode. |
| **3** | **Keterlambatan Solusi Kasus** Mahasiswa membuang waktu responden untuk mencari solusi kasus metodologi di web yang panjang. | **TINGGI (URGENT)** | Responden yang sibuk/tidak ramah akan membatalkan wawancara jika petugas terlalu lama membuka handphone. | Buat **Client-Side Fuzzy Live Search** menggunakan hook useMemo JavaScript (kecepatan pencarian \<100ms) dilengkapi tombol *Quick-Action Chips*. |
| **4** | **Beban Berlebih Call Center** Mahasiswa langsung menghubungi jalur tertinggi (Bu Risni) untuk kendala teknis kecil. | **SEDANG (MEDIUM)** | Menyebabkan *bottleneck* komunikasi pada manajemen pusat dan memperlambat respon kasus yang benar-benar darurat. | Buat sistem **UI Triage (Penyaringan Berjenjang)**. Kontak WA disembunyikan di awal, wajib memilih klasifikasi kasus terlebih dahulu untuk menentukan PIC. |

### **3\. CETAK BIRU IMPLEMENTASI KODE (CODE BLUEPRINTS)**

Bagian ini memuat seluruh kode logika siap pakai yang harus dimasukkan ke dalam repositori proyek Next.js Anda.

#### **3.1. Fitur Offline (PWA & Service Worker)**

**A. Konfigurasi next.config.mjs**

import withPWAInit from '@ducanh2912/next-pwa';

const withPWA \= withPWAInit({  
  dest: 'public',  
  disable: process.env.NODE\_ENV \=== 'development',  
  register: true,  
  skipWaiting: true,  
  cacheOnFrontEndNav: true,  
  aggressiveFrontEndNavCaching: true  
});

/\*\* @type {import('next').NextConfig} \*/  
const nextConfig \= {  
  reactStrictMode: true,  
};

export default withPWA(nextConfig);

**B. File Manifest Aplikasi (public/manifest.json)**

{  
  "theme\_color": "\#f27221",  
  "background\_color": "\#0f172a",  
  "display": "standalone",  
  "scope": "/",  
  "start\_url": "/",  
  "name": "Portal Repository Sensus Ekonomi 2026",  
  "short\_name": "PR-SE2026",  
  "description": "Pusat Bantuan & Bukti Legalitas Sensus Ekonomi 2026 Polstat STIS",  
  "icons": \[  
    {  
      "src": "/icons/icon-192x192.png",  
      "sizes": "192x192",  
      "type": "image/png"  
    },  
    {  
      "src": "/icons/icon-512x512.png",  
      "sizes": "512x512",  
      "type": "image/png"  
    }  
  \]  
}

**C. Root Layout (app/layout.js)**

import './globals.css';

export const metadata \= {  
  title: 'PR-SE2026 \- Portal Repository',  
  description: 'Portal Bukti Legalitas Lapangan Sensus Ekonomi 2026',  
  manifest: '/manifest.json',  
};

export const viewport \= {  
  themeColor: '\#f27221',  
  width: 'device-width',  
  initialScale: 1,  
  maximumScale: 1,  
  userScalable: false,  
};

export default function RootLayout({ children }) {  
  return (  
    \<html lang="id"\>  
      \<head\>  
        \<meta name="apple-mobile-web-app-capable" content="yes" /\>  
        \<meta name="apple-mobile-web-app-status-bar-style" content="default" /\>  
        \<meta name="apple-mobile-web-app-title" content="PR-SE2026" /\>  
        \<link rel="apple-touch-icon" href="/icons/icon-512x512.png" /\>  
      \</head\>  
      \<body className="antialiased bg-slate-950 text-white"\>{children}\</body\>  
    \</html\>  
  );  
}

#### **3.2. Fitur Keamanan Ganda (NextAuth & Obfuscator Kontak)**

**A. API Route Authentication Gate (app/api/auth/\[...nextauth\]/route.js)**

import NextAuth from 'next-auth';  
import GoogleProvider from 'next-auth/providers/google';

const handler \= NextAuth({  
  providers: \[  
    GoogleProvider({  
      clientId: process.env.GOOGLE\_CLIENT\_ID,  
      clientSecret: process.env.GOOGLE\_CLIENT\_SECRET,  
    }),  
  \],  
  callbacks: {  
    async signIn({ profile }) {  
      // Pembatasan Email: Hanya izinkan domain institusi Polstat STIS  
      if (profile?.email && profile.email.endsWith('@stis.ac.id')) {  
        return true;  
      }  
      return '/unauthorized?error=AccessDenied';  
    },  
  },  
  pages: {  
    signIn: '/login',  
    error: '/login',  
  },  
});

export { handler as GET, handler as POST };

**B. Komponen Proteksi Kontak Anti-Bot (components/SecureContact.js)**

'use client';

export default function SecureContact({ name, role, b64Phone }) {  
  const handleCall \= () \=\> {  
    // Dekode nomor telepon Base64 secara dinamis di runtime saat ditekan  
    const decryptedNumber \= atob(b64Phone);  
    const message \= encodeURIComponent(\`Halo ${name}, saya petugas lapangan SE2026 ingin berkonsultasi.\`);  
    window.open(\`https://wa.me/${decryptedNumber}?text=${message}\`, '\_blank', 'noopener,noreferrer');  
  };

  return (  
    \<div className="flex items-center justify-between p-4 bg-slate-800/80 rounded-xl border border-slate-700/50"\>  
      \<div\>  
        \<h4 className="text-sm font-bold text-white"\>{name}\</h4\>  
        \<p className="text-\[11px\] text-slate-400 mt-0.5"\>{role}\</p\>  
      \</div\>  
      \<button  
        onClick={handleCall}  
        className="bg-emerald-600 hover:bg-emerald-500 active:scale-95 text-white text-xs font-bold px-4 py-2.5 rounded-lg transition"  
      \>  
        Hubungi WA  
      \</button\>  
    \</div\>  
  );  
}

#### **3.3. Fitur Kecepatan UX (Fuzzy Live Search & Chips)**

**Halaman Pencarian Solusi Kasus (app/bantuan/page.js)**

'use client';  
import { useState, useMemo } from 'react';

const DATA\_KASUS \= \[  
  {  
    id: 'k1',  
    category: 'Metodologi',  
    tags: \['menolak', 'marah', 'tidak mau', 'usir'\],  
    q: 'Bagaimana jika pelaku UMKM menolak keras didata?',  
    a: 'Tunjukkan Surat Himbauan Menteri UMKM & Surat Tugas BPS. Jelaskan jaminan kerahasiaan data (UU No 16/1997). Jika tetap menolak, catat form kendala dan infokan ke Korwil.'  
  },  
  {  
    id: 'k2',  
    category: 'Sistem',  
    tags: \['pindah', 'bangkrut', 'tutup', 'pindah alamat'\],  
    q: 'Lokasi UMKM di target sampel ternyata sudah pindah?',  
    a: 'Jangan langsung dihapus. Laporkan melalui menu identifikasi masalah dengan opsi "Perubahan Alamat" agar sistem merekapnya otomatis.'  
  }  
\];

const POPULAR\_KEYWORDS \= \['Menolak', 'Pindah', 'Sinyal'\];

export default function SearchCases() {  
  const \[search, setSearch\] \= useState('');  
  const \[activeId, setActiveId\] \= useState(null);

  // Pencarian client-side instan menggunakan useMemo  
  const filteredData \= useMemo(() \=\> {  
    const q \= search.toLowerCase().trim();  
    if (\!q) return DATA\_KASUS;  
    return DATA\_KASUS.filter(item \=\>   
      item.q.toLowerCase().includes(q) ||  
      item.a.toLowerCase().includes(q) ||  
      item.tags.some(t \=\> t.toLowerCase().includes(q))  
    );  
  }, \[search\]);

  return (  
    \<div className="max-w-md mx-auto p-4 space-y-4"\>  
      \<h2 className="text-lg font-black text-yellow-400"\>Pusat Solusi Kasus\</h2\>  
        
      \<input  
        type="text"  
        placeholder="Ketik kata kunci (misal: menolak, pindah)..."  
        value={search}  
        onChange={(e) \=\> setSearch(e.target.value)}  
        className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-sm focus:border-orange-500 focus:outline-none"  
      /\>

      \<div className="flex gap-2"\>  
        {POPULAR\_KEYWORDS.map(kw \=\> (  
          \<button  
            key={kw}  
            onClick={() \=\> setSearch(kw)}  
            className="text-xs px-3 py-1.5 rounded-full bg-slate-800 text-slate-300 hover:bg-slate-700"  
          \>  
            \#{kw}  
          \</button\>  
        ))}  
      \</div\>

      \<div className="space-y-2 pt-2"\>  
        {filteredData.map(item \=\> (  
          \<div key={item.id} className="border border-slate-800 bg-slate-900 rounded-xl overflow-hidden"\>  
            \<button  
              onClick={() \=\> setActiveId(activeId \=== item.id ? null : item.id)}  
              className="w-full text-left p-4 font-bold text-sm text-slate-200"  
            \>  
              {item.q}  
            \</button\>  
            {activeId \=== item.id && (  
              \<p className="px-4 pb-4 text-xs text-slate-400 leading-relaxed border-t border-slate-800/50 pt-2"\>  
                {item.a}  
              \</p\>  
            )}  
          \</div\>  
        ))}  
      \</div\>  
    \</div\>  
  );  
}

#### **3.4. Fitur Triage Call Center (Sistem Penyaringan Darurat)**

**Komponen Triage UI (components/TriageCallCenter.js)**

'use client';  
import { useState } from 'react';  
import SecureContact from './SecureContact';

export default function TriageCallCenter() {  
  const \[stage, setStage\] \= useState('category'); // 'category' | 'result'  
  const \[selectedCategory, setSelectedCategory\] \= useState(null);

  const categories \= \[  
    {  
      id: 'admin',  
      label: '📝 Masalah Laporan & Admin',  
      description: 'Kendala surat tugas hilang, salah rekap, absensi.',  
      pic: 'Sekretaris Lapangan',  
      phoneB64: 'NjI4MTIzNDU2Nzg5' // Gantilah dengan Base64 nomor WA asli  
    },  
    {  
      id: 'mental',  
      label: '🌱 Kelelahan Mental & Stres',  
      description: 'Layanan konseling resmi UPK dan konselor sebaya.',  
      redirectUrl: 'https://s.stis.ac.id/LayananKonselingSebayaSTIS'  
    },  
    {  
      id: 'security',  
      label: '🚨 Konflik Fisik / Penolakan Keras',  
      description: 'Diusir aparat, ancaman keamanan fisik, intimidasi berat.',  
      pic: 'Bu Risni & BPH Utama (Urgent)',  
      phoneB64: 'NjI4OTk5ODg4Nzc3' // Gantilah dengan Base64 nomor WA asli  
    }  
  \];

  return (  
    \<div className="border border-rose-950 bg-rose-950/20 rounded-2xl p-5 space-y-4"\>  
      \<h3 className="text-sm font-black text-rose-400 tracking-wider uppercase"\>📞 Jalur Bantuan Terbimbing\</h3\>  
        
      {stage \=== 'category' ? (  
        \<div className="space-y-2"\>  
          \<p className="text-\[11px\] text-rose-300/80"\>Pilih jenis kendala utama Anda untuk menghindari salah penanganan:\</p\>  
          {categories.map(cat \=\> (  
            \<button  
              key={cat.id}  
              onClick={() \=\> {  
                if (cat.redirectUrl) {  
                  window.open(cat.redirectUrl, '\_blank');  
                } else {  
                  setSelectedCategory(cat);  
                  setStage('result');  
                }  
              }}  
              className="w-full text-left p-3.5 bg-slate-900 hover:bg-slate-800 border border-slate-800 rounded-xl transition"  
            \>  
              \<h4 className="text-xs font-bold text-white"\>{cat.label}\</h4\>  
              \<p className="text-\[10px\] text-slate-400 mt-1"\>{cat.description}\</p\>  
            \</button\>  
          ))}  
        \</div\>  
      ) : (  
        \<div className="space-y-3 animate-fade-in"\>  
          \<div className="p-3 bg-rose-900/30 rounded-lg text-xs text-rose-300"\>  
            \<strong\>Rekomendasi Penanganan:\</strong\> Kontak di bawah ini adalah penanggung jawab yang berwenang menyelesaikan masalah Anda secara cepat.  
          \</div\>  
          \<SecureContact   
            name={selectedCategory.pic}   
            role={\`PIC Bidang ${selectedCategory.label}\`}   
            b64Phone={selectedCategory.phoneB64}   
          /\>  
          \<button  
            onClick={() \=\> { setStage('category'); setSelectedCategory(null); }}  
            className="w-full text-center text-\[11px\] text-slate-400 hover:text-white underline pt-1"  
          \>  
            Kembali ke menu kategori  
          \</button\>  
        \</div\>  
      )}  
    \</div\>  
  );  
}

### **4\. SPESIFIKASI DESAIN & PANDUAN AKSESIBILITAS (WCAG)**

* **Tipografi:** Wajib menggunakan font **Inter** dengan keterbacaan tinggi. Ukuran teks minimal untuk deskripsi adalah 12px (text-xs pada Tailwind) untuk menghindari kesalahan pembacaan nomor atau instruksi kerja.

## **ARSITEKTUR STRUKTUR HALAMAN (SITEMAP)**

Portal dikembangkan menggunakan **Next.js (App Router)** dengan arsitektur *Mobile-First Layout* yang ringan dan bersih.

1. **Halaman Utama (Landing Page / Legalitas):**  
   * *Hero Section:* Poster Menyukseskan SE2026 (Aset lokal, disimpan di `/public/images/poster.png`).  
   * *Quick Action Dashboard:* Grid 2-kolom berisi tombol berbentuk **Kotak Oranye Solid** untuk akses dokumen instan (\< 3 detik): Surat Tugas BPS, Izin Gubernur DKI, Dokumen Kementerian, dan Testimoni Tokoh.  
   * *Footer Section:* Logo Sensus Ekonomi 2026 dan Slogan Resmi dengan latar belakang putih bersih.  
2. **Halaman Struktur & Tupoksi Orlap:**  
   * Manajemen koordinasi panitia (Koormat, Wakil, Seklap, Korwil, Sekwil, Bidang Pendukung).  
   * Komponen kontak terenkripsi berbasis kartu (*cards*) abu-abu muda dengan tombol aksi oranye.  
3. **Halaman Kanal Informasi & Media Promosi:**  
   * Layout grid minimalis untuk pembaruan informasi berkala dan video promosi tanpa elemen dekoratif gelap.  
4. **Halaman Bantuan & Call Center (Triage System):**  
   * Kolom pencarian solusi kasus berbingkai hitam/oranye tegas.  
   * Integrasi pelaporan otomatis via shortlink institusi (`[http://s.stis.ac.id/PertanyaanSE2026](http://s.stis.ac.id/PertanyaanSE2026)`).  
   * Akses Layanan Konseling UPK Resmi dan Konseling Sebaya Ruang Dialog BEM.

## **II. MATRIKS RISIKO, SOLUSI TEKNIS, DAN STATUS URGENSI**

### **1\. Risiko Infrastruktur: Kehilangan Jaringan dan Kuota Data di Lapangan**

* **Deskripsi Masalah:** Mahasiswa mendata di area *blank spot*. Jika portal memerlukan internet untuk memuat dokumen, surat tugas BPS tidak bisa ditunjukkan ke responden, memicu penolakan pendataan.  
* **Solusi Teknis:**  
  1. Konfigurasi **Progressive Web App (PWA)** menggunakan `@ducanh2912/next-pwa`.  
  2. Pindahkan dokumen krusial (Surat BPS DKI) dari Google Drive eksternal ke dalam direktori lokal proyek (`public/docs/surat-tugas-bps.png`) dengan kompresi gambar tinggi (\<500 KB). Hindari penggunaan `<iframe>` pihak ketiga.  
* **Status Urgensi:** **KRITIS (HIGHLY URGENT)**  
* **Alasan:** Legalitas adalah perisai utama petugas. Jika web gagal dimuat akibat kendala sinyal, operasional pendataan berhenti total.

### **2\. Risiko Kognitif: Visibilitas Layar di Bawah Sinar Matahari (Outdoor Glare)**

* **Deskripsi Masalah:** Penggunaan tema gelap (*Dark Mode*) atau kontras rendah membuat layar HP memantulkan bayangan (*glare*) saat digunakan di bawah terik matahari siang hari. Mahasiswa kesulitan membaca teks kuesioner dan solusi kasus.  
* **Solusi Teknis:** Ubah seluruh basis desain menjadi **High-Contrast Light Mode**. Gunakan latar belakang putih murni (`#FFFFFF`), teks hitam pekat (`#000000`), dan elemen penarik perhatian menggunakan warna Oranye Sensus (`#F27221`) dengan tingkat kontras rasio minimal 7:1 memenuhi standar WCAG AAA.  
* **Status Urgensi:** **KRITIS (HIGHLY URGENT)**  
* **Alasan:** Mempercepat durasi interaksi petugas di depan responden karena informasi dapat dibaca secara instan tanpa perlu mencari tempat teduh.

### **3\. Risiko Privasi: Kebocoran Data Kontak Internal & Dosen Pendamping**

* **Deskripsi Masalah:** Menampilkan nomor WhatsApp resmi struktur panitia pada domain publik mengundang risiko *scraping* oleh bot spam otomatis.  
* **Solusi Teknis:**  
  1. Implementasikan **NextAuth Google Provider** terbatas pada domain: `profile.email.endsWith('@stis.ac.id')`.  
  2. Enkripsi string nomor telepon menggunakan metode *Base64 Obfuscation* pada level kode (contoh: `"62812..."` disimpan sebagai `"NjI4..."`). Nomor baru didekode oleh JavaScript runtime hanya saat pengguna menekan tombol "Hubungi WA".  
* **Status Urgensi:** **KRITIS (HIGHLY URGENT)**  
* **Alasan:** Mencegah serangan spam dan gangguan pihak luar terhadap dosen dan panitia inti selama periode sensus.

### **4\. Risiko Kontradiksi Fitur: Ekspektasi Dynamic Content vs Rencana Deployment Statis**

* **Deskripsi Masalah:** Sistem harus bisa menerima input pelaporan masalah tanpa adanya database/backend berbayar.  
* **Solusi Teknis:** Alihkan beban arsitektur pengumpulan data ke Google Form institusi (`[http://s.stis.ac.id/PertanyaanSE2026](http://s.stis.ac.id/PertanyaanSE2026)`). Data otomatis terekap di Google Sheets panitia secara real-time tanpa kode backend di Vercel.  
* **Status Urgensi:** **TINGGI (URGENT)**  
* **Alasan:** Menjaga portal tetap berjalan gratis di Vercel murni frontend namun fungsionalitas rekapitulasi data tetap terpenuhi.

## **III. SPESIFIKASI SISTEM DESAIN (DESIGN SYSTEM COMPLIANCE \- LIGHT MODE)**

JSON

{

  "theme\_name": "Sensus Ekonomi 2026 High-Contrast Light Mode",

  "tokens": {

    "colors": {

      "background\_main": "\#FFFFFF (bg-white)",

      "background\_secondary": "\#F8FAFC (bg-slate-50)",

      "text\_primary": "\#000000 (text-black)",

      "text\_secondary": "\#334155 (text-slate-700)",

      "accent\_solid": "\#000000 (bg-black)",

      "interactive\_box": "\#F27221 (bg-orange-500)",

      "interactive\_text": "\#FFFFFF (text-white)"

    },

    "borders": {

      "standard": "1px solid \#E2E8F0 (border-slate-200)",

      "accent": "2px solid \#000000 (border-black)"

    },

    "typography": {

      "font\_family": "Inter, system-ui, sans-serif",

      "viewport\_meta": "width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no"

    }

  }

}

## **IV. IMPLEMENTASI KODE LOGIKA JALUR PUSAT BANTUAN (LIGHT MODE COMPLIANT)**

Berikut adalah contoh modul kode `app/bantuan/page.js` yang sudah disesuaikan dengan skema warna baru (Latar putih, teks hitam, tombol kotak oranye solid):

JavaScript

'use client';

import { useState, useMemo } from 'react';

const DATA\_QNA \= \[

  {

    id: 'q1',

    category: 'Metodologi',

    tags: \['menolak', 'tidak mau', 'sibuk'\],

    question: 'Bagaimana jika pelaku UMKM menolak keras didata dengan alasan sibuk?',

    answer: 'Tunjukkan Surat Tugas BPS dan Surat Himbauan Menteri Kemenparekraf/Koperasi UMKM. Jelaskan bahwa pendataan ini hanya memakan waktu 5-10 menit. Jika tetap menolak, catat di lembar kendala dan laporkan ke Korwil.'

  },

  {

    id: 'q2',

    category: 'Sistem',

    tags: \['pindah', 'alamat salah', 'tutup'\],

    question: 'Lokasi UMKM di target sampel ternyata sudah pindah alamat atau gulung tikar?',

    answer: 'Jangan hapus target. Gunakan fitur identifikasi permasalahan, pilih kategori "Perubahan Status Alamat" pada sistem rekap agar tercatat otomatis.'

  }

\];

const POPULAR\_TAGS \= \['Menolak', 'Pindah'\];

export default function BantuanPage() {

  const \[searchQuery, setSearchQuery\] \= useState('');

  const \[openAccordion, setOpenAccordion\] \= useState(null);

  const filteredQna \= useMemo(() \=\> {

    const query \= searchQuery.toLowerCase().trim();

    if (\!query) return DATA\_QNA;

    return DATA\_QNA.filter((item) \=\> 

      item.question.toLowerCase().includes(query) ||

      item.tags.some((tag) \=\> tag.toLowerCase().includes(query))

    );

  }, \[searchQuery\]);

  return (

    \<div className="min-h-screen bg-white text-black font-sans antialiased pb-12 max-w-md mx-auto border-x border-slate-200 shadow-sm"\>

      {/\* STICKY SEARCH HEADER \*/}

      \<div className="sticky top-0 bg-white/95 backdrop-blur-md pt-6 pb-4 px-4 border-b border-slate-200 z-30"\>

        \<h1 className="text-lg font-black tracking-tight text-black flex items-center gap-2"\>

          ⬛ Solusi Kasus Lapangan

        \</h1\>

        \<p className="text-xs text-slate-700 mt-0.5 mb-4"\>Pencarian instan untuk kendala pendataan UMKM.\</p\>

        

        \<div className="relative"\>

          \<input

            type="text"

            placeholder="Cari kata kunci: menolak, pindah..."

            value={searchQuery}

            onChange={(e) \=\> setSearchQuery(e.target.value)}

            className="w-full bg-white text-sm rounded-xl border-2 border-black px-4 py-3 pr-16 text-black placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-orange-500 transition"

          /\>

          {searchQuery && (

            \<button 

              onClick={() \=\> setSearchQuery('')}

              className="absolute right-2 top-1/2 \-translate-y-1/2 text-xs font-bold bg-black text-white px-2 py-1 rounded"

            \>

              Clear

            \</button\>

          )}

        \</div\>

        {/\* QUICK CLICK CHIPS \*/}

        \<div className="flex gap-2 mt-3 overflow-x-auto py-1"\>

          {POPULAR\_TAGS.map((tag) \=\> (

            \<button

              key={tag}

              onClick={() \=\> setSearchQuery(tag)}

              className={\`text-xs px-3 py-1.5 rounded-lg font-bold border transition ${

                searchQuery.toLowerCase() \=== tag.toLowerCase()

                  ? 'bg-orange-500 border-orange-500 text-white'

                  : 'bg-slate-100 border-slate-300 text-slate-900 hover:bg-slate-200'

              }\`}

            \>

              \#{tag}

            \</button\>

          ))}

        \</div\>

      \</div\>

      {/\* LIST REPOSITORI KASUS \*/}

      \<main className="px-4 mt-6 space-y-3"\>

        {filteredQna.length \> 0 ? (

          filteredQna.map((item) \=\> {

            const isOpen \= openAccordion \=== item.id;

            return (

              \<div key={item.id} className="border-2 border-black rounded-xl overflow-hidden bg-white"\>

                \<button

                  onClick={() \=\> setOpenAccordion(isOpen ? null : item.id)}

                  className="w-full text-left p-4 flex justify-between items-start gap-2 bg-slate-50"

                \>

                  \<div\>

                    \<span className="text-\[9px\] font-black tracking-wider px-2 py-0.5 rounded bg-black text-white uppercase"\>

                      {item.category}

                    \</span\>

                    \<h3 className="text-sm font-bold text-black mt-1.5 leading-snug"\>{item.question}\</h3\>

                  \</div\>

                  \<span className="text-black font-black text-xs pt-1"\>{isOpen ? '▲' : '▼'}\</span\>

                \</button\>

                {isOpen && (

                  \<div className="p-4 border-t-2 border-black bg-white"\>

                    \<p className="text-xs text-slate-800 leading-relaxed"\>{item.answer}\</p\>

                  \</div\>

                )}

              \</div\>

            );

          })

        ) : (

          /\* FALLBACK UI \*/

          \<div className="text-center py-12 border-2 border-dashed border-slate-300 rounded-2xl bg-slate-50"\>

            \<p className="text-sm text-slate-800 font-bold"\>Kasus tidak ditemukan.\</p\>

            \<a

              href="http://s.stis.ac.id/PertanyaanSE2026"

              target="\_blank"

              rel="noopener noreferrer"

              className="mt-4 inline-block bg-orange-500 text-white text-xs font-black py-3 px-6 rounded-xl shadow-sm active:scale-95 transition"

            \>

              LAPORKAN KASUS BARU VIA G-FORM

            \</a\>

          \</div\>

        )}

      \</main\>

    \</div\>

  );

}

## **V. ALUR VALIDASI IMPLEMENTASI (CHECKLIST RILIS)**

Sebelum portal disebarkan ke seluruh mahasiswa STIS tingkat 2, tim TI wajib memvalidasi 3 indikator ini:

1. **Uji Keterbacaan Monitor Terik (Gleam Test):** Buka aplikasi di bawah sinar matahari langsung, pastikan teks hitam di atas latar putih terbaca sempurna tanpa perlu menaikkan kecerahan layar ke 100%.  
2. **Uji Click Target Size:** Pastikan area tombol kotak oranye pada *landing page* memiliki ukuran minimal `48x48px` agar mudah ditekan satu tangan oleh jari petugas yang sedang memegang papan jalan/kuesioner fisik di lapangan.  
3. **Verifikasi Cache Offline:** Pastikan saat mode pesawat aktif, seluruh kotak tombol oranye di halaman utama tetap aktif dan gambar surat tugas ter-render sempurna dari direktori lokal.

### **5\. ALUR VALIDASI RILIS (CHECKLIST STAGING)**

Sebelum portal ini diluncurkan secara massal ke grup angkatan, tim TI panitia wajib melakukan uji coba manual (*staging test*) dengan kriteria kelulusan sebagai berikut:

* \[ \] **Uji Offline PWA:** Membuka website, mematikan mode pesawat HP, me-refresh halaman, dan memastikan Surat Tugas di /docs/surat-tugas-bps.png tetap tampil tanpa putus jaringan.  
* \[ \] **Uji Batas Domain OAuth:** Mencoba masuk menggunakan email di luar @stis.ac.id. Sistem wajib menolak dan mengarahkan ke halaman kesalahan akses.  
* \[ \] **Uji Kecepatan Fuzzy Search:** Memastikan pengetikan kata kunci pada kolom pencarian langsung menyaring daftar solusi secara dinamis dalam waktu \<100ms tanpa delay atau lag pada ponsel berspesifikasi rendah.  
* \[ \] **Uji Keamanan WA Bot:** Memeriksa apakah nomor telepon panitia/dosen dapat dicari di tab *Elements Inspect Tool* browser. Lulus uji jika yang tertulis di kode sumber hanyalah teks terenkripsi Base64.