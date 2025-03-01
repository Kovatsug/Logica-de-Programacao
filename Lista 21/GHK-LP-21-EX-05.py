def potencia(x,y):
    res=1
    for i in range(y):
        res*=x
    return res
print(potencia(float(input("Digite o numero x: ")),int(input("Digite o numero y: "))))