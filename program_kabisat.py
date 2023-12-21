print('program menentukan tahun Kabisat')
print('-'*50)
tahun = int(input("Masukan Tahun :"))
if (tahun % 4 == 0 and tahun%100 != 0) or (tahun %100==0 and tahun%400==0):
    print("Tahun ini adalah kabisat")
else :
    print("Tahun ini bukan kabisat")
    
