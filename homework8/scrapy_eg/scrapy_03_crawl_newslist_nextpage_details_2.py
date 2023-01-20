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
            url1 = news.css("a::attr('href')").extract_first().strip()
            yield {"date": date, "title": title, "url":url1}

            #
            
            yield scrapy.Request(url=url1, callback=self.parseDetails)

        next_page = response.css(".content_col_2_nav_alignright a::attr('href')").extract_first()        
        if next_page is not None:
            #next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)            
    
    def parseDetails(self, response):
        #page = response.url.split("/")[-1]
        filename ="ruc_news.txt"
        title = response.css(".nc_title::text").extract_first()
        date = response.css(".date::text").extract_first()
        views = response.css(".views::text").extract_first()
        authors = ",".join(response.css(".nc_author::text").extract())

        content = " ".join(response.css(".nc_body p::text").extract())

        

        #yield {title}
        with open(filename, 'at') as f:
            f.write(title)
            f.write("\t")
            f.write(date)
            f.write("\t")

            f.write(views)
            f.write("\t")
            f.write(authors)
            f.write("\t")
            f.write(content)
        print('Saved file ' +  filename)