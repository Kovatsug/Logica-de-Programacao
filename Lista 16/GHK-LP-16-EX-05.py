n=input("Escreva seu numero em binario: ")
d=1

for i in n:
    
    if i=="1":
        d=d*2
    elif i=="0":
      d=d*2-1

print(d-1)

