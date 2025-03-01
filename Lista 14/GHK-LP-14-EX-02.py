menor=float("inf")
maior=float("-inf")

n=0

while n!="":
    n=(input("Digite um numero: "))
    if n=="":
        break
    
    if int(n)>maior:
        maior=int(n)
    if int(n)<menor:
        menor=int(n)

print(f"o menor numero é {menor}")
print(f"o maior numero é {maior}")