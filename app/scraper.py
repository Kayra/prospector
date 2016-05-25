import logging


class DomainData:

    def __init__(self, binganalytics, googleanalytics):
        self.binganalytics = binganalytics
        self.googleanalytics = googleanalytics


class PageData:

    def __init__(self, h1s, h2s, h3s, alttags, metadesc, title, viewstate, pagination, iframe, flash, noindexnofollow, schematag, bloglocation, internallinksno):
        self.h1s = h1s
        self.h2s = h2s
        self.h3s = h3s
        self.alttags = alttags
        self.metadesc = metadesc
        self.title = title
        self.viewstate = viewstate
        self.pagination = pagination
        self.iframe = iframe
        self.flash = flash
        self.noindexnofollow = noindexnofollow
        self.schematag = schematag
        self.bloglocation = bloglocation
        self.internallinksno = internallinksno


def DomainScrape(soup, domainurl):

    # Google analytics check
    googleanalytics = ""
    for script in soup.find_all('script'):
        if ('urchin' or 'googleanalytics') in script:
            if script.string and len(script.string) < 10000:
                googleanalytics = script
            break
        elif script.string and ('googleanalytics' or '_uacct' or 'pagetracker') in script.string.lower():
            if script.string and len(script.string) < 10000:
                googleanalytics = script
            break

    # Bing analytics check
    binganalytics = ""
    for script in soup.find_all('script'):
        if script.string and 'mstag' in script.string and script.string < 10000:
            binganalytics = script
            break
    for meta in soup.find_all('meta'):
        if 'msvaldiate' in meta and meta < 10000:
            binganalytics = meta
            break

    domaindata = DomainData(binganalytics, googleanalytics)

    return domaindata


def PageScrape(soup, domainurl):

    # Scrape all the h1s from the page
    h1s = ""
    for h1 in soup.find_all('h1'):
        if h1:
            h1s += str(h1) + '#'

    # Scrape all the h2s from the page
    h2s = ""
    for h2 in soup.find_all('h2'):
        if h2:
            h2s += str(h2) + '#'

    # Scrape all the h3s from the page
    h3s = ""
    for h3 in soup.find_all('h3'):
        if h3:
            h3s += str(h3) + '#'

    # Scrape all the alt tags from the page
    alttags = ""
    for alttag in soup.find_all('img'):
        if alttag:
            try:
                alttags += alttag['alt'] + '#'
            except KeyError:
                logging.info('Key error: the image did not contain an alt attribute.')

    # Scrape all the meta descriptions from the page
    metadescs = ""
    for metadesc in soup.find_all('meta'):
        try:
            if ('description' in metadesc['name'].lower()) and (len(metadesc['content']) < 1000):
                metadescs += metadesc['content'] + '#'
        except KeyError:
            logging.info('Key error: the metatag did not contain a name attribute.')

    # Scrape the title of the page
    title = ""
    if soup.title:
        title = str(soup.title)

    # Check if there is a viewstate, if so scrape it
    viewstate = ""
    if (type(viewstate) != str):
        for inputtag in soup.find_all('input'):
            try:
                if '__VIEWSTATE' in inputtag['name'].lower():
                    viewstate = inputtag['value']
            except KeyError:
                logging.info('Key error: the input tag did not contain a viewstate attribute.')

    # Check if the page contains pagination
    pagination = ""
    for pagin in soup.find_all('link'):
        try:
            if ('prev' or 'next') in str(pagin['rel']).lower():
                pagination = str(pagin)
        except KeyError:
                logging.info('Key error: the input tag did not contain a viewstate attribute.')

    # Check if the page contains an iframe
    iframe = ""
    if soup.iframe:
        iframe = str(soup.iframe)

    # Check if the page uses flash
    flash = ""
    for flashtag in soup.find_all('embed'):
        try:
            if '.swf' in flashtag['src'].lower():
                flash = str(flashtag)
        except KeyError:
                logging.info('Key error: embed tag did not contain an src attribute')

    # Check if the page contains a no index no follow
    noindexnofollow = ""
    for noindextag in soup.find_all('meta'):
        try:
            if 'noindex, nofollow' in noindextag['content'].lower() and noindextag['name']:
                noindexnofollow = noindextag['name']
        except KeyError:
                logging.info('Key error: meta tag did not contain content attribute')

    # Check if the page contains a schematag
    schematag = ""
    for schema in soup.find_all('div'):
        try:
            if schema['itemtype']:
                schematag += str(schema) + '#'
        except KeyError:
                logging.info('Key error: div tag did not contain schema attribute')

    # Check if the page links to a blog, if so scrape it
    bloglocation = ""
    for blog in soup.find_all('a', href=True):
        try:
            if ('blog' in str(blog)) or ('blog' in blog['href']):
                bloglocation += blog['href'] + '@'
        except KeyError:
                logging.info('Key error: meta tag did not contain content attribute')

    # Record how many internal links the page contains
    internallinksno = 0
    for link in soup.find_all('a', href=True):
        try:
            if (domainurl in link['href']) or ('.' not in link['href']):
                internallinksno += 1
        except KeyError:
            logging.info('Key error: link tag did not contain href attribute')

    pagedata = PageData(h1s, h2s, h3s, alttags, metadescs, title, viewstate, pagination, iframe, flash, noindexnofollow, schematag, bloglocation, internallinksno)

    return pagedata
