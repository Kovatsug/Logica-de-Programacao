def encaixa(a,b):
    if b!=a[-len(b):]:
        print("não encaixa")
    else:
        print("Encaixa")


encaixa(input("Digite um numero: "),input("Digite o segundo número: "))
