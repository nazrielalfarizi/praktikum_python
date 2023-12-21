print("Program mensimulasikan transaksi")
print("="*50)
saldo_awal = 10000  #Saldo awal yang harus disisakan
saldo = saldo_awal
lanjut_transaksi = 'Y'
print(f"Saldo saat ini: Rp {saldo}")


while saldo >= 10000 and lanjut_transaksi=='Y':
    kode_transaksi = int(input("Masukkan kode transaksi (0: Setor, 1: Tarik): "))

    if kode_transaksi == 0:
        jumlah_setoran = int(input("Masukkan jumlah uang yang akan disetor: "))
        saldo += jumlah_setoran
        print(f"Saldo saat ini: Rp {saldo}")
        lanjut_transaksi = str(input("Lanjut transaksi (Y: Ya, T: Tidak): ")).upper()
        print("="*50)
    elif kode_transaksi == 1:
        jumlah_penarikan = int(input("Masukkan jumlah uang yang akan ditarik: "))
        if jumlah_penarikan > saldo - 10000:
            print("Penarikan melebihi saldo yang tersedia atau saldo minimum yang harus disisakan.")
        else:
            saldo -= jumlah_penarikan
            print(f"Saldo saat ini: Rp {saldo}")
            lanjut_transaksi = str(input("Lanjut transaksi (Y: Ya, T: Tidak): ")).upper()
            print("="*50)
    else:
        print("Kode transaksi tidak valid. Masukan 0 untuk setor dan 1 untuk tarik uang")
        ulangi = str(input("Lanjut transaksi (Y: Ya, T: Tidak): ")).upper()
        while lanjut_transaksi !='T' and lanjut_transaksi !='Y':
            print("Input tidak valid")
            ulangi = str(input("Lanjut transaksi (Y: Ya, T: Tidak): ")).upper()

print("Transaksi selesai.")
