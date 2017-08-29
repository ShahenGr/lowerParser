# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PracticeareaSpider(scrapy.Spider):
    name = 'practiceArea'
    allowed_domains = ['http://bit.ly/2iENAQW']
    start_urls = ['http://bit.ly/2iENAQW']

    def parse(self, response):
        pass
        pArealist1 = response.xpath('//div[@id="practices-box-1"]/ul/li/a/@href')
        for link in pArealist1:
            absolute_url = response.urljoin(link.extract())
            yield scrapy.Request(absolute_url, callback=self.getStates, dont_filter=True)
        #pArealist2 = response.xpath('//div[@id="practices-box-2"]/ul/li/a/@href')
        #for link in pArealist2:
        #    absolute_url = response.urljoin(link.extract())
         #   print 'ABSOL --> ', absolute_url
         #   yield scrapy.Request(absolute_url, callback=self.getStates, dont_filter=True)

    def getStates(self, response):
        states = response.xpath('//div[@class="alphabetical-box"]/ul/li/a/@href')
        for link in states:
            absolute_url = response.urljoin(link.extract())
            yield scrapy.Request(absolute_url, callback=self.getCities, dont_filter=True)

    def getCities(self, response):
        yield scrapy.Request(response.url, callback=self.collectData, dont_filter=True)

    def collectData(self, response):
        lowerSummary = response.xpath("//div[@class='clearfix']/div/div[@class='lawyer-summary -align-top']")
        name = lowerSummary.xpath('//h5/a/span')

