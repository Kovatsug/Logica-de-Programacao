pp=float(input("Qual o valor do prato principal: R$"))
suco=float(input("Qual o valor do suco: R$"))
sobremesa=float(input("Qual o valor da sobremesa: R$"))

preco=pp+suco+sobremesa
juros=preco*1.1

print("O valor total da sua refeição com 10% de taxa fica: R$ {:.2f}".format(juros))