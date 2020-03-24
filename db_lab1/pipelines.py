# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from lxml import etree


class DbLab1Pipeline(object):
    def __init__(self):
        self.root = None

    def open_spider(self, spider):
        self.root = etree.Element("data" if spider.name == "basketball" else "shop")

    def close_spider(self, spider):
        with open("task%d.xml" % (1 if spider.name == "basketball" else 2), 'wb') as f:
            f.write(etree.tostring(self.root, encoding="UTF-8", pretty_print=True, xml_declaration=True))

    def process_item(self, item, spider):
        if spider.name == "basketball":
            page = etree.Element("page", url=item["url"])
            for payload in item["payload"]:
                fragment = etree.Element("fragment", type=payload["type"])
                fragment.text = payload["data"]
                page.append(fragment)
            self.root.append(page)
        else:
            product = etree.Element("product")
            description = etree.Element("description")
            description.text = item["description"]
            price = etree.Element("price")
            price.text = item["price"]
            image = etree.Element("image")
            image.text = item["img"]
            product.append(description)
            product.append(price)
            product.append(image)
            self.root.append(product)
        return item
