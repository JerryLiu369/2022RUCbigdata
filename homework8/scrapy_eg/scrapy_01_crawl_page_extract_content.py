import scrapy


class RucNewsSpider(scrapy.Spider):
    name = "RucNews"

    #简略格式
    start_urls = [
         'https://news.ruc.edu.cn/archives/407847',
         'https://news.ruc.edu.cn/archives/408414'  
    ]

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename ="ruc_news_" + page + '_content.txt'

        html = response.text
        start = html.find("<title>") + len("<title>")
        end = html.find("</title>")

        title = html[start:end]

        #去除掉字符串两头的空白符
        title = title.strip()

        with open(filename, 'wt') as f:
            f.write(title)
        print('Saved file ' +  filename)