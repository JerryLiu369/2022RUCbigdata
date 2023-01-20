import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = ['https://news.ruc.edu.cn/archives/295925',
            'https://news.ruc.edu.cn/archives/296855',
            'https://news.ruc.edu.cn/archives/296470',
            'https://news.ruc.edu.cn/archives/296701',
            'https://news.ruc.edu.cn/archives/296782',
            'https://news.ruc.edu.cn/archives/296680',
            'https://news.ruc.edu.cn/archives/295949',
            'https://news.ruc.edu.cn/archives/295995',
            'https://news.ruc.edu.cn/archives/296043',
            'https://news.ruc.edu.cn/archives/296175',
            'https://news.ruc.edu.cn/archives/295932',
            'https://news.ruc.edu.cn/archives/296077',
            'https://news.ruc.edu.cn/archives/295696',
            'https://news.ruc.edu.cn/archives/296201',
            'https://news.ruc.edu.cn/archives/295899',
            'https://news.ruc.edu.cn/archives/295890',
            'https://news.ruc.edu.cn/archives/295882',
            'https://news.ruc.edu.cn/archives/295798',
            'https://news.ruc.edu.cn/archives/295849',
            'https://news.ruc.edu.cn/archives/295666',
            'https://news.ruc.edu.cn/archives/295640',
            'https://news.ruc.edu.cn/archives/295620',
            'https://news.ruc.edu.cn/archives/295508',
            'https://news.ruc.edu.cn/archives/295409',
            'https://news.ruc.edu.cn/archives/295267',
            'https://news.ruc.edu.cn/archives/295469',
            'https://news.ruc.edu.cn/archives/295240',
            'https://news.ruc.edu.cn/archives/295127',
            'https://news.ruc.edu.cn/archives/295091',
            'https://news.ruc.edu.cn/archives/295080',
            'https://news.ruc.edu.cn/archives/295272',
            'https://news.ruc.edu.cn/archives/295126',
            'https://news.ruc.edu.cn/archives/295219',
            'https://news.ruc.edu.cn/archives/294920',
            'https://news.ruc.edu.cn/archives/294855',
            'https://news.ruc.edu.cn/archives/294842',
            'https://news.ruc.edu.cn/archives/295015',
            'https://news.ruc.edu.cn/archives/294827',
            'https://news.ruc.edu.cn/archives/294919',
            'https://news.ruc.edu.cn/archives/294771',
            'https://news.ruc.edu.cn/archives/294732',
            'https://news.ruc.edu.cn/archives/294790',
            'https://news.ruc.edu.cn/archives/294914',
            'https://news.ruc.edu.cn/archives/294696',
            'https://news.ruc.edu.cn/archives/294440',
            'https://news.ruc.edu.cn/archives/294049',
            'https://news.ruc.edu.cn/archives/294314',
            'https://news.ruc.edu.cn/archives/294406',
            'https://news.ruc.edu.cn/archives/294417',
            'https://news.ruc.edu.cn/archives/294223',
            'https://news.ruc.edu.cn/archives/294259',
            'https://news.ruc.edu.cn/archives/294130',
            'https://news.ruc.edu.cn/archives/294044',
            'https://news.ruc.edu.cn/archives/293608',
            'https://news.ruc.edu.cn/archives/294025',
            'https://news.ruc.edu.cn/archives/293919',
            'https://news.ruc.edu.cn/archives/293806',
            'https://news.ruc.edu.cn/archives/293917',
            'https://news.ruc.edu.cn/archives/293962',
            'https://news.ruc.edu.cn/archives/293637',
            'https://news.ruc.edu.cn/archives/293640',
            'https://news.ruc.edu.cn/archives/293760',
            'https://news.ruc.edu.cn/archives/293872',
            'https://news.ruc.edu.cn/archives/293561',
            'https://news.ruc.edu.cn/archives/293447',
            'https://news.ruc.edu.cn/archives/293414',
            'https://news.ruc.edu.cn/archives/293290',
            'https://news.ruc.edu.cn/archives/293382',
            'https://news.ruc.edu.cn/archives/293816',
            'https://news.ruc.edu.cn/archives/293365',
            'https://news.ruc.edu.cn/archives/292953',
            'https://news.ruc.edu.cn/archives/292918',
            'https://news.ruc.edu.cn/archives/292689',
            'https://news.ruc.edu.cn/archives/293032']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename ="ruc_news_" + page + '.txt'

        title = response.css(".nc_title::text").extract_first()
        date = response.css(".date::text").extract_first()
        views = response.css(".views::text").extract_first()
        authors = ",".join(response.css(".nc_author::text").extract())

        content = "\n".join(response.css(".nc_body p::text").extract())

        

        #yield {title}
        with open(filename, 'w') as f:
            f.write(title)
            f.write("\n")
            f.write(date)
            f.write("\n")

            f.write(views)
            f.write("\n")
            f.write(authors)
            f.write("\n")
            f.write(content)
        print('Saved file ' +  filename)