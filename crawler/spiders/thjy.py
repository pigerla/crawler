# -*- coding: utf-8 -*-
import scrapy

from docx import Document
from scrapy.selector import Selector
from scrapy import log
from scrapy import Request
from crawler.items import CrawlerItem
from crawler.mongodb.thjy import Thjy

class ThjySpider(scrapy.Spider):
    name = "thjy"
    allowed_domains = ["thjy.org"]
    website = "http://www.thjy.org"
    start_urls = (
        'http://www.thjy.org/yaoxiahui/Column/635159619715156250.aspx',
    )

    def parse(self, response):
        sel = Selector(response)
        detail_pages = sel.xpath('//div[@class="detailsBox_head"]/h3/a[1]/@href').extract()
        for detail_page in detail_pages:
            url =  self.website + detail_page
            yield Request( url , callback= self.detail)

        totalPageString = sel.xpath('//a[@class="pagenaver last"]/@href').re(r'pid1=(\d+)')
        if len(totalPageString) > 0 :
            totalPageInt = int(totalPageString[0]) + 1
            for index in range(2 , totalPageInt):
                url = response.url + '?pid1=' + str(index)
                yield Request( url , callback= self.list)

    def list(self , response):
        sel = Selector(response)
        detail_pages = sel.xpath('//div[@class="detailsBox_head"]/h3/a[1]/@href').extract()
        for detail_page in detail_pages:
            url =  self.website + detail_page
            yield Request( url , callback= self.detail)

    def detail(self , response):

        items = CrawlerItem()

        sel = Selector(response)
        items['title'] = sel.xpath('//div[@class="detailsBox_head"]/h3/a[1]/text()').re(r'\s+(.*?)\s+')[0]
        items['link'] = response.url
        items['content'] = sel.xpath('//div[@class="detailsBox_content"]//text()').extract()
        # Thjy().insert(dict(items))
        return items






