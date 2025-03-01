def imprime_n_vezes(nome, n):
    for i in range(n):
        print(nome)

imprime_n_vezes(input("Digite sua string: "),int(input("Quantas vezes será repetido: ")))