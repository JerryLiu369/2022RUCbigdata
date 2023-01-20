import scrapy


class RucNewsSpider(scrapy.Spider):
    name = "RucNews"

    #简略格式
    start_urls = [
         'https://news.ruc.edu.cn/archives/407847',
         'https://news.ruc.edu.cn/archives/408414'  
    ]

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename ="ruc_news_" + page + '_content.txt'

        html = response.text

        #<div class="nc_title">有温度的人工智能：为科教兴国、人才强国贡献人大智慧！</div>
        #<div class="nc_subtitle"></div>
        #<div class="nc_meta">
        #    <span class="date">2022-11-02 11:32:34</span> 
        #    <div class="views">11,809 次浏览</div>
        #</div>
        #<div class="nc_author">来源：党委宣传部 高瓴人工智能学院</div>


        start = html.find("<div class=\"nc_title\">") + len("<div class=\"nc_title\">")
        #注意这里的find的第一个参数
        end = html.find("</div>", start)
        title = html[start:end]


        start = html.find("<span class=\"date\">") + len("<span class=\"date\">")
        #注意这里的find的第一个参数
        end = html.find("</span>", start)
        newsdate = html[start:end]
        

        #去除掉字符串两头的空白符
        title = title.strip()

        with open(filename, 'wt') as f:
            f.write(newsdate+"\t"+ title)
        print('Saved file ' +  filename)