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


def create_default_domain_scores():
    pass


def create_default_page_scores():
    pass
