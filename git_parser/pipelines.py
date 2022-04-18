import pymongo
from pymongo import MongoClient
from git_parser import settings

class MongoDbPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['scrapy_repo_db']
        self.collection = db['repo_inf_tb']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item

