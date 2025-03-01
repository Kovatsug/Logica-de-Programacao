data=int(input("Infotme a data:"))

dd= data // 10000
mm= (data // 100) % 100
aa= data % 100


print(f"{aa}{mm}{dd}")
