# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

class SnailPipeline(object):
    def process_item(self, item, spider):
	print 'BBBBB SnailPipeline:', item['name']
        return item
