m=0
menor=float("inf")
maior=float("-inf")


for i in range(10):
    n=int(input("Escolha um numero: "))
    
    m=m+n
    if n>maior:
        maior=n

    if n<menor:
        menor=n




media=m/10

print(f"A media é:{media}\no menor numero é:{menor}\no maior numero é: {maior}")