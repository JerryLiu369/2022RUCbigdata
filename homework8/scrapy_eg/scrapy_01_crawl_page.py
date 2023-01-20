import scrapy

class RucNewsSpider(scrapy.Spider):
    name = "RucNews"

    def start_requests(self):
        urls = [
            'https://news.ruc.edu.cn/archives/407847'   
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)    

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename ="ruc_news_" + page + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        print('Saved file ' +  filename)
