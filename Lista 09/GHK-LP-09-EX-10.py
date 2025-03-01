s=int(input("Você quer a solução 1 ou 2? "))

if s==1:
    for i in range(100,-1,-5):
        print(i)

elif s==2:
    n=105
    for i in range(100):
        n=n-5
        print(n)
        if n==0:
            break