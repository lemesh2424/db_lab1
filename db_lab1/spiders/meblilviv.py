from scrapy.http.response import Response
import scrapy


class MeblilvivSpider(scrapy.Spider):
    name = "meblilviv"
    allowed_domains = ["mebli-lviv.com.ua"]
    start_urls = ['https://mebli-lviv.com.ua/ua/kitchen-tables/']

    def parse(self, response: Response):
        products = response.xpath("//div[contains(@class, 'product-block')]")[:20]
        for product in products:
            yield {
                'img': product.xpath(".//img[contains(@class, 'img-responsive')]/@src").get(),
                'price': product.xpath(".//span[contains(@class, 'special-price')]/text()").get(),
                'description': product.xpath(".//h3[contains(@class, 'name')]/a/text()").get()
            }
