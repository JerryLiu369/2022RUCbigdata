def edits(word):
    # All edits that are one edit away from `word`.
    word=list(word)
    letters = list('abcdefghijklmnopqrstuvwxyz')
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + [R[1]] + [R[0]] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + [c] + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + [c] + R for L, R in splits for c in letters]
    deletes=["".join(x) for x in deletes]
    transposes=["".join(x) for x in transposes]
    replaces=["".join(x) for x in replaces]
    inserts=["".join(x) for x in inserts]
    return set(deletes + transposes + replaces + inserts)


inword = input("输入单词：").lower()
print(edits(inword))
