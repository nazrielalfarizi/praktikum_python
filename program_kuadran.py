print("program menentukan kuadrat berdasarkan koordinat X dan Y")
print("-"*60)
x = float(input("x: "))
y = float(input("y: "))
if x>0 and y>0:
    kuadran = "kuadran 1"
elif x<0 and y>0:
    kuadran = "kuadran 2"
elif x<0 and y<0:
    kuadran = "kuadran 3"
elif x>0 and y<0:
    kuadran = "kuadran 4"
elif x!=0 and y==0:
    kuadran = "sumbu X"
elif x==0 and y!=0:
    kuadran = "sumbu Y"
elif x==0 and y==0:
    kuadran = "titik pusat"
print(f'koordinat ({x},{y}) berada di,{kuadran}')
