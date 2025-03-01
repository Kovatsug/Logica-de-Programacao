n=0
s=0

while True:
    x=input("Digite um numero: ")
    if x=="":
        break
    
    if int(x)>0:
        s+=int(x)

    elif int(x)<0:
        n+=1

print(f"a soma dos numeros é {s} e a quantidade de numeros negativos é {n}")