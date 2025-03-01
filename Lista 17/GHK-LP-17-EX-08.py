p1=input("texto 1: ")
p2=input("texto 2: ")

print(f"{p1} :{len(p1)} caracteres")
print(f"{p2} :{len(p2)} caracteres")

if len(p1)==len(p2):
    print("Tem tamanhos iguais")
else:
    print("tem tamanhos diferentes")
    
if p1==p2:
    print("possuem conteudos iguais")
else:
    print("possuem conteudos diferentes")