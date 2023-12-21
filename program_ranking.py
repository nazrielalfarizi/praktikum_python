print("program menentukan berhak atau tidak mendapat hadiah")
print("-"*60)
ranking = int(input("ranking: "))
rata2 = float(input("rata2: "))
if (ranking==1) or (rata2>=8):
    print("anak berhak mendapat hadiah")
else:
    print("anak tidak berhak mendapat hadiah")
