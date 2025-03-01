s=int(input("Você quer a solução 1 ou 2? "))

if s == 1:
    for i in range(-5,6):
        print(i)

elif s==2:
    n=-6
    for i in range(100):
        n=n+1
        print(n)
        if n==5:
            break


else:
    print("Tente de novo, escolha 1 ou 2")