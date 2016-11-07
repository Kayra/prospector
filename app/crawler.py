from bs4 import BeautifulSoup

import urllib.parse as urlparse
import urllib

from app.models import DomainData, PageData
from app.scrapers import DomainScraper, PageScraper
from app.utils import extract_site_name
from config import MAX_PAGES_TO_VISIT


class Crawler():

    def _get_html_soup(self, url):
        raw_html = urllib.request.urlopen(url).read()
        return BeautifulSoup(raw_html, "html.parser")

    def _get_page_contents(self, domain_url, url_suffix):

        full_url = urlparse.urljoin(domain_url, url_suffix)

        try:
            raw_data = urllib.request.urlopen(full_url).read()
            if raw_data.isinstance(str) and len(raw_data) < 500000:
                return raw_data.decode('utf-8')
        except urllib.error.HTTPError as error_message:
            print('{} for {}'.format(error_message, full_url))

    def scrape_domain_data(self, domain_url, domain_data=None):

        domain_html_soup = self._get_html_soup(domain_url)

        robots_txt = self._get_page_contents(domain_url, 'robots.txt')
        sitemap_xml = self._get_page_contents(domain_url, 'sitemap.xml')
        google_analytics = DomainScraper.scrape_google_analytics(domain_html_soup)
        bing_analytics = DomainScraper.scrape_bing_analytics(domain_html_soup)

        if domain_data:
            domain_data.robots_txt = robots_txt
            domain_data.sitemap_xml = sitemap_xml
            domain_data.google_analytics = google_analytics
            domain_data.bing_analytics = bing_analytics

        else:
            domain_data = DomainData(domain_url=domain_url,
                                     site_name=extract_site_name(domain_url),
                                     robots_txt=robots_txt,
                                     sitemap_xml=sitemap_xml,
                                     google_analytics=google_analytics,
                                     bing_analytics=bing_analytics)

        return domain_data

    def scrape_page_data(self, page_url, domain):

        page_html_soup = self._get_html_soup(page_url)

        h1_tags = PageScraper.header_tags(page_html_soup, 'h1')
        h2_tags = PageScraper.header_tags(page_html_soup, 'h2')
        h3_tags = PageScraper.header_tags(page_html_soup, 'h3')
        alt_tags = PageScraper.alt_tags(page_html_soup)
        meta_description = PageScraper.meta_description(page_html_soup)
        title_text = PageScraper.title_text(page_html_soup)
        view_state = PageScraper.view_state(page_html_soup)
        pagination = PageScraper.pagination(page_html_soup)
        iframe_content = PageScraper.iframe_content(page_html_soup)
        flash_attribute = PageScraper.flash_attribute(page_html_soup)
        no_index_no_follow_attribute = PageScraper.no_index_no_follow_attribute(page_html_soup)
        schema_tag = PageScraper.schema_tag(page_html_soup)
        blog_location = PageScraper.blog_location(page_html_soup)
        number_of_internal_links = PageScraper.number_of_internal_links(page_html_soup, page_url)

        page_data = PageData(page_url=page_url,
                             h1_tags=h1_tags,
                             h2_tags=h2_tags,
                             h3_tags=h3_tags,
                             alt_tags=alt_tags,
                             meta_description=meta_description,
                             title_text=title_text,
                             view_state=view_state,
                             pagination=pagination,
                             iframe_content=iframe_content,
                             flash_attribute=flash_attribute,
                             no_index_no_follow_attribute=no_index_no_follow_attribute,
                             schema_tag=schema_tag,
                             blog_location=blog_location,
                             number_of_internal_links=number_of_internal_links,
                             domain_site=domain)

        return page_data

    def spider_site(self, domain_url):

        urls = [domain_url]

        page_html_soup = self._get_html_soup(domain_url)

        for link in page_html_soup.findAll('a', href=True):

            current_url = urlparse.urljoin(domain_url, link['href'])

            if urlparse.urlparse(current_url).netloc in urlparse.urlparse(domain_url).netloc and '#' not in current_url and current_url not in urls and len(urls) < MAX_PAGES_TO_VISIT and '@' not in current_url:
                urls.append(current_url)

        return urls

    def crawl_site(self, domain_url):

        self.scrape_domain_data(domain_url)
        for page_url in self.spider_site(domain_url):
            self.scrape_page_data(page_url)
