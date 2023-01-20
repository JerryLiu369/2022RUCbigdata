import os
import time

import scrapy


class myspider(scrapy.Spider):
    name = "myRUCNews"
    
    def start_requests(self):
        if not os.path.exists("raw"):
            os.makedirs("raw")
        head = "http://news.ruc.edu.cn/archives/category/important_news/page/"
        for index in range(1, 207):
            if index == 1:
                yield scrapy.Request(url=head.removesuffix("/page/"), callback=self.parse)
            else:
                yield scrapy.Request(url=head + str(index), callback=self.parse)
            time.sleep(0.1)
        with open("news.csv","w",encoding="utf-8-sig") as f:
            for index in range(1, 207):
                with open(f"raw/{index}.csv","r",encoding="utf-8-sig") as ff:
                    f.write(ff.read())
            
        
    
    def parse(self, response):
        page = response.url.split("/")[-1]
        if page=="important_news":
            page="1"
        with open(f"raw/"+page+".csv","w",encoding="utf-8-sig") as f:
            for news in response.css('div.content_col_2_list ul li'):
                f.write((news.css('a::text').extract_first()+","+news.css('a::attr("href")').extract_first()+","+news.css("span::text").extract_first()).replace("\n"," ")+"\n")