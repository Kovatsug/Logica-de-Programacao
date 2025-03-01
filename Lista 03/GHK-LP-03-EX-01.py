numero = int(input("Digite um número inteiro de três dígitos: "))


c = numero // 100
d = (numero % 100) // 10
u = numero % 10


print(f"O número M gerado é: {u}{d}{c}")
