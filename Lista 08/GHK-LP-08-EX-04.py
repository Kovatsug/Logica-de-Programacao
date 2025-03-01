c=int(input("Coluna: "))
l=int(input("linha: "))

if c==l:
    print("Preta")

elif c%2==0 and l%2==0:
    print("preta")

elif c%2==1 and l%2==1:
    print("preta")

else:
    print("Branca")

