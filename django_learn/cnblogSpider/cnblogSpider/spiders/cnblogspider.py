# coding: utf-8
import scrapy
import sys
sys.path.append("F:\Scrapy\cnblogSpider\cnblogSpider")
from items import CnblogspiderItem
from scrapy.selector import Selector
class CnblogsSpider(scrapy.Spider):
	name = 'cnblogs'
	allowed_domains = ['cnblogs.com']
	start_urls = [
	    "http://www.cnblogs.com/qiyeboy/default.html?page=1"
	]

	def parse(self, response):
		# 抽取所有的文章

		papers = response.xpath(".//*[@class='day']")
		for paper in papers:
			url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
			title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
			time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
			content = paper.xpath(".//*[@class='postCon']/div/text()").extract()[0]
			item = CnblogspiderItem(url = url, title = title, time = time, content = content) #创建CnblogspiderItem对象 并保存数据
			request = scrapy.Request(url=url, callback=self.parse_body)
			request.meta['item'] = item
			yield request
            
		next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
		if next_page:
			yield scrapy.Request(url=next_page[0],callback=self.parse)

	def parse_body(self,response):
		item=response.meta['item']
		body=response.xpath(".//*[@class='postBody']")
		item['cimage_urls'] = body.xpath('.//img//@src').extract()
		yield item


        	