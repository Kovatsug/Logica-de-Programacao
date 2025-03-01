n1=input("Escreva a primeira palavra:  ")
n2=input("Escreva a segunda palavra: ")
nw=""

for i in range(-1,(-len(n1)-1),-1):
    nw+=n1[i]

if nw == n2:
    print("Uma palavra é o inverso da outra")
else:
    print("Uma palavra não é o inverso da outra")