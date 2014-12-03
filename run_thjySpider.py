__author__ = 'spy'

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log ,signals
from crawler.spiders.thjy import ThjySpider
from scrapy.utils.project import get_project_settings

thjySpider = ThjySpider()
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop , signal= signals.spider_closed)
crawler.configure()
crawler.crawl(thjySpider)
crawler.start()
log.start()
reactor.run()

# This is a sample above of running spider(s) by file but not command