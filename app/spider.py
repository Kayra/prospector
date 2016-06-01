from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class ProspectorSpider(CrawlSpider):

    name = "prospector"
    allowed_domains = []
    start_urls = []

    rules = (Rule(LinkExtractor(), callback="parse_item"))

    def _string_joiner(self, data):
        if len(data) > 1:
            return '#'.join(data)
        elif len(data) == 1:
            return data[0]
        else:
            return None

    def parse_item(self, response):

        page_data = {}

        for header_number in range(1, 4):
            page_data["h" + header_number + "s"] = self._string_joiner(response.css("h" + header_number).extract())

        return page_data
