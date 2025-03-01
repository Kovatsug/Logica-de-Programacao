x=-2
y=0
pi=3
print(pi)
for i in range (1,15):
    if(i % 2 == 1):
        x+=4
        pi=pi + (4/(x * (x+1) * (x+2)))
        print(pi)



    elif(i % 2 == 0):
        y+=4
        pi=pi - (4/(y * (y+1) * (y+2)))
        print(pi)

