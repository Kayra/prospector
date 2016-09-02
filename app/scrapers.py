
class DomainScraper():

    @staticmethod
    def scrape_google_analytics(domain_html_soup):

        for script in domain_html_soup.find_all('script'):
            if script.string and len(script.string) < 10000:
                if ('urchin' or 'googleanalytics') in script.string.lower():
                    return script.string
                elif script.string and ('googleanalytics' or '_uacct' or 'pagetracker') in script.string.lower():
                    return script.string

    @staticmethod
    def scrape_bing_analytics(domain_html_soup):

        for script in domain_html_soup.find_all('script'):
            if script.string and 'mstag' in script.string and script.string < 10000:
                return script

        for meta in domain_html_soup.find_all('meta'):
            if 'msvaldiate' in meta and meta < 10000:
                return meta


class PageScraper():

    def no_tag_exception_handler(scraping_function):
        def function(*args, **kwargs):
            try:
                return scraping_function(*args, **kwargs)
            except KeyError:
                return None
        return function

    @staticmethod
    def header_tags(page_html_soup, header_tag_to_scrape):
        return "#".join([header_tag.string for header_tag in page_html_soup.find_all(header_tag_to_scrape)])

    @staticmethod
    def alt_tags(page_html_soup):
        return "#".join([img['alt'] for img in page_html_soup.find_all('img') if 'alt' in img])

    @staticmethod
    @no_tag_exception_handler
    def meta_desc(page_html_soup):
        return "#".join([meta_desc['content'] for meta_desc in page_html_soup.find_all('meta') if ('description' in meta_desc['name'].lower()) and (len(meta_desc['content']) < 1000)])

    @staticmethod
    def title(page_html_soup):
        return page_html_soup.title.text if page_html_soup.title else None

    @staticmethod
    @no_tag_exception_handler
    def view_state(page_html_soup):
        view_state = [input_tag['value'] for input_tag in page_html_soup.find_all('input') if '__VIEWSTATE' in input_tag['name'].lower()]
        return str(view_state[0]) if view_state else None

    @staticmethod
    @no_tag_exception_handler
    def pagination(page_html_soup):
        pagination = [link_tag for link_tag in page_html_soup.find_all('link') if ('prev' or 'next') in str(link_tag['rel']).lower()]
        return str(pagination[0]) if pagination else None

    @staticmethod
    def iframe(page_html_soup):
        return page_html_soup.iframe.text if page_html_soup.iframe else None

    @staticmethod
    @no_tag_exception_handler
    def flash(page_html_soup):
        flash = [embed_tag for embed_tag in page_html_soup.find_all('embed') if '.swf' in embed_tag['src'].lower()]
        return str(flash[0]) if flash else None

    @staticmethod
    @no_tag_exception_handler
    def no_index_no_follow(page_html_soup):
        no_index_no_follow = [meta_tag['name'] for meta_tag in page_html_soup.find_all('meta') if 'noindex, nofollow' in meta_tag['content'].lower() and meta_tag.get('name')]
        return str(no_index_no_follow[0]) if no_index_no_follow else None

    @staticmethod
    def schema_tag(page_html_soup):
        return "#".join([schema_tag for schema_tag in page_html_soup.find_all('div') if schema_tag.get('itemtype')])

    @staticmethod
    @no_tag_exception_handler
    def blog_location(page_html_soup):
        return "#".join([link_tag['href'] for link_tag in page_html_soup.find_all('a', href=True) if ('blog' in str(link_tag)) or ('blog' in link_tag['href'])])

    @staticmethod
    def number_of_internal_links(page_html_soup, domain_url):
        return len([link for link in page_html_soup.find_all('a', href=True) if domain_url in link['href']])
