import jieba
import jieba.analyse
import jieba.posseg as pseg

if __name__ == '__main__':
    jieba.load_userdict("ruc_dict_pos_adv.txt")
    allwords=dict()
    keywords=dict()
    names=dict()
    places=dict()
    constitutions=dict()
    with open("homework_input_ruc_news_out.txt", "w", encoding="utf-8-sig") as f_out:
        with open("homework_input_ruc_news_out_keywords.txt", "w", encoding="utf-8-sig") as f_out_:
            with open("homework_input_ruc_news_out_keywords_stat.txt", "w", encoding="utf-8-sig") as f_out__:
                pass
    with open("homework_input_ruc_news.txt", "r", encoding="utf-8-sig") as f_in:
        lines = []
        line = f_in.readline()
        while line != "":
            # 分词，写入
            with open("homework_input_ruc_news_out.txt", "a", encoding="utf-8-sig") as f_out:
                linels = line.split("\t")
                f_out.write(" ".join(jieba.cut(linels[0])) + "\t" + linels[1] + "\t" + " ".join(jieba.cut(linels[2])))
                allword=jieba.lcut(line)
            for word in allword:
                if word in allwords:
                    allwords[word]+=1
                else:
                    allwords[word]=1
            # 抽取关键词
            with open("homework_input_ruc_news_out_keywords.txt", "a", encoding="utf-8-sig") as f_out:
                keyword=jieba.analyse.extract_tags(line)
                f_out.write(" ".join(keyword)+"\n")
            for word in keyword:
                if word in keywords:
                    keywords[word]+=1
                else:
                    keywords[word]=1
                
            # 词性
            words=pseg.cut(line)
            for w,t in words:
                if t=="nr":
                    if w in names:
                        names[w]+=1
                    else:
                        names[w]=1
                elif t=="ns":
                    if w in places:
                        places[w]+=1
                    else:
                        places[w]=1
                elif t=="nt":
                    if w in constitutions:
                        constitutions[w]+=1
                    else:
                        constitutions[w]=1
                
            line = f_in.readline()

    with open("homework_input_ruc_news_out_keywords_stat.txt", "w", encoding="utf-8-sig") as f_out:
        f_out.write("关键词：\n")
        allwordsls=[]
        for item in allwords.items():
            allwordsls.append((item[1],item[0]))
        allwordsls.sort(reverse=True)
        i=0
        count=0
        while True:
            elem=allwordsls[i]
            if elem[1] not in ["11","10","2019"," ","，","。","、","“","”","的","和","了","与","在","《","》","：","；","\t","-",":","（","）"]:
                f_out.write(elem[1]+"\t"+str(elem[0])+"\n")
                count+=1
            if count>=50 or i>=len(allwordsls):
                break
            i+=1
        f_out.write("\n")
        
        f_out.write("关键词：\n")
        keywordsls=[]
        for item in keywords.items():
            keywordsls.append((item[1],item[0]))
        keywordsls.sort(reverse=True)
        i=0
        count=0
        while True:
            elem=keywordsls[i]
            if elem[1] not in ["11","10","2019"]:
                f_out.write(elem[1]+"\t"+str(elem[0])+"\n")
                count+=1
            if count>=50 or i>=len(keywordsls):
                break
            i+=1
        f_out.write("\n")

        f_out.write("人名：\n")
        namesls=[]
        for item in names.items():
            namesls.append((item[1],item[0]))
        namesls.sort(reverse=True)
        i=0
        count=0
        while True:
            elem=namesls[i]
            if elem[1] not in ["师生","养老","智慧","立德","明德","王","高水平","从严治党","大力支持","文明","史","荣誉","荣获","盖章","卓越","关怀","祝贺","老同志","宝钢"]:
                f_out.write(elem[1]+"\t"+str(elem[0])+"\n")
                count+=1
            if count>=50 or i>=len(namesls):
                break
            i+=1
        f_out.write("\n")
        
        f_out.write("地点名：\n")
        placesls=[]
        for item in places.items():
            placesls.append((item[1],item[0]))
        placesls.sort(reverse=True)
        i=0
        count=0
        while True:
            elem=placesls[i]
            if elem[1] not in ["嘉宾","城市","扎根"]:
                f_out.write(elem[1]+"\t"+str(elem[0])+"\n")
                count+=1
            if count>=50 or i>=len(placesls):
                break
            i+=1
        f_out.write("\n")
        
        f_out.write("机构名：\n")
        constitutionsls=[]
        for item in constitutions.items():
            constitutionsls.append((item[1],item[0]))
        constitutionsls.sort(reverse=True)
        i=0
        count=0
        while True:
            elem=constitutionsls[i]
            if elem[1] not in ["暨"]:
                f_out.write(elem[1]+"\t"+str(elem[0])+"\n")
                count+=1
            if count>=50 or i>=len(constitutionsls):
                break
            i+=1
        f_out.write("\n")
        