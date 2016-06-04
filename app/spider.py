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

        page_data["alttags"] = self._string_joiner(response.css("img::attr(alt)").extract())

        page_data["metadescs"] = self._string_joiner(response.xpath("//meta[@name='description']/@content").extract())

        page_data["title"] = response.css("title::text").extract()[0]

        page_data["viewstate"] = response.xpath("//input[@name='__VIEWSTATE']/@value").extract()[0]

        page_data["pagination"] = self._string_joiner(response.xpath("//link[contains(@rel, 'prev') or contains(@rel, 'next')]").extract())

        page_data["iframe"] = response.xpath("//iframe").extract()[0]

        page_data["flash"] = self._string_joiner(response.xpath("//embed[contains(@src, '.swf')]").extract())

        page_data["noindexnofollow"] = response.xpath("//meta[contains(@content, 'no index, no follow')]/@name]").extract()[0]

        page_data["schematag"] = response.xpath("//div/@itemtype").extract()[0]

        return page_data
