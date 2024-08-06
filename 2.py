#2-vazifa
file=open("royxat.txt","r", encoding="utf-8")
malumot=[]
lines=file.readlines()
for line in lines:
    info=line.strip().split(",")
    change=info[3].replace("$","")
    dict={
        "num":info[0],
        "code":info[1],
        "product":info[2],
        "price":float(change),
        "availability":info[4]
    }
    malumot.append(dict)

filtered=list(filter(lambda info: info["availability"] == "true",malumot ))
filtered.sort(key=lambda info:info["price"],reverse=False)
for dict in filtered:
    print(f"{dict["num"]},{dict["code"]},{dict["product"]},{dict["price"]},{dict["availability"]}\n")
file.close()
