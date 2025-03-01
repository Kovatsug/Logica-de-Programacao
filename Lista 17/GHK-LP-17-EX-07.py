pal=input("Sua palavra: ")
vog="aeiou"
npal=""
for letra in pal:
    npal+=letra
    for vogal in vog:
        if letra==vogal:
            npal+=letra

print(npal)