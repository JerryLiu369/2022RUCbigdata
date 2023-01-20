from collections import Counter

datels = []
yearls = []
monthls = []
with open("news.csv", "r+", encoding="utf-8-sig") as f:
    line = f.readline()
    while line.strip("\n").strip(" ") != "":
        datels.append(line.split(",")[-1].split("-")[0] + "-" + line.split(",")[-1].split("-")[1])
        yearls.append(line.split(",")[-1].split("-")[0])
        monthls.append(line.split(",")[-1].split("-")[1])
        line = f.readline()
    datecounter = Counter(datels)
    yearcounter = Counter(yearls)
    monthcounter = Counter(monthls)
    datels.clear()
    yearls.clear()
    monthls.clear()
    for item in datecounter.items():
        datels.append((item[1], item[0]))
    for item in yearcounter.items():
        yearls.append((item[1], item[0]))
    for item in monthcounter.items():
        monthls.append((item[1], item[0]))
    datels.sort(reverse=True)
    yearls.sort(reverse=True)
    monthls.sort(reverse=True)
    with open("result/date.csv","w",encoding="utf-8-sig") as f:
        for i in datels:
            f.write(i[1]+","+str(i[0])+"\n")
    with open("result/year.csv","w",encoding="utf-8-sig") as f:
        for i in yearls:
            f.write(i[1]+","+str(i[0])+"\n")
    with open("result/month.csv","w",encoding="utf-8-sig") as f:
        for i in monthls:
            f.write(i[1]+","+str(i[0])+"\n")
