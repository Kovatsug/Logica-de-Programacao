modelos=[]
kmpl=[]


for i in range(1,6):
    print(f"Veiculo {i}")
    v=input("Nome: ")
    k=float(input("Km por litro: "))
    modelos.append(v)
    kmpl.append(k)

#litros necessários para 1000km
ln=[]
for i in kmpl:
    ln.append(1000/i)

#preço dos litros para 1000km
pl=[]
for i in ln:
    pl.append(i*5.25)

print(f"\nRelatório Final")

for i in range(5):
    print(f" {i+1} - {str(modelos[i]).ljust(15)}-{str(kmpl[i]).rjust(5)} - {(f'{ln[i]:.1f}').rjust(6)} litros - R$ {pl[i]:.2f}")

print(f"O menor consumo é do {modelos[kmpl.index(max(kmpl))]}.")