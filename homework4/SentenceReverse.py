def reverse(sentence: str):
    index = sentence.rfind(" ")
    if index == -1:
        return sentence
    else:
        return sentence[index + 1:] + " " + reverse(sentence[:index])


instr = input("输入一句话：")
# print(" ".join(instr.split(" ")[::-1]))
print(reverse(instr))
