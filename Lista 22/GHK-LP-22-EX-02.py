import random

def sorteia_dado():
    return random.randint(1,6)

numeros=[0,0,0,0,0,0]

for i in range(1000000):
    numeros[sorteia_dado()-1]+=1


for i in range(1,7):
    print(f"Numeros {i}: {numeros[i-1]}\t\t{numeros[i-1]*100/1000000}%")