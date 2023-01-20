import jieba
import jieba.posseg as pseg
import os
import shutil
import matplotlib.pyplot as plt
from jieba.analyse import extract_tags

# 分词参数设定
jieba.load_userdict("meetings_dict.txt")
stopwords = {"\n", " ", "、", "，", "的", "是", "。", "“", "”", "和", "等", "《", "》", "对", "（", "）", "要", "在", "一",
			 "了", "为", "国务院", "李克强", "常务会议", "会议", "召开", "主持", "；"}
ag_words = [
	"农村",
	"农业",
	"农民",
]

# 初始化分词结果存储文件夹
if os.path.exists("split"):
	shutil.rmtree("split")
os.mkdir("split")
if os.path.exists("ag_words"):
	shutil.rmtree("ag_words")
os.mkdir("ag_words")

# 依顺序读取文本数据并分词
title_dict = dict()
content_dict = dict()
keyword_dict = dict()
for root, dirs, files in os.walk("data"):
	for file in files:
		with open(f"{root}/{file}", "r", encoding="utf-8-sig") as f:
			with open(f"split/{file}", "w", encoding="utf-8-sig") as ff:
				# 读取文本
				f.readline()
				f.readline()
				title = f.readline()
				f.readline()
				content = f.readline()
				# 写入分词结果文件
				# 标题分词
				ff.write("标题：\n")
				for word, flag in pseg.cut(title, HMM=True):
					if word in stopwords:
						continue
					ff.write(word + " ")
					if word in title_dict:
						title_dict[word] += 1
					else:
						title_dict[word] = 1
				ff.write("正文：\n")
				# 正文分词
				for word, flag in pseg.cut(content, HMM=True):
					if word in stopwords:
						continue
					ff.write(word + " ")
					if word in content_dict:
						content_dict[word] += 1
					else:
						content_dict[word] = 1
					# 涉农词语挑选，写入日期
					for ag_word in ag_words:
						if ag_word in word:
							with open(f"ag_words/{ag_word}.txt", "a", encoding="utf-8-sig") as fff:
								fff.write(file.strip(".txt") + "\n")
				# 关键词提取
				for word in extract_tags(content, 10, allowPOS=("n")):
					if word in stopwords:
						continue
					if word in keyword_dict:
						keyword_dict[word] += 1
					else:
						keyword_dict[word] = 1

# 词频统计
for term in ["title", "content", "keyword"]:
	exec(f"""
{term}_queue = list()
for key, value in {term}_dict.items():
	{term}_queue.append((value, key))
{term}_queue.sort()
{term}_queue.reverse()
""")

# 初始化作图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 14
if os.path.exists("figures"):
	shutil.rmtree("figures")
os.mkdir("figures")

# 作图
# 词频统计
match = {"title": "标题", "content": "正文", "keyword": "关键词"}
for term in ["title", "content", "keyword"]:
	plt.figure(figsize=(16, 10))
	x = list(map(lambda t: t[1], eval(f"{term}_queue")[:20]))  # 获取x轴数据
	y = list(map(lambda t: t[0], eval(f"{term}_queue")[:20]))  # 获取y轴数据
	x.reverse()
	y.reverse()
	for index, y_value in enumerate(y):
		plt.text(y_value + 2, index - 0.2, "%s" % y_value)
	plt.barh(x, y)
	plt.title(f"{match[term]}词频分布", size=28)
	plt.ylabel("词语（前20）", size=22)
	plt.xlabel("词频", size=22)
	plt.savefig(f"figures/{term}.png")

# 涉农词语
all_years_dict = dict()
all_months_dict = dict()
for root, dirs, files in os.walk("ag_words"):
	for file in files:
		years_dict = dict()
		months_dict = dict()
		with open(f"{root}/{file}", "r", encoding="utf-8-sig") as f:
			dates = f.read().strip("\n").split("\n")
			for date in dates:
				yr, mon, day = date.split("-")
				if yr == "2023":
					continue
				if yr in years_dict:
					years_dict[yr] += 1
				else:
					years_dict[yr] = 1
				if yr in all_years_dict:
					all_years_dict[yr] += 1
				else:
					all_years_dict[yr] = 1
				if mon in months_dict:
					months_dict[mon] += 1
				else:
					months_dict[mon] = 1
				if mon in all_months_dict:
					all_months_dict[mon] += 1
				else:
					all_months_dict[mon] = 1
		
		plt.figure(figsize=(16, 10))
		x = []
		y = []
		temp = list(years_dict.items())
		temp.sort()
		for i in temp:
			x.append(i[0])
			y.append(i[1])
		for index, y_value in enumerate(y):
			plt.text(index - 0.1, y_value, "%s" % y_value)
		plt.plot(x, y)
		plt.title(f"“{file.strip('.txt')}”年份分布", size=28)
		plt.ylabel("词频", size=22)
		plt.xlabel("年份", size=22)
		plt.savefig(f"figures/{file.strip('.txt')}年份.png")
		
		plt.figure(figsize=(16, 10))
		x = []
		y = []
		temp = list(months_dict.items())
		temp.sort()
		for i in temp:
			x.append(i[0])
			y.append(i[1])
		for index, y_value in enumerate(y):
			plt.text(index - 0.1, y_value, "%s" % y_value)
		plt.bar(x, y)
		plt.title(f"“{file.strip('.txt')}”月份分布", size=28)
		plt.ylabel("词频", size=22)
		plt.xlabel("月份", size=22)
		plt.savefig(f"figures/{file.strip('.txt')}月份.png")

plt.figure(figsize=(16, 10))
x = []
y = []
temp = list(all_years_dict.items())
temp.sort()
for i in temp:
	x.append(i[0])
	y.append(i[1])
for index, y_value in enumerate(y):
	plt.text(index - 0.1, y_value, "%s" % y_value)
plt.plot(x, y)
plt.title("三农词语总体年份分布", size=28)
plt.ylabel("词频", size=22)
plt.xlabel("年份", size=22)
plt.savefig(f"figures/三农年份.png")

plt.figure(figsize=(16, 10))
x = []
y = []
temp = list(all_months_dict.items())
temp.sort()
for i in temp:
	x.append(i[0])
	y.append(i[1])
for index, y_value in enumerate(y):
	plt.text(index - 0.1, y_value, "%s" % y_value)
plt.bar(x, y)
plt.title(f"三农词语总体月份分布", size=28)
plt.ylabel("词频", size=22)
plt.xlabel("月份", size=22)
plt.savefig(f"figures/三农月份.png")
