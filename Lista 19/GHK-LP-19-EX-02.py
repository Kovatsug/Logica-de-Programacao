medias=[]

acimade7=0

for i in range(1,11):
    n1=float(input(f"Qual a primeira nota do aluno {i}: "))
    n2=float(input(f"Qual a segunda nota do aluno {i}: "))
    n3=float(input(f"Qual a terceira nota do aluno {i}: "))
    n4=float(input(f"Qual a quarta nota do aluno {i}: "))
    m=(n1+n2+n3+n4)/4
    medias.append(m)

for media in medias:
    if media>=7:
        acimade7+=1

print(f"O total de alunos com nota igual ou superior a 7 é: {acimade7}")
