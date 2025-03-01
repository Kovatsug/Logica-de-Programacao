vasilhames_pequenos = int(input("Digite a quantidade de vasilhames de um litro ou menos: "))

vasilhames_grandes = int(input("Digite a quantidade de vasilhames de mais de um litro: "))

total_credito = vasilhames_pequenos * 0.10 + vasilhames_grandes * 0.25

print("O valor total dos créditos é: R$ {:.2f}".format(total_credito))
