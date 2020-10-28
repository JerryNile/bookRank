import scrapy
a = []
for i in range(1,21):
    a.append('http://www.yc.ifeng.com/store/79_0_favorite_total_2_'+str(i))
class Rankbook1000Spider(scrapy.Spider):
    name = 'rankBook1000'
    allowed_domains = ['yc.ifeng.com']
    start_urls = a
    def parse(self, response):
        books = response.xpath('//div[@id="book_list"]/table/tbody/tr')
        for book in books:
           book_num = book.xpath('./td[@class="col-num"]/text()').extract()
           book_type = book.xpath('./td[2]/a/em/text()').extract()
           book_name = book.xpath('./td[@class="col-name"]/a/strong/text()').extract()
           book_author = book.xpath('./td[4]/a/text()').extract()
           book_time = book.xpath('./td[5]/text()').extract()
           yield {
               '排名': book_num,
               '类型': book_type,
               '书名/章节': book_name,
               '作者': book_author,
               '更新时间': book_time
           }