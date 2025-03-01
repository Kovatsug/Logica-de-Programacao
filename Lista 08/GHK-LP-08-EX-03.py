n1=float(input("NOTA 1: "))
n2=float(input("NOTA 2: "))

m=(n1+n2)/2



nf=10-m

if n1<3 or n2<3 or m<5:
    print(f"media {m} \nReprovado!")
    print(f"Necessario de {nf} na prova final")


elif m >= 5:
    print(f"Media: {m} \nParabens!")

