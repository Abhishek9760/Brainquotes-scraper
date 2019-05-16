# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['brainyquote.com']

    def __init__(self, q):
        self.start_urls = ['http://brainyquote.com/topics/' + q]

    def parse(self, response):
        quotes =  response.xpath("//a[@title='view quote']/text()").extract()
        authors = response.xpath("//a[@title='view author']/text()").extract()
        tags = [i.xpath(".//a/text()").extract() for i in response.xpath("//div[@class='kw-box']")]

        next_page_url = response.xpath('//link[@rel="next"]/@href').extract_first()

        for quote,author,tag in zip(quotes, authors, tags):
            t = ','.join(tag)
            yield {
            'Quote' : quote,
            'Author' : author,
            'Tags' : t,
            }

        yield Request(next_page_url)





