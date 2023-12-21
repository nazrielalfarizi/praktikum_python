#sub program bilangan ganjil
def tampil_bil_ganjil(nilai_awal,nilai_akhir:int):
    for i in range(nilai_awal,nilai_akhir+1):
        if i%2 !=0:
            print(i, end=' ')
            
#sub program jumlah ganjil
def jumlah_ganjil(nilai_awal,nilai_akhir:int):
    jumlah=0
    for i in range(nilai_awal,nilai_akhir+1):
        if i%2 !=0:
            jumlah=jumlah+i
    return jumlah
            
#sub program bilangan genap
def tampil_bil_genap(nilai_awal,nilai_akhir:int):
    for i in range(nilai_awal,nilai_akhir+1):
        if i%2 ==0:
            print(i, end=' ')

#sub program jumlah genap
def jumlah_genap(nilai_awal,nilai_akhir:int):
    jumlah=0
    for i in range(nilai_awal,nilai_akhir+1):
        if i%2 ==0:
            jumlah=jumlah+i
    return jumlah


#Program Utama
lagi = 'y'
while lagi == 'y':
    print('Program Bilangan Ganjil Genap')
    print('-'*50)
    print('1. Menampilkan Bilangan Ganjil diantara 2 nilai')
    print('2. Menampilkan Bilangan Genap diantara 2 nilai')
    print('3. Menampilkan Total Bilangan Ganjil diantara 2 nilai')
    print('4. Menampilkan Total Bilangan Genap diantara 2 nilai')
    print('-'*50)
    pilihan = int(input('Pilihan Anda : '))
    awal = int(input('Masukan nilai awal :'))
    akhir = int(input('Masukan nilai akhir :'))
    if pilihan == 1:
        print(f'Bilangan Ganjil antara {awal} s.d {akhir} : ')
        tampil_bil_ganjil(awal,akhir)
    elif pilihan == 2:
        print(f'Bilangan Genap antara {awal} s.d {akhir} : ')
        tampil_bil_genap(awal,akhir)
    elif pilihan == 3:
        print(f'Total Bilangan Ganjil antara {awal} s.d {akhir} : {jumlah_ganjil(awal,akhir)}')
    elif pilihan == 4:
        print(f'Total Bilangan Genap antara {awal} s.d {akhir} : {jumlah_genap(awal,akhir)}')
    lagi = str(input('Lagi?'))
