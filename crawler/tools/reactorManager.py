__author__ = 'spy'
# encoding:utf-8

from twisted.internet import reactor
from scrapy import log
#管理Reactor启动关闭
class ReactorManager:

    def __init__(self):
        self.spiderCounter = 0

    def run(self):
        reactor.run()

    def stop(self):
        self.spiderCounter -= 1
        log.msg("[stopMethod] Spider Number : " + str(self.spiderCounter))
        if self.spiderCounter == 0:
            reactor.stop()
            log.msg("---------------------All crawlers finish --------------------")

    def add(self):
        self.spiderCounter += 1
        log.msg("[addMethod] Spider Number : " + str(self.spiderCounter))