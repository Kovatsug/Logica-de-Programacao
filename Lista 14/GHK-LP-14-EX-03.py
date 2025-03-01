n=0
c=0
numeros=0

while n!="":
    n=(input("Digite um numero: "))
    if n=="":
        break
    c+=1
    numeros+=int(n)

print(f"{c} numeros foram fornecidos, a media é {numeros/c}")
