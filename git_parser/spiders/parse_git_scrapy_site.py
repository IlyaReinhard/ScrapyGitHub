import scrapy
from scrapy.spiders import  CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RepoSpider(CrawlSpider):
    name = 'repo_scrapy'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/orgs/scrapy/repositories']

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://github.com/orgs/scrapy/repositories', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3[@class="wb-break-all"]/a'), callback='parse_repo', follow=True, process_request='set_user_agent'),
    )

    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request


    def parse_repo(self, response):

        yield {
            'repo_name': response.xpath('//strong[@class="mr-2 flex-self-stretch"]/a/text()').get(),
            'description': self.exist_description(response),
            'Link': response.xpath('//span[@class="flex-auto min-width-0 css-truncate css-truncate-target width-fit"]/a/@href').get(),
            'stars_count': response.xpath('//span[@id="repo-stars-counter-star"]').xpath('@title').get(),
            'forks_count': response.xpath('//span[@id="repo-network-counter"]').xpath('@title').get(),
            'watch_count': response.xpath('//a[@class="Link--muted"]/strong/text()')[1].get(),
            'commits_count': response.xpath("//span[@class='d-none d-sm-inline']/strong/text()").get(),
            'last_commit_inf': {'author': response.xpath("//div[@class='css-truncate css-truncate-overflow color-fg-muted']/a/text()").get(),
                                'title': self.last_commit_take_information(response),

                                'date_of_created': response.xpath("//a[@class='Link--secondary ml-2']/relative-time/@datetime").get()
                                },
            'release_count': response.xpath("//h2[@class='h4 mb-3']/a/span").xpath('@title').get(),
            'last_release_inf': {'version': response.xpath("//span[@class='css-truncate css-truncate-target text-bold mr-2']/text()").get(),
                                 'created_data': response.xpath("//div[@class='text-small color-fg-muted']/relative-time/@datetime").get()},

        }

    def exist_description(self, response):
        if response.xpath('//p[@class="f4 mb-3"]/text()').get() is None:
            return None
        else:
            return response.xpath('//p[@class="f4 mb-3"]/text()').get().strip()


    def last_commit_take_information(self, response):
        if response.xpath("//pre[@class='mt-2 text-mono color-fg-muted text-small ws-pre-wrap']/text()").get() is None:
            return response.xpath('//a[@class="Link--primary markdown-title"]/text()').get()










