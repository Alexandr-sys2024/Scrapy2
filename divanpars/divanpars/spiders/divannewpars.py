import scrapy
import csv


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet?types%5B%5D=136"]

    def parse(self, response):
        luminaires = response.css('div._Ud0k')
        for luminaire in luminaires:
            yield{
                'name' : luminaire.css('div.lsooF span::text').get(),
                'price': luminaire.css('div.pY3d2 span::text').get(),
                'url': luminaire.css('a').attrib['href']
            }

