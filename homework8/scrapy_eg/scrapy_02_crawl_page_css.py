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
        page = response.url.split("/")[-1]
        filename ="ruc_news_" + page + '_css.txt'

        title = response.css(".nc_title::text").extract_first()
        date = response.css(".date::text").extract_first()

        paragraphs = response.css(".nc_body p::text").extract()

        #yield {title}
        with open(filename, 'w') as f:
            f.write(date)
            f.write("\t")
            f.write(title)
            f.write("\n")
            for para in paragraphs:
                f.write(para)
                f.write("\n")
        print('Saved file ' +  filename)