def novo_numero():
    while True:
        try:
            n=int(input("\nDigite um número inteiro positivo, ou um negativo para parar: "))
            break
        except:
            print("Escreva um número inteiro! Não use letras nem adicione casas decimais.")
            continue
    return n

def par_impar(n):
    if n%2==0:
        print(f"O número {n} é Par.")
    else:
        print(f"O número {n} é Impar.")
    
def multiplo7(n):
    if n%7==0:
        print(f"O número {n} é multiplo de 7.")
    else:
        print(f"O número {n} não é multiplo de 7.")
    
def intervalo(n):
    if 200<=n<=400:
        print(f"O número {n} está no intervalo de 200 a 400.")
    else:
        print(f"O número {n} está no intervalo de 200 a 400.")
    
primos=[]
def primo(n):
    divisores=[]
    for i in range(1,n+1):
        if n%i==0:
            divisores.append(i)
    if divisores==[1,n]:
        print(f"O número {n} é um número primo.")
        primos.append(n)   
    else:
        print(f"O número {n} não é um número primo, seus divisores são: {divisores}.")
    
def multiplo3e4(n):
    if n%3==0 and n%4==0:
        print(f"O número {n} é multiplo de 3 e 4 simultaneamente.")
    else:
        print(f"O número {n} não é multiplo de 3 e 4 simultaneamente.")

def repetido():
    repetidos=[]
    vezes=0
    for i in numeros:
        repetiu=numeros.count(i)
        if repetiu>vezes:
            repetidos=[i]
            vezes=repetiu
        elif repetiu==vezes and i not in repetidos:
            repetidos.append(i)
    print(f"O(s) número(s) mais repetido(s) foi/foram: {repetidos}. Sendo informado(s) {vezes} vezes.")

def valorCentral():
    n=len(numeros)
    if n%2==1:
        print(f"O valor central obtido foi: {numeros[n//2]}.")
    else:
        print(f"O valor central obtido foi: {(numeros[n//2] + numeros[n//2-1])/2}.")


quantidade=0
numeros=[]

while True:
    try:
        n=int(input("Digite um número inteiro positivo: "))
        break
    except:
        print("Escreva um número inteiro! Não use letras nem adicione casas decimais.")
        continue

while n>=0:

    par_impar(n)
    multiplo7(n)
    intervalo(n)
    primo(n)
    multiplo3e4(n)

    quantidade+=1
    numeros.append(n)

    n=novo_numero()


try:
    print(f"Os números fornecidos foram: {numeros}\nSendo um total de {quantidade} números.")
    print(f"A média aritmética dos é: {sum(numeros)/quantidade}.")
    print(f"O maior número fornecido foi: {max(numeros)}.")
    print(f"O menor número fornecido foi: {min(numeros)}.")

    try:
        print(f"O maior número primo fornecido foi: {max(primos)}.")
        print(f"O menor número primo fornecido foi: {min(primos)}.")
    except:
        print("Não foi recebido nenhum número primo para mostrar o menor e o maior deles.")

    fatorial=1
    for i in range(1,min(numeros)+1):
        fatorial*=i
    print(f"O fatorial do menor número informado ({min(numeros)}) é: {fatorial}.")

    repetido()
    valorCentral()
except:
    print("Não foi informado nenhum numero para mostrar o restante das informações.")