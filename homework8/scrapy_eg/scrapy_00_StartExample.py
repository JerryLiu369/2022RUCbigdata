
#引入Scrapy包
import scrapy

#定义了一个类，这个类必须继承scrapy.Spider，说明这个类中包装了一个爬虫。
class RucNewsSpider(scrapy.Spider):

    #这个爬虫的名字是RucNews
    name = "RucNews"

    #定义start_requests函数，函数名和参数必须和下面一致：
    def start_requests(self):
        #指定要爬取的网页的网址
        url = "http://news.ruc.edu.cn/archives/category/important_news"
        

        #发送请求，抓取这个网页的内容，指定抓取下来后，用self.parse函数解析
        yield scrapy.Request(url=url, callback=self.parse)

    #这个就是scrapy.Request指定的callback函数
    #参数固定，response是抓取到的内容的封装对象
    def parse(self, response):
        for news in response.css('div.content_col_2_list ul li'):
            print("*******************")
            print(news.css('a::text').extract_first()+","+news.css('a::attr("href")').extract_first()+","+news.css("span::text").extract_first()+"\n")
            yield {
                '标题': news.css('a::text').extract_first(),
                '链接':  news.css('a::attr("href")').extract_first(),
                "日期": news.css("span::text").extract_first()
            }
