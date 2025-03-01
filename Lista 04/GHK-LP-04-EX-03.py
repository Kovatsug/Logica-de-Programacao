troco=int(input("Qual seu troco em centavos (de 0 a 99): "))

m50 = troco // 50
m25 = (troco - m50 * 50) // 25
m10 = (troco - m50 * 50 - m25 * 25) // 10
m5 = (troco - m50 * 50 - m25 * 25 - m10 * 10) // 5
m1 = moeda5 = (troco - m50 * 50 - m25 * 25 - m10 * 10 - m5 * 5)

print(f"A quantidade de moedas de 50 foi {m50}\nA quantidade de moedas de 25 foi {m25}\nA quantidade de moedas de 10 foi {m10}\nA quantidade de moedas de 5 foi {m5}\nA quantidade de moedas de 1 foi {m1}")