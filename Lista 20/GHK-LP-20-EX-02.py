import random as rn
valores=[0,0,0,0,0,0,0]
numeros=[]

for i in range(100):
    x=rn.randint(1,6)
    numeros.append(x)
    valores[x]+=1

for i in range(1,7):
    print(f"O número {i} caiu {valores[i]} vezes")

print(f"\nA ordem dos números obtidos foi:\n{numeros}")