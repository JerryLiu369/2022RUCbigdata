word = input("输入：").lower()
ALL_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
res=set()
for index in range(len(word)):
    res.add(word[:index] + word[index + 1:])
    for letter in ALL_LETTERS:
        res.add(word[:index] + letter+word[index + 1:])
        res.add(word[:index] + letter+word[index:])
for i in range(len(word)):
    for j in range(i+1,len(word)):
        res.add(word[:i]+word[j]+word[i+1:j]+word[i]+word[j+1:])
print(res)