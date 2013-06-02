#/usr/bin/env python
#coding=utf-8
#from urlparse import urljoin  
#import simplejson  
  
#from scrapy.http import Request  
from scrapy.contrib.spiders import CrawlSpider, Rule  
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor  
from scrapy.selector import HtmlXPathSelector  

from snailSpider.items import PostItem

class MainSpider(CrawlSpider):  
    name = 'snailSpider'  
    rules = (  
        #下面是符合规则的网址,但是不抓取内容,只是提取该页的链接
        #Rule(SgmlLinkExtractor(allow=(r'http://sale.jd.com/'))),  
        #下面是符合规则的网址,提取内容
        Rule(SgmlLinkExtractor(allow=(r'/team-\d+')), callback="parse_item"),  
    )  

    def start_requests(self):
	#self.allowed_domains = ['jd.com']
	# load seeds
	start_urls = [
            "http://tuan.jd.com/beijing-0-0-0-0-0-0-1-0-0.html",
    	]  
	for url in start_urls:
	    yield self.make_requests_from_url(url)

    def parse_item(self, response):  
        hxs = HtmlXPathSelector(response)  
        item = PostItem()  
	print 'AAAAAAAAAAAAAAAAAAAAAAAAA: parse_item'
	# 提取内容
        #item['name'] = hxs.select('//div[@class="h1_title book_head"]/h1/text()').extract()[0]  
        #item['author'] = hxs.select('//div[@class="book_detailed"]/p[1]/a/text()').extract()  
        #publisher = hxs.select('//div[@class="book_detailed"]/p[2]/a/text()').extract()  
        #item['publisher'] = publisher and publisher[0] or ''  
        #publish_date = hxs.select('//div[@class="book_detailed"]/p[3]/text()').re(u"[\u2e80-\u9fffh]+\uff1a([\d-]+)")  
        #item['publish_date'] = publish_date and publish_date[0] or ''  
        #prices = hxs.select('//p[@class="price_m"]/text()').re("(\d*\.*\d*)")  
        #item['price'] = prices and prices[0] or ''  
	item['name'] = 'aaskfjaksjftest_name'
        return item  

