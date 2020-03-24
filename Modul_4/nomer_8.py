from random import randint

quiz = randint(1, 100)
jawab = 0
count = 1

print('Saya menyimpan angka bulat antara 1 sampai 100. anda punya 7x kesempatan. coba tebak')
while jawab != quiz and count < 8:
    jawab = int(input('Masukkan tebakan ke-{}:>'.format(count)))
    if jawab == quiz:
        print('Ya. Anda benar')
    elif jawab < quiz:
        print('Itu terlalu kecil. Coba lagi')
    else:
        print('Itu terlalu besar. Coba lagi')
    count += 1

# Karena menggunakan konsep Big-O. Dimana yang dipakai
# adalah rumus O(log n) dengan rincian 1 = 1, 2 = 2, 4 = 3, 10 = 4, 100 = 7, 1000=10.
# Di mana log berasal dari pangkat log berbasis 2. Dengan begitu dapat mengetahui jumlah
# maksimal tebakan.
# Untuk pola sendiri:
#         apabila ingin menebak angka 70
        
#         a = nilai tebakan pertama // 2
#         tebakan selanjutnya = nilai tebakan "lebih dari" + a
#         *jika hasil tebakan selanjutnya "kurang dari", maka nilai yang dipakai
#         tetap nilai lebih dari sebelumnya*
#         a = a // 2
#     Simulasi
#         tebakan ke 1: 50 (mengambil nilai tengah) jawaban= "lebih dari itu"
#         tebakan ke 2: 75 (dari 50 + 25) jawaban = "kurang dari itu"
#         tebakan ke 3: 62 (dari 50 + 12) jawaban = "lebih dari itu"
#         tebakan ke 4: 68 (dari 62 + 6) jawaban = "lebih dari itu"
#         tebakan ke 5: 71 (dari 68 + 3) jawaban = "kurang dari itu"
#         tebakan ke 6: 69 (dari 68 + 1) jawaban = "lebih dari itu"
#         tebakan ke 7: antara 71 dan 69 hanya ada 1 angka = 70!!!

