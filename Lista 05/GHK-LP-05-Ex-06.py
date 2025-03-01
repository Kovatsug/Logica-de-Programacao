a=int(input("Escolha o primeiro numero: "))
b=int(input("Escolha o segundo numero: "))

if a>b:
    if a%b==0:
        print(f"os numeros {b} e {a} são multiplos")
    else:
        print(f"os numeros {b} e {a} não são multiplos")



else:
    if b%a==0:
        print(f"os numeros {a} e {b} são multiplos")
    else:
        print(f"os numeros {a} e {b} não são multiplos")