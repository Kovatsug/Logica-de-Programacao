s1=input("Escreva a primeira palavra: ")
s2=input("Escreva a segunda palavra: ")
s3=""

c=0

while len(s3)!=(len(s1)+len(s2)):
    if len(s1)>c:
        s3+=s1[c]
    if len(s2)>c:
        s3+=s2[c]
    c+=1

print(s3)  

