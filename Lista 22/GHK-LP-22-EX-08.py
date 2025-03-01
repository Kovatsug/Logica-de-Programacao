def encaixa(a,b):
    if a > b:
        a=str(a)
        b=str(b)
        if b in a:
            print(f"{b} é segmento de {a}")
        else:
            print(f"{b} não é segmento de {a}")

    elif b > a:
        a=str(a)
        b=str(b)
        if a in b:
            print(f"{a} é segmento de {b}")
        else:
            print(f"{a} não é segmento de {b}")
            

encaixa(int(input("Digite um numero: ")),int(input("Digite o segundo número: ")))
