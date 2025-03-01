n=int(input("Digite um numero: "))
n=2*n-1

c=1
a=0

while c<=n:
    a+=1/c
    c+=2
print(a)