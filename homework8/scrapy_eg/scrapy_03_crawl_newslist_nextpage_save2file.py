import scrapy
class RucInfoSpider(scrapy.Spider):
    name = "info"

    def start_requests(self):
        urls = [
            'http://news.ruc.edu.cn/archives/category/important_news'         
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for news in response.css(".content_col_2_list li"): #一条新闻
            date = news.css(".date::text").extract_first().strip()
            title = news.css("a::text").extract_first().strip()
            url = news.css("a::attr('href')").extract_first().strip()
            yield {"date": date, "title": title, "url":url}

        next_page = response.css(".content_col_2_nav_alignright a::attr('href')").extract_first()        
        if next_page is not None:
            #next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)            
            