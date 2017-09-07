# -*- coding: utf-8 -*-
import scrapy


class LowerparserItem(scrapy.Item):
    url = scrapy.Field()
    image = scrapy.Field()
    name = scrapy.Field()
    experience = scrapy.Field()
    firm_name = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    zip = scrapy.Field()
    country = scrapy.Field()
    phone = scrapy.Field()
    fax = scrapy.Field()
    website = scrapy.Field()
    practice = scrapy.Field()
