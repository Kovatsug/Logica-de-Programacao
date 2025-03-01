la=[]
li=[]

for i in range(1,6):
    idade=int(input(f"Qual a idade da pessoa {i}: "))
    altura=float(input(f"Qual a altura da pessoa {i}: "))
    li.append(idade)
    la.append(altura)
li.reverse()
la.reverse()
print(li)
print(la)