s=input("Escreva seu texto: ")
t=0

v="aeiou"

for i in v:
    t+=s.count(i)
    
print(s.count(" "),"Espaços em branco")
print(t,"vogais")
    
