print('program menghitung status umur untuk pemilu')
print('-'*50)
umur = int(input('umur :'))
if umur < 17 :
    status_nikah = str(input("status nikah[Y/T] :"))
    if status_nikah.upper() == "Y" :
        print('Anda berhak ikut pemilu')
    else :
        print('Anda tidak berhak ikut pemilu')
else :
    print('Anda berhak ikut pemilu')
    
