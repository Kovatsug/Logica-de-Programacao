n=int(input("Escreva seu numero de 4 digitos: "))

na=n//1000

nb=n//100 % 10

nc=n//10 %10

nd=n%10

soma=na+nb+nc+nd

print(f"A soma dos algarismos de {n} é: {soma} ")