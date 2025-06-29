# Proyek Akhir : Menyelesaikan Permasalahan Perusahaan Edutech - Jaya Jaya Institute

## 1. Business Understanding 

### 1.1 Latar Belakang

Jaya Jaya Institute merupakan lembaga pendidikan yang telah berdiri sejak tahun 2000 dan dikenal sebagai penghasil lulusan berprestasi di berbagai bidang. Meski demikian, masih terdapat sejumlah mahasiswa yang tidak berhasil menyelesaikan studi mereka atau mengalami putus kuliah (dropout). 

Tingginya angka putus kuliah menjadi tantangan serius bagi institusi ini. Oleh karena itu, Jaya Jaya Institute berupaya untuk mengidentifikasi mahasiswa yang berisiko mengalami dropout sejak dini, sehingga mereka dapat diberikan bimbingan dan pendampingan secara khusus. 

## 2. Permasalahan Bisnis 

1. Tingginya Angka Siswa yang Mengundurkan Diri, jumlah siswa yang tidak melanjutkan pendidikan cukup tinggi, sehingga berdampak negatif terhadap reputasi serta daya saing institusi. Kondisi ini dapat menurunkan persepsi terhadap kualitas pendidikan dan mengurangi minat calon pendaftar.
2. Ketiadaan Sistem Pemantauan yang Optimal, Institusi belum memiliki pemantauan kinerja siswa secara real-time, sehingga menyulitkan dalam mengidentifikasi siswa yang berisiko keluar lebih awal. Akibatnya, langkah intervensi untuk mencegah dropout menjadi kurang efektif.
3. Kendala dalam Mengetahui Penyebab Mengundurkan Diri, Jaya Jaya Institute masih belum sepenuhnya memahami faktor-faktor utama yang mendorong siswa untuk berhenti studi. Tanpa wawasan yang menyeluruh, institusi kesulitan dalam merancang strategi penanggulangan yang tepat sasaran.

## 3. Cakupan Proyek 

1. Persiapan Data dan Exploratory Data Analysis (EDA)
   Melakukan proses pengumpulan, pembersihan, dan analisis data guna memperoleh       pemahaman menganai faktor-faktor yang mempengaruhi terjadinya dropout. 
2. Pembuatan Model
   Merancang model prediktif berbasis machine learning untuk mengidentifikasi         siswa yang memiliki potensi tinggi mengalami dropout.
3. Evaluasi Model
   Mengukut dan menilai kinerja model guna memastikan tingkat akurasi dalam           memprediksi siswa yang berisiko tidak menyelesaikan studi. 
4. Pengembangan Dashboard
   Membangun dashboard interaktif yang memungkinkan pihak Jaya Jaya Institut          memantau perkembangan akademik siswa secara langsung dan melakukan tindakan        intervensi secara tepat waktu.
5. Pemberian Rekomendasi
   Menyusun saran strategis berdasarkan temuan analisis guna menekan angka dropout    serta mendukung peningkatan mutu pendidikan di Jaya Jaya Institut.

## 4. Persiapan

### 4.1 Sumber : 

Dataset yang digunakan dalam proyek ini merupakan data terkait informasi performa siswa, serta atribut demografis seperti jenis kelamin, kelompok etnis, tingkat pendidikan orang tua, dll. Data ini digunakan untuk analisis dan pengembangan model prediksi siswa yang berpotensi mengalami dropout.

[[🔗 Link Dataset - Student Performance]](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

### 4.2 Setup Environment 

Gunakan langkah berikut untuk mengatur lingkungan kerja : 

1. Buka Terminal atau CMD

Jalankan terminal atau command prompt pada perangkat Anda.

2. Setup Environment - Anaconda

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```
3. Setup Environment - Shell/Terminal

```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```
## 5. Business Dashboard

Proyek ini dirancang untuk mengembangkan sistem prediktif yang dapat mendukung Jaya Jaya Institut dalam mengenali mahasiswa yang berpotensi mengalami putus studi (dropout). Sistem ini memanfaatkan berbagai indikator, seperti karakteristik individu, pencapaian akademik, dan faktor sosial-ekonomi, guna memperkirakan kemungkinan seorang mahasiswa tidak melanjutkan pendidikannya.

Salah satu komponen utama dalam sistem ini adalah Business Dashboard, yang berfungsi untuk menyajikan visualisasi data secara informatif, sehingga memudahkan pihak institusi dalam mengambil keputusan berbasis data terkait risiko dropout mahasiswa.

### 5.1 Penjelasan Proyek 

Dashboard ini dirancang untuk menyajikan visualisasi yang informatif mengenai berbagai faktor yang dapat memengaruhi status dropout mahasiswa di Jaya Jaya Institut. Berdasarkan data yang tersedia, dashboard ini bertujuan untuk mendukung pihak institusi dalam mengenali serta memantau faktor-faktor yang berkaitan dengan potensi mahasiswa tidak menyelesaikan studi mereka.

1. Key Performance Indicators (KPI)

   Bagian ini menyajikan ringkasan metrik utama yang berkaitan dengan data mahasiswa, meliputi :
   - Total Students : Jumlah keseluruhan mahasiswa yang terdaftar di institusi.
   - Total Student Dropout : Jumlah mahasiswa yang tercatat keluar atau tidak melanjutkan studi.
   - Student Dropout Rate : Persentase mahasiswa yang dropout dibandingkan dengan jumlah total mahasiswa.
   - Average Age : Rata-rata umur mahasiswa.

2. Visualisasi Data Menggunakan Diagram

   Bagian ini menyajikan representasi visual untuk memperlihatkan distribusi mahasiswa yang mengalami dropout berdasarkan berbagai kategori penting, antara lain:
   - Student berdasarkan Status : Menggambarkan proporsi status mahasiswa secara keseluruhan, seperti dropout, lulus, dan masih aktif.
   - Student Dropout berdasarkan Marital Status : Membandingkan tingkat dropout antara mahasiswa berdasarkan status pernikahan mereka.
   - Student Dropout berdasarkan Gender : Menunjukkan distribusi mahasiswa dropout berdasarkan jenis kelamin.
   - Student Dropout berdasarkan Scholarship Holder : Menampilkan hubungan antara status penerima beasiswa dan kemungkinan mahasiswa mengalami dropout.
   - Student Dropout by Course : Menampilkan jumlah mahasiswa dropout berdasarkan jenis program studi yang diambil.
   - Student Dropout berdasarkan Nacionality :  Menampilkan jumlah mahasiswa dropout berdasarkan kewarganegaraan. 

Berikut link dashboard : https://public.tableau.com/views/STUDENTSDROPOUTANALYTICSDASHBOARD/STUDENTSDROPOUTANALYTICDASHBOARD?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## 6. Menjalankan Sistem Machine Learning

