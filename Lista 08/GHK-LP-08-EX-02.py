n1=float(input("NOTA 1: "))
n2=float(input("NOTA 2: "))

m=(n1+n2)/2

if n1<3 or n2<3:
    print("uma das notas é inferior a 3")


elif m >= 5:
    print(f"Media: {m} \nParabens!")

else:
    print(f"media {m} \nReprovado!")