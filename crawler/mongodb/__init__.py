__author__ = 'spy'

from mongokit import Connection
from crawler import settings

MongoConnection = Connection(settings.MONGODB_SERVER, settings.MONGODB_PORT)