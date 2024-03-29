# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class SnailItem(Item):
    # define the fields for your item here like:
    # name = Field()
    __name__ = Field()

class PostItem(SnailItem):
    __name__ = Field()
    name = Field()
    title = Field()
    author = Field()
    publish_time = Field()
    
    content = Field()
