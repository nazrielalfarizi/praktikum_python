print('program menghitung nilai akhir')
print('-'*50)
nilai_tugas=float(input('Nilai tugas = '))
nilai_uts=float(input('Nilai uts = '))
nilai_uas=float(input('Nilai uas = '))
nilai_akhir=(0.30*nilai_tugas)+(0.30*nilai_uts)+(0.40*nilai_uas)
if nilai_akhir>=80 and nilai_akhir<=100:
    indeks='A'
    keterangan='Sangat baik'
elif nilai_akhir>=68 and nilai_akhir<80:
    indeks='B'
    keterangan='Baik'
elif nilai_akhir>=56 and nilai_akhir<68:
    indeks='C'
    keterangan='Cukup'
elif nilai_akhir>=45 and nilai_akhir<56:
    indeks='D'
    keterangan='Kurang'
elif nilai_akhir>=0 and nilai_akhir<45:
    indeks='E'
    keterangan='Sangat kurang'
print('Nilai akhir =',nilai_akhir)
print('Indeks nilai =',indeks)
print('Keterangan =',keterangan)
