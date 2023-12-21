print("Program menghitung saldo dengan tambahan bunga")
print("="*50)
# Input saldo awal, bunga (dalam persen), dan jangka waktu (dalam bulan)
saldo_awal = float(input("Masukkan saldo awal: "))
bunga = float(input("Masukkan bunga bulanan (dalam persen): "))
jangka_waktu_bulan = int(input("Masukkan jangka waktu (dalam bulan): "))

# Menggunakan perulangan for untuk menghitung saldo akhir setiap bulan
for bulan in range(1, jangka_waktu_bulan + 1):
    saldo_awal += saldo_awal * bunga/100
    print(f"Saldo Akhir bulan ke {bulan} = {saldo_awal}")



