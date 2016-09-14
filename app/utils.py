from urllib.parse import urlparse


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
