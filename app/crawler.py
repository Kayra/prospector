from app.models import DomainData, PageData, db
from app.scraper import DomainScraper, PageScraper
import urllib.parse as urlparse
import urllib
from bs4 import BeautifulSoup


class Crawler():

    def __init__(self, domain_url):
        self._MAX_PAGES_TO_VISIT = 60
        self.domain_url = domain_url

    def get_html_soup(self, url):
        raw_html = urllib.request.urlopen(url).read()
        return BeautifulSoup(raw_html, "html.parser")

    def get_page_contents(self, url_suffix):
        full_url = urlparse.urljoin(self.domain_url, url_suffix)
        raw_data = urllib.request.urlopen(full_url).read()
        if raw_data.isinstance(str) and len(raw_data) < 500000:
            return raw_data.decode('utf-8')

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
                                 gooogle_analytics=google_analytics,
                                 bing_analytics=bing_analytics)

        db.session.add(domain_data)
        db.session.commit()

    def scrape_page_data(self, page_url):

        page_html_soup = self.get_html_soup(page_url)

        h1s = PageScraper.h1s(page_html_soup)
        h2s = PageScraper.h2s(page_html_soup)
        h3s = PageScraper.h3s(page_html_soup)
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

        urls = list(domain_url)

        page_html_soup = self.get_html_soup(domain_url)

        for link in page_html_soup.findAll('a', href=True):

            current_url = urlparse.urljoin(domain_url, link['href'])

            if urlparse.urlparse(page_html_soup).netloc in urlparse.urlparse(current_url).netloc and '#' not in current_url and current_url not in urls and len(urls) < self._MAX_PAGES_TO_VISIT:
                urls.append(current_url)

            return urls


def Crawler(url):

    urls = [url]
    visited = [url]

    domainhtml = urllib.request.urlopen(url).read()

    domainsoup = BeautifulSoup(domainhtml, "html.parser")

    # Scrape the page
    domaindata = DomainScrape(domainsoup, url)
    domainpagedata = PageScrape(domainsoup, url)

    # Cut out the domain name
    domainname = url.split(".")

    # Check if there is a robots file
    # Scrape the robots file
    robotsfile = ""
    robotsurl = urlparse.urljoin(url, 'robots.txt')
    try:
        robotsdata = urllib.request.urlopen(robotsurl).read()
        if robotsdata and type(robotsdata) is str and len(robotsdata) < 50000:
            robotsfile = robotsdata.decode('utf-8')
    except Exception as error:
        print(error)
        print("Unable to scrape robots.txt")

    # Check if there is a sitemap file
    # Scrape the sitemap file
    sitemapfile = ""
    sitemapurl = urlparse.urljoin(url, 'sitemap.xml')
    try:
        sitemapdata = urllib.request.urlopen(sitemapurl).read()
        if sitemapdata and isinstance(sitemapdata, (str)) and len(sitemapdata) < 50000:
            sitemapfile = sitemapdata.decode('utf-8')
    except Exception as error:
        print(error)
        print("Unable to scrape sitemap.xml")

    # Add the domain information to the db
    url = url
    s = models.Site(domainurl=url, sitename=domainname[1], binganalytics=domaindata.binganalytics, googleanalytics=domaindata.googleanalytics, robots=robotsfile, sitemap=sitemapfile, ranking=0)
    db.session.add(s)

    # Add the page information to the db
    h = models.Page(pageurl=url, h1s=domainpagedata.h1s, h2s=domainpagedata.h2s, h3s=domainpagedata.h3s, alttags=domainpagedata.alttags, metadesc=domainpagedata.metadesc, title=domainpagedata.title, viewstate=domainpagedata.viewstate, pagination=domainpagedata.pagination, iframe=domainpagedata.iframe, flash=domainpagedata.flash, noindexnofollow=domainpagedata.noindexnofollow, schematag=domainpagedata.schematag, bloglocation=domainpagedata.bloglocation, internallinksno=domainpagedata.internallinksno, domainsite=s)

    db.session.add(h)
    db.session.commit()

    # Get all the urls in the page
    GetUrls(domainsoup, url, urls, visited)

    while (len(urls) > 0) and len(visited) < 60:
        for pageurl in urls:

            # Download the page
            try:
                pagehtml = urllib.request.urlopen(pageurl).read()
                pagesoup = BeautifulSoup(pagehtml, "html.parser")
                visited.append(pageurl)
            except Exception as error:
                print('Couldn\'t download:')
                print(pageurl)
                print('Because:')
                print(error)
                pagehtml = None
                pagesoup = None

            # ensures the top level domain is included
            # pageurl = urlparse.urljoin(url, pageurl)

            if pagesoup and url in pageurl:
                # Get all the urls in the page
                GetUrls(pagesoup, url, urls, visited)
                # Scrape the page
                domainpagedata = PageScrape(pagesoup, pageurl)

                # Add the page information to the db
                h = models.Page(pageurl=pageurl, h1s=domainpagedata.h1s, h2s=domainpagedata.h2s, h3s=domainpagedata.h3s, alttags=domainpagedata.alttags, metadesc=domainpagedata.metadesc, title=domainpagedata.title, viewstate=domainpagedata.viewstate, pagination=domainpagedata.pagination, iframe=domainpagedata.iframe, flash=domainpagedata.flash, noindexnofollow=domainpagedata.noindexnofollow, schematag=domainpagedata.schematag, bloglocation=domainpagedata.bloglocation, internallinksno=domainpagedata.internallinksno, domainsite=s)
                db.session.add(h)
                db.session.commit()

            urls.pop(0)
            if len(visited) > 60:
                break

    return domainname[1]


def GetUrls(soup, domainurl, urls, visited):

    for tag in soup.findAll('a', href=True):

        # Ensures the top level domain is included
        currenturl = urlparse.urljoin(domainurl, tag['href'])

        # Check that the url goes to the website we are scraping
        # Make sure we haven't already visited it
        # and '.' not in urlparse.urlparse(currenturl).path
        if urlparse.urlparse(domainurl).netloc in urlparse.urlparse(currenturl).netloc and currenturl not in visited and '#' not in currenturl and currenturl not in urls:
            print("ADDING: %s" % currenturl)
            # Add to urls to scrape
            urls.append(currenturl)
