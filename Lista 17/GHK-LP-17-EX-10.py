n=input("escreva seu nascimento no formato dd/mm/aaaa: ")

x=n[3:5]

if x=="01":
    x="janeiro"

elif x=="02":
    x="fevereiro"

elif x=="03":
    x="março"

elif x=="04":
    x="abril"

elif x=="05":
    x="maio"

elif x=="06":
    x="junho"

elif x=="07":
    x="julho"

elif x=="08":
    x="agosto"

elif x=="09":
    x="setembro"

elif x=="10":
    x="outubro"

elif x=="11":
    x="novembro"

elif x=="12":
    x="dezembro"

print(f"Você nasceu no dia {n[:2]} de {x} de {n[-4:]}")