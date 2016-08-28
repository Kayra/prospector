from app.models import DomainData, PageData, db
from app.scrapers import DomainScraper, PageScraper
import urllib.parse as urlparse
import urllib
from bs4 import BeautifulSoup


class Crawler():

    def __init__(self, domain_url):
        self._MAX_PAGES_TO_VISIT = 60
        self.domain_url = domain_url
        self.crawl_site(self.domain_url)

    def get_html_soup(self, url):
        raw_html = urllib.request.urlopen(url).read()
        return BeautifulSoup(raw_html, "html.parser")

    def get_page_contents(self, url_suffix):

        full_url = urlparse.urljoin(self.domain_url, url_suffix)

        try:
            raw_data = urllib.request.urlopen(full_url).read()
            if raw_data.isinstance(str) and len(raw_data) < 500000:
                return raw_data.decode('utf-8')
        except urllib.error.HTTPError as error_message:
            print('{} for {}'.format(error_message, full_url))

    def scrape_domain_data(self, domain_url):

        domain_html_soup = self.get_html_soup(domain_url)

        robots_txt_contents = self.get_page_contents('robots.txt')
        sitemap_contents = self.get_page_contents('sitemap.xml')
        google_analytics = DomainScraper.scrape_google_analytics(domain_html_soup)
        bing_analytics = DomainScraper.scrape_bing_analytics(domain_html_soup)

        domain_data = DomainData(domain_url=domain_url,
                                 site_name=domain_url.split('.')[1],
                                 robots=robots_txt_contents,
                                 sitemap=sitemap_contents,
                                 google_analytics=google_analytics,
                                 bing_analytics=bing_analytics)

        db.session.add(domain_data)
        db.session.commit()

    def scrape_page_data(self, page_url):

        page_html_soup = self.get_html_soup(page_url)

        h1s = PageScraper.header_tags(page_html_soup, 'h1')
        h2s = PageScraper.header_tags(page_html_soup, 'h2')
        h3s = PageScraper.header_tags(page_html_soup, 'h3')
        alt_tags = PageScraper.alt_tags(page_html_soup)
        meta_desc = PageScraper.meta_desc(page_html_soup)
        title = PageScraper.title(page_html_soup)
        view_state = PageScraper.view_State(page_html_soup)
        pagination = PageScraper.pagination(page_html_soup)
        iframe = PageScraper.iframe(page_html_soup)
        flash = PageScraper.flash(page_html_soup)
        no_index_no_follow = PageScraper.no_index_no_follow(page_html_soup)
        schema_tag = PageScraper.schema_tag(page_html_soup)
        blog_location = PageScraper.blog_location(page_html_soup)
        number_of_internal_links = PageScraper.number_of_internal_links(page_html_soup)

        page_data = PageData(page_url=page_url,
                             h1s=h1s,
                             h2s=h2s,
                             h3s=h3s,
                             alt_tags=alt_tags,
                             meta_desc=meta_desc,
                             title=title,
                             view_state=view_state,
                             pagination=pagination,
                             iframe=iframe,
                             flash=flash,
                             no_index_no_follow=no_index_no_follow,
                             schema_tag=schema_tag,
                             blog_location=blog_location,
                             number_of_internal_links=number_of_internal_links)

        db.session.add(page_data)
        db.session.commit()

    def spider_site(self, domain_url):

        urls = [domain_url]

        page_html_soup = self.get_html_soup(domain_url)

        for link in page_html_soup.findAll('a', href=True):

            current_url = urlparse.urljoin(domain_url, link['href'])

            if urlparse.urlparse(current_url).netloc in urlparse.urlparse(current_url).netloc and '#' not in current_url and current_url not in urls and len(urls) < self._MAX_PAGES_TO_VISIT:
                urls.append(current_url)

            return urls

    def crawl_site(self, domain_url):

        self.scrape_domain_data(domain_url)
        [self.scrape_page_data(page_url) for page_url in self.spider_site(domain_url)]
