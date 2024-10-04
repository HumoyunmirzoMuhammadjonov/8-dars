ism, familiya, yosh = map(str,input("ism, familiya, yosh kiring: ").split())

file = open(f"{ism}.txt","w+")

file.write(ism+"\n"+familiya+"\n"+yosh)

file.seek(0)

for i in file.readlines():
    print(i,end="")
file.close()