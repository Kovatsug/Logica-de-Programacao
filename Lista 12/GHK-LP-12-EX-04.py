x=0
y=1

n=int(input("Quantos termos da série de Fibonacci você quer? "))

for i in range(n):
    print(x)
    y+=x
    x=y-x
