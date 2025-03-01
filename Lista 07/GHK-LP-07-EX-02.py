n1=int(input("Digite o primeiro numero: "))
n2=int(input("Digite o segundo numero: "))
n3=int(input("Digite o terceiro numero: "))

if n1<n2<n3:
    d1=n1
    d2=n2
    d3=n3

if n1<n3<n2:
    d1=n1
    d2=n3
    d3=n2

if n2<n1<n3:
    d1=n2
    d2=n1
    d3=n3

if n2<n3<n1:
    d1=n2
    d2=n3
    d3=n1

if n3<n1<n2:
    d1=n3
    d2=n1
    d3=n2

if n3<n2<n1:
    d1=n3
    d2=n2
    d3=n1



print(f"a ordem decrescente é: {d3} {d2} {d1}")