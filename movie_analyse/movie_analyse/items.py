# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieAnalyseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    genre = scrapy.Field()
    language = scrapy.Field()
    actors = scrapy.Field()
    director = scrapy.Field()
    country = scrapy.Field()
    up_date = scrapy.Field()
    length = scrapy.Field()
    introduce = scrapy.Field()
    grade = scrapy.Field()
    keywords = scrapy.Field()
    #box_office = scrapy.Field()
    #comment = scrapy.Field()




