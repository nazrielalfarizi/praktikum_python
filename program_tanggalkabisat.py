print('program validasi tanggal')
print('-'*50)
tanggal = int(input("Masukan Tanggal 1 s.d 31 :"))
bulan = int(input("Masukan Bulan 1 s.d 12 :"))
tahun = int(input("Masukan Tahun :"))
if bulan>=1 and bulan<=12:
    if(bulan == 1 or bulan == 3 or bulan == 5 or bulan ==7 or bulan == 8 or bulan == 10 or bulan == 12) and (tanggal>= 1 and  tanggal<=31):
        print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah valid.")
    elif(bulan == 4 or bulan == 6 or bulan == 9 or bulan ==11) and (tanggal>= 1 and  tanggal<=30):
        print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah tidak valid.")
    elif bulan == 2:
        if (tahun % 4 == 0 and tahun%100 != 0) or (tahun %100==0 and tahun%400==0):
            if tanggal >= 1 and tanggal <= 29:
                print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah valid.")
            else:
                print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah tidak valid.")
        else:
            if tanggal >= 1 and tanggal <= 28:
                print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah valid.")
            else:
                print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah tidak valid.")
    else:
        print("Tanggal yang Anda masukkan tidak valid.")
else :
     print("Bulan tidak valid")
