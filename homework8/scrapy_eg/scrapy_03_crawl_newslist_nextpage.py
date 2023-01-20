import scrapy
class RucInfoSpider(scrapy.Spider):
    name = "info"

    maxpage = 3
    page = 0

    def start_requests(self):
        urls = [
            'http://news.ruc.edu.cn/archives/category/important_news'         
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        self.page= self.page+1
        print ("正在采集第" + str(self.page)+"页")
        with open("ruc_news_list_all.txt", 'a') as f:        
            for news in response.css('div.content_col_2_list ul li'):
                f.write(news.css('a::text').extract_first()),
                f.write("\t")
                f.write(news.css('a::attr("href")').extract_first()),
                f.write("\t")
                f.write(news.css("span::text").extract_first()),
                f.write("\n")     
        if self.page>= self.maxpage:
            return

        next_page = response.css(".content_col_2_nav_alignright a::attr('href')").extract_first()        
        if next_page is not None:
            #next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)            
            