import math
#Sub Program function Luas Keliling Lingkaran
def lk_lingkaran(radius):
    luas = math.pi * radius**2

    keliling = 2 * math.pi * radius

    return luas, keliling

#Sub Program function Luas Keliling Bujursangkar
def lk_bujursangkar(sisi):
    luas = sisi * sisi

    keliling = 4 * sisi

    return luas, keliling

#Sub Program function Luas Keliling Persegi Panjang
def lk_persegipanjang(panjang, lebar):
    luas = panjang * lebar

    keliling = 2 * (panjang + lebar)

    return luas, keliling

#Sub Program function Luas Keliling Segitiga
def lk_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi

    sisi_miring = math.sqrt(alas**2 + tinggi**2)

    keliling = alas + tinggi + sisi_miring

    return luas, keliling

#Program Utama
print('Aplikasi Perhitungan Luas dan Keliling')
print('-'*50)
print('1. Lingkaran')
print('2. Bujursangkar')
print('3. Persegi Panjang')
print('4. Segitiga')
print('0. Keluar')
print('-'*50)
pilihan = int(input('Pilihan anda ? '))
if pilihan == 1 :
    print('Perhitungan Luas dan Keliling Lingkaran')
    radius_input = float(input("Masukkan nilai radius lingkaran: "))
    luas, keliling = lk_lingkaran(radius_input)
    lk_lingkaran(radius_input)
    print(f"Luas lingkaran: {luas}")
    print(f"Keliling lingkaran: {keliling}")
elif pilihan == 2 :
    print('Perhitungan Luas dan Keliling Bujursangkar')
    sisi_input = float(input("Masukkan nilai sisi bujursangkar: "))
    luas, keliling = lk_bujursangkar(sisi_input)
    lk_lingkaran(sisi_input)
    print(f"Luas Bujursangkar: {luas}")
    print(f"Keliling Bujursangkar: {keliling}")
elif pilihan == 3 :
    print('Perhitungan Luas dan Keliling Persegi Panjang')
    panjang_input = int(input("Masukkan nilai panjang: "))
    lebar_input = int(input("Masukkan nilai lebar: "))
    luas, keliling = lk_persegipanjang(panjang_input,lebar_input)
    lk_persegipanjang(panjang_input,lebar_input)
    print(f"Luas lingkaran: {luas}")
    print(f"Keliling lingkaran: {keliling}")
elif pilihan == 4 :
    print('Perhitungan Luas dan Keliling Segitiga')
    alas_input = int(input("Masukkan nilai alas: "))
    tinggi_input = int(input("Masukkan nilai tinggi: "))
    luas, keliling = lk_segitiga(alas_input,tinggi_input)
    lk_segitiga(alas_input, tinggi_input)
    print(f"Luas lingkaran: {luas}")
    print(f"Keliling lingkaran: {keliling}")
elif pilihan == 0 :
    print('Program telah dikeluarkan')
    SystemExit

    






    