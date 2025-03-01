while True:
    n1=input("Escreva o primeiro numero: ")
    n2=input("Escreva o segundo numero: ")

    if len(n2)!=len(n1):
        print("Escreva numeros com a mesma quantidade de algarismos!")    
        continue

    else:
        for i in range(len(n1)):
            if n1[i]<n2[i]:
                x=True
            else:
                x=False
                break
    break

def HelloWorld(c):
    print(c)

HelloWorld(x)


