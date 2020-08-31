from flask import current_app

from bs4 import BeautifulSoup
from urllib import parse, request, error

from app.prospector.models import PageData
from app.prospector.scrapers import DomainScraper, PageScraper

# with current_app.app_context():
    # MAX_PAGES_TO_VISIT = current_app.config["MAX_PAGES_TO_VISIT"]

MAX_PAGES_TO_VISIT = 60


def _get_html_soup(url):
    print('OPENING', url)
    raw_html = request.urlopen(url).read()
    return BeautifulSoup(raw_html, "html.parser")


def _get_page_contents(domain_url, url_suffix):

    full_url = parse.urljoin(domain_url, url_suffix)

    try:
        raw_data = request.urlopen(full_url).read()
        if isinstance(raw_data, str) and len(raw_data) < 500000:
            return raw_data.decode('utf-8')
    except error.HTTPError as error_message:
        print('{} for {}'.format(error_message, full_url))


def scrape_domain_data(domain_data):

    domain_url = domain_data.domain_url

    domain_html_soup = _get_html_soup(domain_url)

    domain_data.robots_txt = _get_page_contents(domain_url, 'robots.txt')
    domain_data.sitemap_xml = _get_page_contents(domain_url, 'sitemap.xml')
    domain_data.google_analytics = DomainScraper.scrape_google_analytics(domain_html_soup)
    domain_data.bing_analytics = DomainScraper.scrape_bing_analytics(domain_html_soup)

    return domain_data


def scrape_page_data(page_url, domain):

    page_html_soup = _get_html_soup(page_url)

    print('DOMAIN', domain.id)
    page_data = PageData.query.filter_by(page_url=page_url).filter_by(domain_site=domain).first()

    if not page_data:
        page_data = PageData()
        page_data.page_url = page_url
        page_data.domain_site = domain

    page_data.h1_tags = PageScraper.header_tags(page_html_soup, 'h1')
    page_data.h2_tags = PageScraper.header_tags(page_html_soup, 'h2')
    page_data.h3_tags = PageScraper.header_tags(page_html_soup, 'h3')
    page_data.alt_tags = PageScraper.alt_tags(page_html_soup)
    page_data.meta_descriptions = PageScraper.meta_descriptions(page_html_soup)
    page_data.title_text = PageScraper.title_text(page_html_soup)
    page_data.view_state = PageScraper.view_state(page_html_soup)
    page_data.pagination = PageScraper.pagination(page_html_soup)
    page_data.iframe_content = PageScraper.iframe_content(page_html_soup)
    page_data.flash_attribute = PageScraper.flash_attribute(page_html_soup)
    page_data.no_index_no_follow_attribute = PageScraper.no_index_no_follow_attribute(page_html_soup)
    page_data.schema_tags = PageScraper.schema_tags(page_html_soup)
    page_data.blog_locations = PageScraper.blog_locations(page_html_soup)
    page_data.number_of_internal_links = PageScraper.number_of_internal_links(page_html_soup, page_url)

    return page_data


def spider_site(domain_url):

    urls = [domain_url]

    page_html_soup = _get_html_soup(domain_url)

    for link in page_html_soup.findAll('a', href=True):

        current_url = parse.urljoin(domain_url, link['href'])

        if parse.urlparse(current_url).netloc in parse.urlparse(domain_url).netloc and \
           '#' not in current_url and \
           current_url not in urls and \
           len(urls) < MAX_PAGES_TO_VISIT and \
           '@' not in current_url and \
           ':' not in current_url:
            urls.append(current_url)

    return urls
