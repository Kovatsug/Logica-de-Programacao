def conta_digitos(n,d):
    if not(0<d<=9):
        return "Numero fora do limite solicitado"
    else:
        return f"O numero {d} aparece {str(n).count(str(d))} vezes no numero {n}"
    
print(conta_digitos(int(input("digite um numero inteiro: ")),int(input("Digite um número inteiro de 1 a 9: "))))