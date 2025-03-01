def imprimir(x):
    print(x)

n=input("Escreva uma string: ")

for i in range(-1,-1-len(n),-1):
    imprimir(n[i:])