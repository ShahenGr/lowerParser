# -*- coding: utf-8 -*-
import scrapy
from lowerParser.items import LowerparserItem


class PracticeareaSpider(scrapy.Spider):
    name = 'practiceArea'
    allowed_domains = ['http://bit.ly/2iENAQW']
    start_urls = ['http://bit.ly/2iENAQW']

    def parse(self, response):
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
        for number in xrange(1, 41):
            xCommand = '%s%s%s' % ('//div[@class="results-lawyers lawyer-card-group"]/div[@data-vars-value="',
                                   number,
                                   '"]/div/div/div[@class="lawyer-summary -align-top"]')
            lowerSummary = response.xpath(xCommand)
            lowerPage = lowerSummary.xpath('div/h5/a/@href')
            lp = lowerPage.extract()[0]
            yield scrapy.Request(lp, callback=self.collectData, dont_filter=True)

    def collectData(self, response):
        image = response.xpath('//div[@class="lawyer-avatar-wrapper"]/div/img/@src').extract()
        name = response.xpath('//div[@class="lawyer-coreinfo has-padding-30 has-no-bottom-padding"]/h1/text()').extract()
        firm_name = response.xpath('//div[@class="lawyer-coreinfo has-padding-30 has-no-bottom-padding"]/span/text()').extract()
        experience = response.xpath('//ul[@class="-hide-landscape-tablet lawyer-key-info list-gutter--tiny has-no-padding has-no-top-margin"]/li/time/text()').extract()
        address =  response.xpath('//div[@itemprop="address"]/div/div/text()').extract()
        city = response.xpath('//div[@itemprop="address"]/div/span[@class="locality"]/text()').extract()
        state = response.xpath('//div[@itemprop="address"]/div/span[@class="region"]/text()').extract()
        zip = response.xpath('//div[@itemprop="address"]/div/span[@class="postal-code"]/text()').extract()
        country = response.xpath('//div[@itemprop="address"]/div/span[@class="country"]/text()').extract()
        phone = response.xpath('//span[@itemprop="telephone"]/text()').extract()
        fax = response.xpath('//span[@itemprop="faxNumber"]/text()').extract()
        website = response.xpath('//dt[@class="dsc-term"]/a/@href').extract()
        practice_areas = response.xpath('//ul[@class="has-no-list-styles"]/li/text()').extract()

        item = LowerparserItem()
        item['url'] = response.url
        item['image'] = self.clearData(image)
        item['name'] = self.clearData(name)
        item['experience'] = self.clearData(experience)
        item['firm_name'] = self.clearData(firm_name)
        item['address'] = self.clearData(address)
        item['city'] = self.clearData(city)
        item['state'] = self.clearData(state)
        item['zip'] = self.clearData(zip)
        item['country'] = self.clearData(country)
        item['phone'] = self.clearData(phone)
        item['fax'] = self.clearData(fax)
        item['website'] = self.clearData(website)
        item['practice'] = practice_areas
        yield item

    def clearData(self, data=[]):
        if data:
            return data[0].strip()
        else:
            return None

