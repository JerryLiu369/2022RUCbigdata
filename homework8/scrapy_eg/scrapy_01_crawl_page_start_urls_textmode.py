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
        filename ="ruc_news_" + page + '.txt'
        with open(filename, 'wt') as f:
            f.write(response.text)
        print('Saved file ' +  filename)