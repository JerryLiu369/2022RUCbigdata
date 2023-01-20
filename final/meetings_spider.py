from scrapy import Spider, Request
from scrapy.http.response import Response
import os
import shutil


# 辅助去空函数
def del_null(rawls: list):
	for i, v in enumerate(rawls):
		v = v.replace("\xa0", " ")
		v = v.replace("\u3000", " ")
		v = v.replace("\n", " ")
		v = v.replace("\t", " ")
		v = v.replace("\r", " ")
		rawls[i] = v.strip(" ").strip("资料图")
	while "" in rawls:
		rawls.remove("")
	return rawls


class MeetingsSpider(Spider):
	name = "meetings"
	
	# 初始化爬虫和数据存储
	def start_requests(self):
		if os.path.exists("data"):
			shutil.rmtree("data")
		os.mkdir("data")
		yield Request(url="http://sousuo.gov.cn/column/30562/0.htm", callback=self.parse)
	
	def parse(self, response: Response, **kwargs):
		if response.url.find("sousuo") != -1:
			# 进入会议列表中的全部链接，并翻到下一页
			css_ls = ["ul.listTxt a::attr(href)", "div.newspage a.next::attr(href)"]
			for css in css_ls:
				ls = response.css(css).extract()
				for url in ls:
					yield Request(url=url, callback=self.parse)
		else:
			ls = response.css("div.left_area a::attr(href)").extract()
			if ls:
				# 对于隐藏正文的链接找出正文
				url: str = ls[0]
				if url[:2] == "..":
					url = "http://www.gov.cn/guowuyuan/" + url[3:]
				yield Request(url=url.strip(" "), callback=self.parse)
			else:
				# 处理正文标题
				t_mode = 0
				title = response.css("div.pages_content p:nth-child(1) * *::text").extract()
				if len(title) == 0:
					t_mode = 1
					title = response.css("div.pages_content tr strong font::text").extract()
				if len(title) == 0:
					t_mode = 2
					title = response.css("div.pages_content p:nth-child(2) * *::text").extract()
				if len(title) == 0:
					t_mode = 3
					title = response.css("div.pages_content>div>span::text").extract() + response.css(
						"div.pages_content>div div[style*=\"text\"] *::text").extract()
				if len(title) == 0:
					t_mode = 4
					title = response.css("div.pages_content>div *::text").extract()
				title = del_null(title)
				
				# 处理正文内容
				c_mode = 0
				content = response.css("div.pages_content p::text").extract()
				content = del_null(content)
				if len(content) == 0:
					c_mode = 1
					content = response.css(
						"div.pages_content tr td:nth-child(1) * font::text").extract()
					content = del_null(content)
				if len(content) == 0:
					c_mode = 2
					content = response.css("div.pages_content tr td:nth-child(1) p * *::text").extract()
					content = del_null(content)
				if content[0].find("国务院总理") != 0 and content[0].find("新华社") != 0 and content[0].find(
						"日前") != 0:
					if title[-1].find("国务院总理") == 0:
						content = title[-1:] + content
						title = title[:-1]
					else:
						c_mode = 3
						content = response.css("div.pages_content p *::text").extract()
					content = del_null(content)
				for i in title:
					if i in content and i.find("国务院总理") != 0:
						content.remove(i)
				if content[0].find("国务院总理") != 0 and content[0].find("新华社") != 0 and content[0].find(
						"日前") != 0:
					c_mode = 4
					content = response.css(
						"div.pages_content tr td:nth-child(1)>font font:nth-child(2) * *::text").extract()
					content = del_null(content)
				
				# 提取正文日期
				date = response.css("div.pages-date::text").extract()[0].strip(' ').split(' ')[0]
				
				# 特殊情况单独人工处理
				if date == "2019-12-13":
					title = ["李克强主持召开国务院常务会议\n通过《中华人民共和国外商投资法实施条例（草案）》 实化促进和保护外商投资的措施\n部署推动进一步降低小微企业综合融资成本"]
				if date == "2014-07-23":
					title = ["""李克强主持召开国务院常务会议
部署多措并举缓解企业融资成本高问题
审议通过《企业信息公示暂行条例（草案）》推动构建公平竞争市场环境"""]
					content = ["""国务院总理李克强7月23日主持召开国务院常务会议，部署多措并举缓解企业融资成本高问题，审议通过《企业信息公示暂行条例（草案）》，推动构建公平竞争市场环境。
会议指出，企业是经济活动的基本细胞。当前我国货币信贷总量不小，但企业特别是小微企业融资不易、成本较高的结构性问题依然突出，不仅加重企业负担、影响宏观调控效果，也带来金融风险隐患。有效缓解这一问题，既可为企业“输氧供血”，促进当前稳增长，又能形成金融与实体经济良性互动，使经济固本培元、行稳致远。要按照定向调控要求，多措并举、标本兼治，推动结构性改革和调整，深化金融体制改革，加强金融服务和监管，为做强实体经济、扩大就业和改善民生提供金融支持。
会议确定，一要继续坚持稳健的货币政策，保持信贷总量合理增长，着力调整结构，优化信贷投向。加大支农、支小再贷款和再贴现力度，提高金融服务小微企业、“三农”和支持服务业、节能环保等重点领域及重大民生工程的能力。二要抑制金融机构筹资成本的不合理上升，遏制变相高息揽储，维护良好的金融市场秩序。三要缩短企业融资链条，清理不必要的环节，整治层层加价行为。理财产品资金运用原则上应与实体经济直接对接。四要清理整顿不合理收费，对直接与贷款挂钩、没有实质服务内容的收费，一律取消。规范担保、评估、登记等收费。严禁“以贷转存”、“存贷挂钩”等行为。五要优化商业银行小微企业贷款管理，采取续贷提前审批、设立循环贷款等方式，提高贷款审批发放效率。对小微企业贷款实行差别化监管要求。六要积极稳妥发展面向小微企业和“三农”的特色中小金融机构，加快推动具备条件的民间资本依法发起设立中小型银行等金融机构，促进市场竞争，增加金融供给。七要大力发展直接融资，发展多层次资本市场，支持中小微企业依托中小企业股份转让系统开展融资，扩大中小企业债务融资工具及规模。八要完善商业银行考核评价指标体系，引导商业银行纠正单纯追逐利润、攀比扩大资产规模的行为。九要大力发展支持小微企业等获得信贷服务的保险产品，开展“保险+信贷”合作。积极发展政府支持的担保机构，扩大小微企业担保业务规模。十要有序推进利率市场化改革，充分发挥金融机构利率定价自律机制作用，增强财务硬约束，提高自主定价能力。综合考虑我国宏微观经济金融形势，完善市场利率形成和传导机制。会议要求，各有关部门要抓紧制定实施配套办法，定期督促检查，引入第三方评估，确保政策尽快落实、见到实效。
会议指出，在推进工商登记制度改革、废除企业年检制度、大力取消事前审批的同时，加快实施企业信息公示制度，从主要依靠行政审批管企业，转向更多依靠建立透明诚信的市场秩序规范企业，是创新政府事中事后监管的重要改革举措，有利于进一步转变政府职能，推进简政放权、放管结合，营造公平竞争市场环境，让“信用”成为社会主义市场经济体系的“基础桩”。会议审议通过《企业信息公示暂行条例（草案）》，建立了反映企业基本经营状况的年度报告公示制度，并要求即时公布股东出资、股权变更等信用信息，有关部门要对公示信息进行抽查。设立经营异常企业名录和严重违法企业名单制度，对不按时公示或隐瞒情况、弄虚作假的企业采取信用约束措施，在政府采购、工程招投标、国有土地出让等工作中依法予以限制或禁入。建立部门间互联共享信息平台，运用大数据等手段提升监管水平。对不守法、不诚信行为“广而告之”，让违法企业一处违规、处处受限；为诚实守信的企业树“金字招牌”，让诚信企业在公平竞争中不断增多壮大。
会议还研究了其他事项。"""]
				
				# 检查标题和正文是否全都符合格式
				if title[0].find("李克") != 0:
					print(f"title error!*****{response.url}")
					print(t_mode)
					print(title)
					print(content)
				if content[0].find("国务院总理") != 0 and content[0].find("新华社") != 0 and content[0].find(
						"日前") != 0:
					print(f"content error!*****{response.url}")
					print(c_mode)
					print(title)
					print(content)
				
				# 数据写入指定文件
				with open(f"data/{date}.txt", "w", encoding="utf-8-sig") as f:
					f.write(f"url:{response.url}\n")
					f.write("标题：\n")
					f.write(" ".join(title))
					f.write("\n")
					f.write("正文：\n")
					f.write(" ".join(content))
