n=int(input("Digite um numero: "))

digitos=1

while n>=10:
    n=n/10
    digitos+=1
print(digitos)