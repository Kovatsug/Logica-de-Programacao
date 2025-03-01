a=0

n=int(input("Digite seu número: "))

for i in range(1, n+1):
    a+= (n-(i-1))/n

print(a)