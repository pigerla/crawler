__author__ = 'spy'
# encoding:utf-8
from crawler.tools.reactorManager import ReactorManager
from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings
from scrapy import signals
from scrapy import log


class MultiSpider:

    reactor = ReactorManager()

    def __init__(self):
        #启动日志
        # log.log.defaultObserver = MyObserver()
        # log.log.defaultObserver.start()
        # log.started = False
        log.start()
        pass

    def setup_spider(self,spider):
        '''
        运行爬虫
        :param spider:
        :return:
        '''
        settings = get_project_settings()
        crawler = Crawler(settings)
        crawler.signals.connect(self.reactor.stop, signal=signals.spider_closed)
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()
        self.reactor.add()

    def run(self):
        self.reactor.run()
