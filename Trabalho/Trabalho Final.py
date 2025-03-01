def par_ou_impar(n):

    if n%2==0:
        print(f"O número {n} é par.")
    else:
        print(f"O número {n} é impar.")

def multiplo7(n):

    if n%7==0:
        print(f"O número {n} é multiplo de 7.")
    else:
        print(f"O número {n} não é multiplo de 7.")
    
def intervalo_200a400(n):

    if 200<=n<=400:
        print(f"O número {n} está no intervalo de 200 a 400.")
    else:
        print(f"O número {n} não está no intervalo de 200 a 400.")

def primo(n):

    divisores=[]
    for i in range(1,n+1):
        if n%i==0:
            divisores.append(i)

    if divisores==[1,n]:
        print(f"{n} é um número primo.")
    
        primos.append(n)

    else:
        print(f"Os divisores de {n} são: {divisores}")

primos=[]

def multilpo_3_4(n):

    if n%3==0 and n%4==0:
        print(f"O número {n} é multiplo de 3 e 4 ao mesmo tempo.")
    else: 
        print(f"O número {n} não é multiplo de 3 e 4 ao mesmo tempo.")

def fatorial(x):
    resultado=1
    for i in range(2,x+1):
        resultado*=i
    print(f"O fatorial do menor número ({min(numeros)}) é: {resultado}")

def numeros_repetidos():
    
    repetidos=[]
    vezes=0

    for i in numeros:
        apareceu=numeros.count(i)
        
        if apareceu>vezes:
            repetidos=[i]
            vezes=apareceu
        
        elif apareceu==vezes and i not in repetidos:
            repetidos.append(i)

    print(f"O número mais repetido foi: {repetidos} aparecendo {vezes} vezes")


def valor_central():

    if total_numeros%2==1:
        vc=numeros[total_numeros//2]

    else:
        vc=(numeros[total_numeros//2-1]+numeros[total_numeros//2])/2
    print(f"O valor central  é: {vc}")


numeros=[]
total_numeros=0

while True:
    while True:
        try:
            n=int(input("\nDigite um número inteiro positivo, ou um negativo para parar: "))
            break
        except ValueError:
            print("Digite um número inteiro, não coloque letras.")
            continue
    if n<0:
        break

    numeros.append(n)
    total_numeros+=1

    par_ou_impar(n)
    multiplo7(n)
    intervalo_200a400(n)
    primo(n)
    multilpo_3_4(n)


print(f"Os números fornecidos foram: {numeros}\nSendo um total de {total_numeros} números.")

try:
    print(f"A média aritimédica dos números é {sum(numeros)/total_numeros}.")
    print(f"O maior número foi {max(numeros)}.")
    print(f"O menor número foi {min(numeros)}.")
    
    try:
        print(f"O maior número primo foi {max(primos)}.")
        print(f"O menor número primo foi {min(primos)}.")
    except:
        print("Nenhum número primo foi fornecido")

    fatorial(min(numeros))
    numeros_repetidos()
    valor_central()

except:
    print("Não foi digitado nenhum número antes de encerrar o programa para mostrar o resto das informações .")
