c=int(input("digite um numero: "))
a=0
x=1

while x<=c:
    if x%2==1:
        a+=1/x
        x+=1
    elif x%2==0:
        a-=1/x
        x+=1
print(a)