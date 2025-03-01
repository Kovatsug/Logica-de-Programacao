a=0
b=[]
d=0
f=0
g=0

n=float(input("Digite a nota (-1 para cancelar): "))
while n!=(-1):
    #b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    b.append(n)

    #a) Mostre a quantidade de valores que foram lidos;
    a+=1
    #d) Calcule e mostre a soma dos valores;
    d+=n

    n=float(input("Digite a nota (-1 para cancelar): "))


#a) Mostre a quantidade de valores que foram lidos;
print(a)

#b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print(b)

#c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
for i in range(-1,-1-len(b),-1): 
    print(b[i])

#d) Calcule e mostre a soma dos valores;
print(f"Soma dos valores: {d}")

#e) Calcule e mostre a média dos valores;
e=d/a
print(f"Média dos valores: {e}")

#f) Calcule e mostre a quantidade de valores acima da média calculada;
for i in b:
    if i>=e:
        f+=1
print(f"A quantidade de valores acima da média é: {f}")

#g) Calcule e mostre a quantidade de valores abaixo de sete;
for i in b:
    if i<7:
        g+=1
print(f"A quantidade de valores abaixo de 7 é: {g}")

#h) Encerre o programa com uma mensagem;
print("\nVocê arrasou! Analisamos suas notas com carinho e tudo foi calculado.")
print("Agora, está tudo pronto! Até a próxima! 👋✨")