import scrapy

class RucNewsSpider(scrapy.Spider):
    name = "RucNews"

    def start_requests(self):
        urls = [
            'https://news.ruc.edu.cn/archives/407847',
            'https://news.ruc.edu.cn/archives/408414'            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        

        title = response.css(".nc_title::text").extract_first()
        date = response.css(".date::text").extract_first()

        paragraphs = " ".join(response.css(".nc_body p::text").extract())

        yield {
                'title': title,
                'link':  date,
                "date": paragraphs
            }
     