n1=int(input("Digite o primeiro numero: "))
n2=int(input("Digite o segundo numero: "))
n3=int(input("Digite o terceiro numero: "))

if n1<n2 and n1<n3:
    menornumero=n1
elif n2<n1 and n2<n3:
    menornumero=n2
elif n3<n1 and n3<n2:
    menornumero=n3


    
print(f"o menor numero é: {menornumero}")