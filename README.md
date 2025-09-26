# soal-acak-matematika
Membuat soal acak matematika dengan python dan \LaTeX

## yang diperlukan
- python dengan paket: numpy, sympy, matplotlib
- latex

## caranya
Ini hanya contoh saja. Akan dibuat 30 tipe soal dengan masing-masing ada `kode soal` yang berbeda-beda, ada di bagian setelah petunjuk pengerjaan soal. Berisi soal-soal yang bisa dibangkitkan dengan tiap nomor berisi soal yang sama, tapi angka atau simbol yang berbeda-beda. Bilangannya dibangkitkan dengan `np.random.choice()` atau `np.random.randint()` sesuai yang dibutuhkan. Akan tersedia 5 pilihan (ABCDE) di setiap nomornya.

## yang perlu diperhatikan
1. Masih ada kemungkinan menampilkan pilihan jawaban yang sama antara A, B, C, dan D. Bisa diperbaiki di bagian itu.
2. Untuk mengoreksi lembar jawabannya, dan pembuatan lembar jawabannya (LJK) bisa menggunakan program omr yang dari sini: https://github.com/muktyas/omr-3kolom-30soal.
