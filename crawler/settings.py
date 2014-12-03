# -*- coding: utf-8 -*-

# Scrapy settings for crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
# Base settings
BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

#mongoDB settings
MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'crawler'

# pipelines setting before using pipelines
ITEM_PIPELINES = {
    'crawler.pipelines.CrawlerPipeline': 1,
}

# The number of running spiders at the same time(default value)
CONCURRENT_REQUESTS = 100

# set delay time
DOWNLOAD_DELAY = 0.5

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawler (+http://www.yourdomain.com)'
