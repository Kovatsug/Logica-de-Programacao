a=0

n=int(input("Digite seu número: "))
n=n*2-1

for i in range (1, n+1, 2):
   a+= 1/i

print(a)