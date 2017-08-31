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
        number = 1
        xCommand = '%s%s%s' % ('//div[@class="results-lawyers lawyer-card-group"]/div[@data-vars-value="',
                               number ,
                               '"]/div/div/div[@class="lawyer-summary -align-top"]')
        #lowerSummary = response.xpath("//div[@class='clearfix']/div/div[@class='lawyer-summary -align-top']")
        lowerSummary = response.xpath(xCommand)
        name = lowerSummary.xpath('div/h5/a/span/text()').extract()
        experience = lowerSummary.xpath('div/div/span/span/text()').extract()
        wPlacess = lowerSummary.xpath('div/div/span/text()').extract()
        phone_number = lowerSummary.xpath('div/div/div/strong/a/text()').extract()
        streetAndOthers = lowerSummary.xpath('div/div/div/span/span/text()').extract()
        nextPage = response.xpath('//div[@class="wrapper jcard has-padding-30 has-no-bottom-padding"]/div/span[@class="next"]/a/@href').extract()
        print "Name --> ", name

