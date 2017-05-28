from urllib.parse import urlparse

from app.prospector.models import DomainData, DomainScores, PageScores


def format_url(url):

    if 'www.' not in url and 'http://' not in url:
        return 'http://www.' + url

    elif 'http://' not in url:
        return 'http://' + url

    else:
        return url


def extract_site_name(url):

    parsed_url = urlparse(url)
    position = 1 if 'www' in parsed_url.netloc else 0

    return parsed_url.netloc.split('.')[position]


def get_or_create_domain_data(domain_url, user):

    if user is not None:
        domain_data = DomainData.query.filter_by(domain_url=domain_url).filter_by(owner=user.id).first()
    else:
        domain_data = DomainData.query.filter_by(domain_url=domain_url).filter_by(owner=None).first()

    if domain_data is None and user is not None:
        domain_data = DomainData(domain_url=domain_url, site_name=extract_site_name(domain_url), owner=user.id)
    elif domain_data is None:
        domain_data = DomainData(domain_url=domain_url, site_name=extract_site_name(domain_url))

    return domain_data


def create_default_domain_scores(owner=None):

    default_domain_scores = DomainScores(google_analytics=9,
                                         bing_analytics=8,
                                         robots_txt=9,
                                         sitemap_xml=9,
                                         owner=owner)

    return default_domain_scores


def create_default_page_scores(owner=None):

    default_page_scores = PageScores(h1_tags=9,
                                     h2_tags=8,
                                     h3_tags=7,
                                     alt_tags=6,
                                     meta_descriptions=7,
                                     title_text=8,
                                     view_state=2,
                                     pagination=8,
                                     iframe_content=4,
                                     flash_attribute=3,
                                     no_index_no_follow_attribute=6,
                                     schema_tags=7,
                                     blog_locations=8,
                                     number_of_internal_links={
                                         "high": {
                                             19: 9
                                         },
                                         "medium": {
                                             9: 7
                                         },
                                         "low": {
                                             8: 5
                                         }
                                     },
                                     url_character_length={
                                         "high": {
                                             150: 2
                                         },
                                         "medium": {
                                             100: 4
                                         },
                                         "low": {
                                             50: 7
                                         },
                                     },
                                     owner=owner)

    return default_page_scores


def load_domain_scores_form_to_model(domain_score_form, domain_score_model):
    pass
