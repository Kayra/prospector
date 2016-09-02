
def format_url(url):

    if 'www.' not in url and 'http://' not in url:
        return 'http://www.' + url
    elif 'http://' not in url:
        return 'http://' + url
    else:
        return url


def extract_site_name(url):
    return url.split('.')[1]
