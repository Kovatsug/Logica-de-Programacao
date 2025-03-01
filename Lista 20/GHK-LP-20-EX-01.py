votos=[0,0,0,0,0,0,0]

print("""Qual o melhor Sistema Operacional para uso em servidores?
As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro""")

v=int(input("Digite seu voto (ou 0 para encerrar): "))
while v!=0:

    if 1<=v<=6:
        votos[v]+=1

    elif v<1 or v>6:
        print("\nDigite um voto válido!")
        v=int(input("Digite seu voto (ou 0 para encerrar): "))
        continue
    
    
    v=int(input("Digite seu voto (ou 0 para encerrar): "))

totalVotos=sum(votos)

percentual=[]
for i in range(1,7):
    percentual.append((votos[i]*100)//totalVotos)

vencedor=votos.index(max(votos))

opc=["Windows Server","Unix","Linux","Netware","Mac OS","Outro"]

print("""
Sistema operacional\tVotos\t%
-------------------\t-----\t---""")

for i in range(6):
    print(f"{opc[i].ljust(14)}\t\t{str(votos[i+1]).rjust(5)}\t{str(percentual[i]).rjust(2)}%")

print(f"""-------------------\t-----
Total              \t{str(totalVotos).rjust(5)}

O sistema operacional mais votado foi o {opc[vencedor-1]}, com {votos[vencedor]} votos, correspondendo a {percentual[vencedor-1]}% dos votos.""")
