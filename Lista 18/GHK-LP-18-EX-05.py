s=input("Digite seu numero: ")
ns=""
for i in s:
    if i=="9":
        ns+="0"
        continue
    ns+=str(int(i)+1)

print(ns)