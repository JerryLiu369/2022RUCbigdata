class Word:
    def __init__(self, word, n):
        self.word = word
        self.n = n
    
    def __lt__(self, other):
        if self.n == other.n:
            return self.word < other.word
        else:
            return self.n < other.n
    
    def __str__(self):
        return "(\"" + self.word + "\"," + str(self.n) + ")"
    
    __repr__ = __str__


class Report:
    def __init__(self, filename):
        self.filename = filename
        self.frequency = dict()
    
    def stat(self):
        file = open(self.filename, "r", encoding="utf-8")
        now = file.readline()
        while now != "":
            words = now.split(" ")
            for word in words:
                if word in self.frequency:
                    self.frequency[word] += 1
                else:
                    self.frequency[word] = 1
            now = file.readline()
    
    def show_head(self, k):
        ls = list()
        for word, n in self.frequency.items():
            if word not in ["，", "。", "、", "\n", "", "“", "”"]:
                ls.append(Word(word, n))
        ls.sort(reverse=True)
        print(self.filename + ":")
        for i in range(min(k, len(ls))):
            print(ls[i], end=";")
        print()
        
    def write(self):
        with open("frequency_"+self.filename.removesuffix(".txt")+".csv","w",encoding="utf-8-sig") as f:
            ls = list()
            for word, n in self.frequency.items():
                if word not in ["，", "。", "、", "\n", "", "“", "”"]:
                    ls.append(Word(word, n))
            ls.sort(reverse=True)
            for word in ls:
                f.write(word.word+","+str(word.n)+"\n")
        
    
    def __add__(self, other):
        res = Report(self.filename)
        res.frequency = dict(self.frequency)
        for word, n in other.frequency.items():
            if word in res.frequency:
                res.frequency[word] += n
            else:
                res.frequency[word] = n
        return res


if __name__ == '__main__':
    res = Report("all_path")
    for filename in ["gov_cut.txt", "shanxi_cut.txt", "sichuan_cut.txt"]:
        temp = Report(filename)
        temp.stat()
        res += temp
        temp.show_head(10)
    res.show_head(10)
    res.write()
    
