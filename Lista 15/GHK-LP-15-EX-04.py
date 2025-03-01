c1=0
c2=1
n=int(input("Qual termo da serie de fibonacci vc quer: "))
c=3

if n ==1:
    print(c1)

elif n ==2:
    print(c2)

while c<=n:
    c+=1
    c2+=c1
    c1=c2-c1
print(c2)