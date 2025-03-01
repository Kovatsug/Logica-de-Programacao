def permutacao(a,b):
    if len(a)!=len(b):
        print(f"{a} não é permutação de {b}")
    else:
        l1=[0,0,0,0,0,0,0,0,0,0]
        for i in a:
            l1[int(i)]+=b.count(i)
        l2=[0,0,0,0,0,0,0,0,0,0]
        for i in b:
            l2[int(i)]+=a.count(i)
        if l1==l2:
            print(f"{a} é permutação de {b}")
        else:
            print(f"{a} não é permutação de {b}")

permutacao(input("digite o primeiro número: "), input("Digite o segundo numero: "))
