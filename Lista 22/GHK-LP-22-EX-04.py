def eh_bissexto(ano):
    if ano%4==0 and (ano%100!=0 or ano%100==0):
        return True
    else:
        return False
    
print(eh_bissexto(int(input(f"Digite um ano: "))))
