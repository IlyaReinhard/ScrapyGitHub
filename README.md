# ScrapyGitHub
Scrapy project for parsing GitHub pages. 

* Basic structure for scrapy.
* Configuration of scrapy in order to access GitHub pages and scraping data.
* Basic scrapy pipeline to save crawled objets to MongoDB locally.
* Basic spider definition



## Setup
1 - Install venv
````
$ python3 -m venv venv && source venv/bin/activate
````
2 - Install requirements.txt
````
$ pip3 install -r requirements.txt
````
3 - Configure MongoDB in Scrapy pipelines.py
````
import pymongo
from pymongo import MongoClient
from git_parser import settings

class MongoDbPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost', # Change to your host if your deploy on Cloud database
            27017
        )
        db = self.conn['scrapy_repo_db']
        self.collection = db['repo_inf_tb']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
        
 ````
 


## Start the project
In order to start this project you will need to run crawling by the console

````
$ crapy crawl <name-of-your-spider>
````
Or if you want to save data to file, add file with extension in the end of command
````
$ crapy crawl <name-of-your-spider> -O <name-file>.json

````


