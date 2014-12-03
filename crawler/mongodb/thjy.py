__author__ = 'spy'

from __init__ import MongoConnection


class Thjy:
    def __init__(self):
        self.collection = MongoConnection.crawler.thjy

    def insert(self , document):
        self.collection.insert(document)

    def add(self, query, document):
        self.collection.update(query, document, True)

    def find(self, query):
        self.collection.find(query)