# Scrapy settings for snail project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'snail'

SPIDER_MODULES = ['snailSpider.spiders']
NEWSPIDER_MODULE = 'snailSpider.spiders'

ITEM_PIPELINES = ['snailSpider.pipelines.SnailPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'snail (+http://www.yourdomain.com)'
