n=int(input("De qual numero você quer o fatorial? "))

f=1

for i in range(1, (n+1)):
    f=f*i

print(f"O fatorial de {n} é {f}")