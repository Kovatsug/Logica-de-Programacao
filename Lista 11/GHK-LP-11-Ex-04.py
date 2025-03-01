n = int(input('Dígite um número:'))
a=0

for i in range (1, n+1):
    if(i % 2 == 1):
        a = a + 1 / i

    if(i % 2 == 0):
        a = a - 1 / i

print (a)