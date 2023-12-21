nama = 'Nazriel' #Identifier global
#Procedure Tulis nama
def tulis_nama():
    print(f'Nama saya {nama}')
    print('Saya tinggal di Bandung')

#Procedure Tulis nama berulang
def tulis_nama_berulang(N):
    for i in range(1,N+1):
        print(f'{i} Nama saya {nama}')
    tulis_nama()

#Function jumlah deret
def jumlah_deret(N):
    jumlah = 0
    for i in range(1,N+1):
        jumlah += i
    return jumlah

#function besar bunga
def bunga (awal,persen,waktu):
    return awal * (1+persen/100)**waktu

#Program Utama
bbunga = bunga(persen=2,awal=100000,waktu=4) #argumen secara tidak berurutan dengan parameter
print(f'Hasil Perhitungan {bbunga}')
p_ulang= int(input('Masukan jumlah deret : '))
print(f'Jumlah deret 1 s.d {p_ulang} = {jumlah_deret(p_ulang)}')
tulis_nama()
j_ulang= int(input('Masukan jumlah pengulangan : ')) #input argumen ke parameter secara tak langsung
tulis_nama_berulang(j_ulang)
print(nama)
