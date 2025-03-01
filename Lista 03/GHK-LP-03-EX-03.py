matricula=int(input("Informa o número de matricula no formato AASDDD:"))

ano=matricula//10000
semestre=(matricula//1000)%10


print("O ano da matricula foi",ano,"no",semestre,"º semestre")