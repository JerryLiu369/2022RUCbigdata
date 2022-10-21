from collections import Counter
with open("big.txt","r",encoding="utf-8") as f:
    txt=f.read()
    ls=txt.split(" ")
    lls=[]
    for elem in ls:
        lls+=elem.split("\n")
    ls=[]
    for elem in lls:
        ls+=elem.split(",")
    lls=[]
    for elem in ls:
        lls+=elem.split(".")
    ls=[]
    for elem in lls:
        ls+=elem.split("(")
    lls=[]
    for elem in ls:
        lls+=elem.split(")")
    ls=[]
    for elem in lls:
        ls+=elem.split("[")
    lls=[]
    for elem in ls:
        lls+=elem.split("]")
    ls=[]
    for elem in lls:
        ls+=elem.split("'")
    lls=[]
    for elem in ls:
        lls+=elem.split("\"")
    ls=[]
    for elem in lls:
        ls+=elem.split("/")
    lls=[]
    for elem in ls:
        lls+=elem.split("=")
    ls=[]
    for elem in lls:
        ls+=elem.split("?")
    lls=[]
    for elem in ls:
        lls+=elem.split("!")
    ls=[]
    for elem in lls:
        ls+=elem.split("+")
    lls=[]
    for elem in ls:
        lls+=elem.split("-")
    print(lls)
    words_counter=Counter([x.lower() for x in lls if x not in [" ", "", "\n", ",", "."]])
    print(words_counter.most_common(10))
    inword=input("请输入要查找的单词：")
    print(f"该单词出现的次数是：{words_counter[inword]}")