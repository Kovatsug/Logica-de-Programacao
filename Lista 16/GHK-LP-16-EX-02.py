total=0

while True:
    c=input("Quantos anos a pessoa tem: ")
    if c=="":
        break

    c=int(c)

    if c<3:
        continue

    elif 2<c<13:
        total+=14
    
    elif c>=65:
        total+=18
    
    else:
        total+=23

print(f"O total fica R${total:.2f}")