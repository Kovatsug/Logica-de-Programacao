codigo=int(input("Digite seu código de cinco digitos:"))

s=6*(codigo//10000)+5*(codigo//1000%10)+4*(codigo//100%10)+3*(codigo//10%10)+2*(codigo%10)


v=s%7


print("o código verificador é:", v)