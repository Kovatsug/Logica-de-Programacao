n=int(input("Escreva um numero: "))

c=1
a=0

while c<=n:
    a+=(n-(c-1))/c
    c+=1

print(a)