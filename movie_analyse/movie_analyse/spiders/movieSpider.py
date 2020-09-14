# -*- coding: utf-8 -*-
import scrapy
from movie_analyse.items import MovieAnalyseItem

class MoviespiderSpider(scrapy.Spider):
    name = 'movieSpider'
    allowed_domains = ['imdb.cn']

    def start_requests(self):
        # 把所有的URL地址统一扔给调度器入队列
        for offset in range(0,30):
            url = 'https://www.imdb.cn/feature-film/?page={}'.format(offset)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )

    def parse(self, response):
        item = MovieAnalyseItem()
        href_list = response.xpath("//a[@class='img_box']/@href").getall()
        for i in href_list:
            #每部电影的详情链接
            href = "https://www.imdb.cn"+i
            yield scrapy.Request(href, meta=({'item': item}), callback=self.content)

    def content(self, response):
        item = response.meta["item"]
        item["director"] = response.xpath("//div[@class='txt_bottom_r txt_bottom_r_overflow']/a/text()").get()
        item["actors"] =  response.xpath("(//div[@class='txt_bottom_r txt_bottom_r_overflow'])[last()]/a/text()").getall()
        inform2 = response.xpath("//div[@class='txt_bottom_r']/text()").getall()
        item["name"] = response.xpath("//div[@class='per_txt fr']/h1/div/text()").get()
        item["grade"] = response.xpath("//em[@class='Z_grade_rate']/text()").get()
        item["keywords"] = response.xpath("//ul[@class='tvkw_link clear']//li/a/text()").getall()
        item["introduce"] = response.xpath("//div[@id='movie_desc_content']/p/text()").get()
        #item["box_office"] = response.xpath("//table[@class='boxoffice_con']/tbody/tr[last()]/td[2]/text()").get()
        item["genre"] = inform2[0]
        item["language"] = inform2[2]
        item["country"] = inform2[1]
        item["up_date"] = response.xpath("//div[@class='per_txt fr']/h1/div/span/text()").get()
        item["length"] = inform2[4]
        yield item




