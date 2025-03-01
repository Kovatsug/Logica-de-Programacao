cpf=input("Digite seu CPF no formato xxx.xxx.xxx-xx: ")
cpf=cpf.replace(".","")
cpf=cpf.replace("-","")


#digito verificador 1
v1=0
c=1
for i in cpf[0:-2]:
    v1+=int(i)*c
    c+=1
    
v1%=11
if v1==10:
    v1=0

#digito verificador 2
v2=0
a=0
for i in cpf[0:-1]:
    v2+=int(i)*a
    a+=1

v2%=11
if v2==10:
    v2=0

dv=str(v1)+str(v2)

#verifica se os digitos são repetidos
d="1234567890"
for i in d:
    if cpf.count(i)==11:
        cpf="repetido"


if cpf[-2:]!=dv:
    print("CPF inválido")

else:
    print("CPF válido")
