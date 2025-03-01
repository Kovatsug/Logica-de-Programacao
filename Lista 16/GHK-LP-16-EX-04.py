n=int(input("Escreva um numero inteiro igual ou maior do que 2: "))
fator=2

if n<2:
    print("erro")

while fator<=n:
    
    if n%fator==0:
        print(fator)
        n=n/fator
    else:
        fator+=1