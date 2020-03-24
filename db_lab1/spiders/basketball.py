# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response import Response


class BasketballSpider(scrapy.Spider):
    name = "basketball"
    allowed_domains = ['basketball365.ru']
    start_urls = [
        'http://basketball365.ru/'
    ]

    def parse(self, response: Response):
        images = response.xpath("//img/@src")
        texts = response.xpath("//*[not(self::script)][not(self::style)][string-length(normalize-space(text())) > "
                               "30]/text()")
        hyperlinks = response.xpath("//a/@href")
        yield {
            'url': response.url,
            'payload': [{
                'type': 'text',
                'data': text.get()
            } for text in texts] + [{
                'type': 'image',
                'data': image.get()
            } for image in images] + [{
                'type': 'hyperlink',
                'data': hyperlink.get()
            } for hyperlink in hyperlinks]
        }
        if response.url == self.start_urls[0]:
            links = response.xpath("//a/@href")
            selected_links = list(set(link.get() for link in links))[:19]
            for link in selected_links:
                yield scrapy.Request('http://basketball365.ru' + link, self.parse)
