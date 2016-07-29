from app import db, models


class Ranker():

    def __init__(self):
        pass

    def rank_domain_data(self):
        pass

    def rank_page_data(self):
        pass

    def rank_site(self):
        pass


total = 0
entries = 0
domaintotal = 0
domainentries = 0


def adddomainscore(score):
    global domaintotal
    global domainentries

    domaintotal += score
    domainentries += 1


def addscore(score):
    global total
    global entries

    total += score
    entries += 1


def Ranker(websiteurl):

    # Load in the site to be ranked
    site = models.Site.query.filter(models.Site.domainurl == websiteurl).first()

    # Domain ranking
    if site.binganalytics:
        adddomainscore(8)
    else:
        adddomainscore(3)

    if site.googleanalytics:
        adddomainscore(9)
    else:
        adddomainscore(2)

    if site.robots:
        adddomainscore(9)
    else:
        adddomainscore(2)

    if site.sitemap:
        adddomainscore(9)
    else:
        adddomainscore(3)

    # List checks
    h1checklist = []
    h2checklist = []
    h3checklist = []
    alttagchecklist = []
    metadescchecklist = []
    titlechecklist = []
    pagecount = 0

    # Page ranking
    for page in site.pages:

        pagecount += 1

        # List checks
        h1s = page.h1s.split('#')
        for h1 in h1s:
            if h1 in h1checklist:
                addscore(3)
                break
            else:
                addscore(9)
                h1checklist.append(h1)

        h2s = page.h2s.split('#')
        for h2 in h2s:
            if h2 in h2checklist:
                addscore(3)
                break
            else:
                addscore(8)
                h2checklist.append(h2)

        h3s = page.h3s.split('#')
        for h3 in h3s:
            if h3 in h3checklist:
                addscore(4)
                break
            else:
                addscore(7)
                h3checklist.append(h3)

        alttags = page.alttags.split('#')
        for alttag in alttags:
            if alttag in alttagchecklist:
                addscore(4)
                break
            else:
                addscore(6)
                alttagchecklist.append(alttag)

        metadescs = page.metadesc.split('#')
        for metadesc in metadescs:
            if metadesc in metadescchecklist:
                addscore(4)
                break
            else:
                addscore(7)
                metadescchecklist.append(metadesc)

        # Slightly different as there is (should be) only one title
        title = page.title
        if title in titlechecklist:
            addscore(2)
        else:
            addscore(8)
        titlechecklist.append(title)

        # Boolean checks
        if page.viewstate:
            addscore(2)

        if page.pagination:
            addscore(8)

        if page.iframe:
            addscore(4)

        if page.flash:
            addscore(3)

        if page.noindexnofollow:
            addscore(6)

        if page.schematag:
            addscore(7)

        if page.bloglocation:
            addscore(7)

        if page.internallinksno > 9:
            addscore(8)
        elif page.internallinksno > 19:
            addscore(9)
        else:
            addscore(3)

        if len(page.pageurl) < 100:
            addscore(7)
        elif len(page.pageurl) < 150:
            addscore(4)
        else:
            addscore(3)

    pageranking = (total / entries) * 10  # average score between 0 and 100
    factor = 0.2  # a third of the score is the domain. This could be made dependent on the amount of pages
    domainranking = (domaintotal / domainentries) * 10  # score between 0 and 100

    ranking = (pageranking + (domainranking * factor)) / (1 + factor)

    site.ranking = round(ranking)

    if (site.ranking / 25) < 1:
        site.level = 'low'
    elif (site.ranking / 25) < 2:
        site.level = 'midlow'
    elif (site.ranking / 25) < 3:
        site.level = 'midhigh'
    elif (site.ranking / 25) < 4:
        site.level = 'high'

    db.session.commit()
