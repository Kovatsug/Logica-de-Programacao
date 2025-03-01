q=int(input("Escreva o numero decimal:"))
result=""

while q != 0:
    c=q%2
    c=str(c)
    result=c+result
    q=q//2

print(result)