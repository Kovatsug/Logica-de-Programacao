neg=0
soma=0

for i in range(20):
    n=int(input("escreva um numero: "))
    if n<0:
        neg=neg+1
    else:
        soma=soma+n

print(f"a soma dos numeros positivos é: {soma}\nA quantidade de numeros negativos é: {neg}")


