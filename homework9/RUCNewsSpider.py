import scrapy


class myspider(scrapy.Spider):
    name = "myRUCNews"
    
    def start_requests(self):
        filename = "ruc_news.csv"
        with open(filename, 'w', encoding="utf-8"):
            pass
        urls = [
            'http://news.ruc.edu.cn/archives/category/important_news'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        filename = "ruc_news.csv"
        with open(filename, 'a', encoding="utf-8") as f:
            for news in response.css('div.content_col_2_list ul li'):
                title = news.css('a::text').extract_first()
                url = news.css('a::attr("href")').extract_first()
                date = news.css("span::text").extract_first()
                f.write(title)
                f.write(",")
                f.write(url)
                f.write(",")
                f.write(date)
                f.write("\n")
                
        next_page = response.css(".content_col_2_nav_alignright a::attr('href')").extract_first()
        if next_page is not None:
            # next_page = subresponse.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)
