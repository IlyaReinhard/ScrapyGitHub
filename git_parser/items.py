# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GitParserItem(scrapy.Item):
    repo_name = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    stars_count = scrapy.Field()
    forks_count = scrapy.Field()
    watch_count = scrapy.Field()
    commits_count = scrapy.Field()
    pass
