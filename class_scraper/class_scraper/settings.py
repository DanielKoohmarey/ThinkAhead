# Scrapy settings for class_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'class_scraper'

SPIDER_MODULES = ['class_scraper.spiders']
NEWSPIDER_MODULE = 'class_scraper.spiders'
ITEM_PIPELINES = {
    'class_scraper.pipelines.CleanUnicodePipeline': 1, 
    'class_scraper.pipelines.WritePipeline': 2, 
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'class_scraper (+http://www.yourdomain.com)'
