Nama: Farhan Hakim
NIM: H1D024064

## 🛠️ Alur Utama & Cara Kerja Program (`main.py`)

Script `main.py` mengintegrasikan seluruh modul logika untuk menjalankan siklus evolusi Algoritma Genetika.

1. **Inisialisasi Masalah**: Menentukan daftar barang (nama, harga, bobot) serta parameter GA (generasi, populasi, probabilitas crossover, dan mutasi).
2. **Siklus Evolusi**: Untuk setiap generasi, program melakukan evaluasi fitness, seleksi orang tua, perkawinan silang (*crossover*), dan mutasi gen.
3. **Pencatatan data**: Menyimpan nilai fitness tertinggi, terendah, dan rata-rata di setiap generasi.
4. **Visualisasi**: Menghasilkan grafik konvergensi algoritma (`fitness_plot.png`).

---

## 📂 Penjelasan Fungsi & Cara Kerja Tiap Script

### 1. `inisiasipopulasi.py` (Pembentukan Solusi Awal)
Script ini bertanggung jawab untuk membentuk kumpulan solusi acak generasi pertama.
* **`inisialisasi_populasi(jumlah_populasi, jumlah_gen)`**
  * **Cara Kerja**: Membuat list dua dimensi berukuran `jumlah_populasi × jumlah_gen`. Setiap individu (kromosom) direpresentasikan sebagai array biner acak (contoh: `[1, 0, 1, 1, 0]`). Angka `1` berarti barang diambil, dan `0` berarti ditinggal.

### 2. `EvaluasiFitness.py` (Penilaian Kualitas Solusi)
Modul ini mengukur seberapa baik suatu individu dalam memecahkan masalah tanpa melanggar batasan.
* **`hitung_fitness(kromosom, barang, kapasitas_tas)`**
  * **Cara Kerja**: Melakukan iterasi pada kromosom. Jika gen bernilai `1`, bobot dan harga barang ditambahkan ke total akumulasi.
  * **Aturan Penalti**: Jika total bobot **melebihi** `kapasitas_tas`, fungsi langsung mengembalikan nilai `0` (solusi dianggap cacat/gagal). Jika aman, nilai total harga dijadikan nilai fitness.

### 3. `selection.py` (Seleksi Induk/Parent)
Berfungsi memilih individu berkualitas untuk diwariskan ke generasi berikutnya. Menyediakan dua metode:
* **`roulette_wheel_selection(populasi, fitness_populasi)`**
  * **Cara Kerja**: Membuat proporsi peluang berdasarkan nilai fitness (mirip papan roda kasino). Semakin besar fitness suatu individu, semakin besar peluangnya terpilih.
* **`tournament_selection(populasi, fitness_populasi, k=3)`**
  * **Cara Kerja**: Memilih `k` individu secara acak dari populasi, lalu mengadu nilai fitness-nya. Individu dengan fitness tertinggi di dalam kelompok kecil tersebut keluar sebagai pemenang.

### 4. `crossover.py` (Rekombinasi Genetik)
Menggabungkan sifat dari dua induk untuk menghasilkan dua anak (*offspring*) baru. Menyediakan tiga metode:
* **`one_point_crossover(parent1, parent2)`**: Memotong biner di satu titik acak, lalu menukar potongan bagian belakang antar induk.
* **`two_point_crossover(parent1, parent2)`**: Memotong di dua titik acak, lalu menukar segmen gen yang berada di antara kedua titik tersebut.
* **`uniform_crossover(parent1, parent2)`**: Membuat *mask* biner acak untuk menentukan gen anak diambil dari parent 1 atau parent 2 secara independen tiap indeksnya.

### 5. `mutation.py` (Mutasi Gen/Variasi Baru)
Memberikan perubahan acak pada gen anak untuk menjaga variasi populasi agar tidak terjebak di optimal lokal. Menyediakan tiga metode:
* **`swap_mutation(kromosom)`**: Memilih dua posisi gen secara acak pada satu kromosom lalu menukar posisinya.
* **`inversion_mutation(kromosom)`**: Membalikkan urutan sub-array gen di antara dua titik acak.
* **`uniform_mutation(kromosom, mutation_rate=0.1)`**: Menjelajahi setiap gen individu; jika angka acak berada di bawah `mutation_rate`, bit gen tersebut akan di-flip (`0` jadi `1`, atau `1` jadi `0`).

---

## 📊 Output Hasil Eksperimen

Setelah eksekusi selesai, program akan menampilkan output teks di terminal berupa:
* **Nilai Fitness Terbaik**: Total keuntungan maksimal yang bisa didapatkan.
* **Total Bobot**: Beban riil barang bawaan yang terpilih.
* **Barang Terpilih**: Daftar nama barang yang berhasil dimasukkan ke dalam tas.

Program juga otomatis menyimpan grafik performa (`fitness_plot.png`) yang menggambarkan pergerakan nilai fitness tertinggi (biru), rata-rata (merah), dan terendah (kuning) di sepanjang generasi.