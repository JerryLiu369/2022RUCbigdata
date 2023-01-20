import scrapy


class RucNewsSpider(scrapy.Spider):
    name = "RucNews"

    #def start_requests(self):
    #    urls = [
    #        'http://news.ruc.edu.cn/archives/263466',
    #        'http://news.ruc.edu.cn/archives/263470'         
    #    ]
    #    for url in urls:
    #        yield scrapy_.Request(url=url, callback=self.parse)

    #简略格式
    start_urls = [
         'https://news.ruc.edu.cn/archives/407847',
         'https://news.ruc.edu.cn/archives/408414'  
    ]

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename ="ruc_news_" + page + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        print('Saved file ' +  filename)