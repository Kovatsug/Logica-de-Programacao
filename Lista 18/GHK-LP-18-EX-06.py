s=input("Digite sua string: ")
ns=""

for i in s:
    if i in "1234567890":
        ns+=i
    ns+=i

print(f"A string com os algarismos duplicados fica: {ns}")    