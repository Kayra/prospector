from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class ProspectorSpider(CrawlSpider):

    name = "prospector"
    allowed_domains = []
    start_urls = []

    rules = (Rule(LinkExtractor(), callback="parse_item"))

    def parse_item(self, response):
        pass
