# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    type=scrapy.Field()
    url=scrapy.Field()
    time=scrapy.Field()
    related_topics=scrapy.Field()



class BbcmediaItem(scrapy.Item):
    url=scrapy.Field()
    title=scrapy.Field()
    type=scrapy.Field()

    pass
