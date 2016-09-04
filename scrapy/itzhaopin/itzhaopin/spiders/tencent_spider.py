import re
import json


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from itzhaopin.items import *
from itzhaopin.misc.log import *


class TencentSpider(CrawlSpider):
    name = "tencent"
    allowed_domains = ["wljx.net"]
    start_urls = [
        "http://www.wljx.net/forum-36-1.html"
    ]
    rules = [
        Rule(sle(allow=("http://www.wljx.net/thread-\d{5}-[\s\S]*.html")), follow=True, callback='parse_item')
    ]

    def parse_item(self, response):
        items = []
        sel = Selector(response)
        base_url = get_base_url(response)
       
        #sites_odd = sel.css('td#postmessage_13023')
        #for site in sites_odd:
        item = TencentItem()
        item['name'] = ''.join(response.xpath('//td[starts-with(@id, "postmessage")]/text()').re("[\s\S]+"))
        item['title'] = ''.join(response.xpath('//title/text()').extract())
            #relative_url = site.css('.l.square a').xpath('@href').extract()[0] 
            #item['detailLink'] = urljoin_rfc(base_url, relative_url)
            #item['catalog'] = site.css('tr > td:nth-child(2)::text').extract()[0]
            #item['workLocation'] = site.css('tr > td:nth-child(4)::text').extract()[0]
            #item['recruitNumber'] = site.css('tr > td:nth-child(3)::text').extract()[0]
            #item['publishTime'] = site.css('tr > td:nth-child(5)::text').extract()[0]
        items.append(item)
            #print repr(item).decode("unicode-escape") + '\n'

        info('parsed ' + str(response))
        return items


    def _process_request(self, request):
        info('process ' + str(request))
        return request

