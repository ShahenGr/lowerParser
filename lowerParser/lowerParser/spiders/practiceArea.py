# -*- coding: utf-8 -*-
import scrapy


class PracticeareaSpider(scrapy.Spider):
    name = 'practiceArea'
    allowed_domains = ['http://bit.ly/2iENAQW']
    start_urls = ['http://bit.ly/2iENAQW']

    BASE_URL = 'https://www.justia.com'

    def parse(self, response):
        pArealist1 = response.xpath('//div[@id="practices-box-1"]/ul/li/a/@href')
        for link in pArealist1:
            absolute_url = self.BASE_URL + link.extract()
            yield scrapy.Request(absolute_url, callback=self.getStates)
        pArealist2 = response.xpath('//div[@id="practices-box-2"]/ul/li/a/@href')
        for link in pArealist2:
            absolute_url = self.BASE_URL + link.extract()
            yield scrapy.Request(absolute_url, callback=self.getStates)

    def getStates(self, response):
        print response.url
