# -*- coding: utf-8 -*-
import scrapy
from ..items import LogintestItem
from scrapy import FormRequest, Request
import requests
from lxml import etree


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['github.com']
    login_url = ['https://github.com/login']

    def start_requests(self):
        for url in self.login_url:
            yield Request(url, meta={'cookiejar': 1}, callback=self.parse)

    def parse(self, response):
        authenticity_token = response.xpath(".//*[@id='login']/form/input[2]/@value").extract_first()
        data = {'commit': 'Sign in',
                'utf8': '✓',
                'authenticity_token': authenticity_token,
                'login': '2300855016@qq.com',
                'password': '2394986394.com'
                }
        return FormRequest(
                         url='https://github.com/session',
                         formdata=data,
                         meta={'cookiejar': response.meta['cookiejar']},
                         callback=self.after_parse)

    def after_parse(self, response):
        result = response.xpath('//span[contains(@class,"css-truncate")]/text()').extract()
        item = LogintestItem()
        for i in result:
            item['head'] = i
            yield item

