i=0
total=0
lagi='Y'
while lagi=='Y':
    i = int(input('Input Angka : '))
    #total = total+1
    total += i
    
    print('Total Sekarang', total)
    lagi = str(input('Lagi? : ')).upper()


