from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from lxml import etree
import os
import webbrowser


def clean():
    try:
        os.remove("task1.xml")
        os.remove("task2.xml")
        os.remove("task2.xhtml")
    except OSError:
        pass


def get_data():
    process = CrawlerProcess(get_project_settings())
    process.crawl('basketball')
    process.crawl('meblilviv')
    process.start()


def task1():
    print("Task 1")
    root = etree.parse("task1.xml")
    hyperlinks = root.xpath("//fragment[@type='hyperlink']/text()")
    print("List of hyperlinks:")
    for h in hyperlinks:
        print(h)



def task2():
    print("Task 2")
    transform = etree.XSLT(etree.parse("task2.xsl"))
    result = transform(etree.parse("task2.xml"))
    result.write("task2.xhtml", pretty_print=True, encoding="UTF-8")


if __name__ == '__main__':
    print("Lab 1")
    clean()
    get_data()
    while True:
        print("-" * 30)
        print("Choose number of task")
        print("1. Task 1")
        print("2. Task 2")
        print("> ", end='', flush=True)
        number = input()
        if number == "1":
            task1()
        elif number == "2":
            task2()
        else:
            break

