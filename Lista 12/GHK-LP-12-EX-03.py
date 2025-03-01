a=int(input("Escolha o primeiro numero para multiplicar: "))
b=int(input("Escolha o segundo numero para multiplicar: "))
x=0

for i in range(abs(b)):
    x+=a

if (a<0 and b>0) or (a>0 and b<0):
    x = -x

print(f"O resultdo da multiplicação é {x}")