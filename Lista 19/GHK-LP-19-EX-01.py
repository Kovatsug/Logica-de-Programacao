l=[]
lp=[]
li=[]

for i in range(20):
    n=int(input("Digite um numero inteiro: "))
    l.append(n)
    if n %2==0:
        lp.append(n)
    if n%2==1:
        li.append(n)

print(f"a lista é :\n{l}\nos numeros pares são:\n{lp}\nos numeros impares são:\n{li}")